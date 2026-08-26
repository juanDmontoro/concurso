"""Inyecta en un deck Quarto las «Versión editada» de su esquema de notas de orador.

Uso (desde la raíz de catedra/):
  python 0_ejercicio/deck/scripts/inyectar_notas.py \
      0_ejercicio/cv/deck/presentacion_cv_esquema.md 0_ejercicio/cv/deck/presentacion_cv.qmd [--dry-run]
  python 0_ejercicio/deck/scripts/inyectar_notas.py \
      0_ejercicio/propuesta_docente/sol/propuesta_docente_esquema.md \
      0_ejercicio/propuesta_docente/sol/propuesta_docente.qmd [--dry-run]

El esquema es el documento que revisa el autor; este script lo vuelca al deck
(fuente de las notas = «Versión editada» del esquema). Tras inyectar: renderizar el
deck, comprobar aside.notes = slides visibles y paginación Beamer sin cambios, y
re-sincronizar el deck unificado con sync_partes.py.

Para cada slide visible (`##` fuera de `::: {.content-hidden}`) del deck, localiza el
bloque `::: {.notes}` de esa slide y sustituye su contenido por la «Versión editada»
del esquema (emparejada por título de slide, en orden). Si la slide no tiene bloque
de notas, lo crea al final de la slide (antes del siguiente encabezado o del cierre
del contenedor). Las slides ocultas y las secciones `#` no se tocan.

Con --dry-run no escribe: imprime el resumen y las diferencias de recuento.
"""

import re
import sys
from pathlib import Path


def leer_esquema(path: Path):
    s = path.read_text(encoding="utf-8")
    # bloques: "## Título" ... "#### Versión editada\n\n<texto>" hasta el siguiente "## " o "# "
    bloques = re.findall(r"^## (.+?)\n(.*?)(?=^## |^# |\Z)", s, flags=re.M | re.S)
    notas = []
    for titulo, cuerpo in bloques:
        m = re.search(r"#### Versión editada\n\n(.*)\Z", cuerpo, flags=re.S)
        if not m:
            continue
        notas.append((titulo.strip(), m.group(1).strip()))
    return notas


def slides_visibles(lines, start):
    """Devuelve lista de dicts con índices de línea de cada slide ## visible y de su bloque .notes."""
    depth = []
    slides = []
    cur = None
    in_notes = False
    notes_depth = None

    def cerrar(i):
        nonlocal cur
        if cur is not None:
            cur["end"] = i
            slides.append(cur)
            cur = None

    for i in range(start, len(lines)):
        st = lines[i].strip()
        m = re.match(r"^(#{1,2}) (.*)$", st)
        in_callout = bool(depth) and depth[-1] == "C"
        if m and not st.startswith("###") and not in_notes and not in_callout:
            cerrar(i)
            cur = {"kind": m.group(1), "title": re.sub(r"\s*\{[^}]*\}\s*$", "", m.group(2)).strip(),
                   "hidden": any(d == "H" for d in depth), "start": i, "notes": None, "depth_at_start": len(depth)}
            continue
        if re.match(r"^:{3,}\s*(\{|[A-Za-z.#])", st):
            tag = "H" if "content-hidden" in st else ("C" if "callout" in st else "D")
            # un bloque content-hidden que se abre al nivel de la slide actual la termina
            if tag == "H" and cur is not None and len(depth) == cur["depth_at_start"]:
                cerrar(i)
            depth.append(tag)
            if ".notes" in st and cur is not None:
                in_notes = True
                notes_depth = len(depth)
                cur["notes"] = [i, None]
            continue
        if re.match(r"^:{3,}\s*$", st):
            if in_notes and len(depth) == notes_depth:
                in_notes = False
                notes_depth = None
                cur["notes"][1] = i
            if depth:
                depth.pop()
            # el cierre de un contenedor abierto antes de la slide la termina
            if cur is not None and len(depth) < cur["depth_at_start"]:
                cerrar(i)
            continue
    cerrar(len(lines))
    return [s for s in slides if s["kind"] == "##" and not s["hidden"]]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    esquema, deck = Path(args[0]), Path(args[1])
    notas = leer_esquema(esquema)
    txt = deck.read_text(encoding="utf-8")
    assert txt.startswith("---\n")
    yaml_end = txt.index("\n---\n", 4) + 5
    lines = txt.splitlines(keepends=True)
    # índice de línea donde empieza el cuerpo
    start = txt[:yaml_end].count("\n")
    vis = slides_visibles(lines, start)
    if len(vis) != len(notas):
        sys.exit(f"ERROR: {len(vis)} slides visibles en el deck y {len(notas)} notas en el esquema")
    for s, (t, _) in zip(vis, notas):
        if s["title"] != t:
            sys.exit(f"ERROR: títulos no coinciden: deck «{s['title']}» vs esquema «{t}»")

    creadas = sustituidas = 0
    # aplicar de abajo arriba para no desplazar índices
    for s, (t, prosa) in reversed(list(zip(vis, notas))):
        bloque = "::: {.notes}\n" + prosa + "\n:::\n"
        if s["notes"]:
            a, b = s["notes"]
            lines[a:b + 1] = [bloque]
            sustituidas += 1
        else:
            # insertar antes del final de la slide; retroceder sobre líneas en blanco y
            # sobre el cierre `:::` de un contenedor que envuelva la slide (p. ej. content-visible)
            j = s["end"]
            while j > s["start"] + 1 and lines[j - 1].strip() == "":
                j -= 1
            lines[j:j] = ["\n", bloque]
            creadas += 1
    nuevo = "".join(lines)
    n_vis_notes = len(re.findall(r"^:::\s*\{\.notes\}", nuevo, flags=re.M))
    print(f"{deck.name}: {len(vis)} slides visibles · {sustituidas} notas sustituidas · {creadas} creadas · "
          f"{n_vis_notes} bloques .notes en total (incl. ocultas)")
    if dry:
        print("(dry-run: no se escribe)")
        return
    deck.write_text(nuevo, encoding="utf-8")
    print("escrito")


if __name__ == "__main__":
    main()
