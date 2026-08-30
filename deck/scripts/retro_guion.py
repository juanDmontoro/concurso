#!/usr/bin/env python3
"""Retro-propaga ediciones hechas sobre ``guion_lectura.qmd`` a los esquemas de notas.

El guion de lectura es un fichero generado (``generar_guion.py``) y no debería
editarse; cuando aun así se corrige su prosa a mano, este script devuelve esas
correcciones aguas arriba, al punto del pipeline donde las notas son fuente:

- slides ``##`` de las Partes 1 y 2 → sección «Versión editada» de sus esquemas
  (``presentacion_cv_esquema.md``, ``propuesta_docente_esquema.md``), listas para
  ``inyectar_notas.py``;
- notas de sección ``#`` (sin representación en los esquemas; hoy solo
  «Tema 7» en la Parte 2) → directamente al bloque ``::: {.notes}`` del deck
  fuente, y solo si cambiaron.

La Parte 3 queda fuera del alcance: sus marcas se validan pero cualquier cambio
de texto en ella aborta el volcado.

Método: se regenera en memoria el guion canónico a partir de los ``_parte*.qmd``
(la misma emisión de ``generar_guion.redactar``), se trocean ambos guiones en
bloques anclados en ``\\guionmarca{...}`` y se exige que la secuencia de marcas
coincida 1:1; la diferencia de texto entre bloques homólogos es la edición a
retro-propagar. Los esquemas se reescriben en TODAS las slides (no solo las
editadas): tras el recorte de f23e0be los decks van por delante de los esquemas
y una inyección desde un esquema a medio actualizar desharía ese recorte.

Uso (desde ``0_ejercicio/deck``):

    python scripts/retro_guion.py --dry-run
    python scripts/retro_guion.py
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from extraer_notas import HEADING, PARTES, limpiar_titulo
from generar_guion import Item, recorrer, redactar

ESQUEMAS = {
    0: Path("../cv/deck/presentacion_cv_esquema.md"),
    1: Path("../propuesta_docente/sol/propuesta_docente_esquema.md"),
}
DECKS_FUENTE = {
    0: Path("../cv/deck/presentacion_cv.qmd"),
    1: Path("../propuesta_docente/sol/propuesta_docente.qmd"),
}

SEPARADORES = {
    "\\medskip",
    "\\bigskip",
    "\\needspace{2\\baselineskip}",
    "\\needspace{3\\baselineskip}",
    "\\vspace{2\\baselineskip}",
}


@dataclass
class Bloque:
    """Un bloque del guion: la marca de margen y la prosa que ancla."""

    marca: str
    texto: str


def extraer_marca(linea: str) -> tuple[str, str]:
    """Separa ``\\guionmarca{...}`` (llaves balanceadas) del resto de la línea."""
    prefijo = "\\guionmarca{"
    profundidad = 1
    for j in range(len(prefijo), len(linea)):
        if linea[j] == "{":
            profundidad += 1
        elif linea[j] == "}":
            profundidad -= 1
            if profundidad == 0:
                resto = linea[j + 1:]
                return linea[len(prefijo):j], resto[1:] if resto.startswith(" ") else resto
    raise SystemExit(f"marca sin cerrar en el guion: {linea[:80]}…")


def bloques_guion(texto: str) -> list[Bloque]:
    """Trocea el cuerpo del guion (tras ``\\clearpage``) en bloques anclados."""
    lineas = texto.splitlines()
    try:
        inicio = lineas.index("\\clearpage")
    except ValueError:
        raise SystemExit("no encuentro \\clearpage en el guion")
    bloques: list[Bloque] = []
    marca: str | None = None
    cuerpo: list[str] = []

    def cerrar() -> None:
        if marca is not None:
            bloques.append(Bloque(marca, "\n".join(cuerpo).strip()))

    for linea in lineas[inicio + 1:]:
        if linea.strip() in SEPARADORES:
            continue
        if linea.startswith("\\guionmarca{"):
            cerrar()
            marca, resto = extraer_marca(linea)
            cuerpo = [resto]
        elif marca is not None:
            cuerpo.append(linea)
    cerrar()
    return bloques


def duenos_de_bloques(partes_items: list[list[Item]]) -> list[tuple[int | None, Item | None]]:
    """(índice de parte, ítem) por cada bloque del guion, en orden; el cierre es (None, None)."""
    duenos: list[tuple[int | None, Item | None]] = []
    for p, items in enumerate(partes_items):
        duenos.extend((p, it) for it in items if not it.oculta and it.notas)
    duenos.append((None, None))  # bloque «CIERRE» generado, sin ítem
    return duenos


# ---------------------------------------------------------------------------
# Escritura: esquemas y nota de sección
# ---------------------------------------------------------------------------

BLOQUE_ESQUEMA = re.compile(r"^## (.+?)\n(.*?)(?=^## |^# |\Z)", re.M | re.S)
EDITADA = re.compile(r"#### Versión editada\n\n")


def volcar_esquema(ruta: Path, slides: list[tuple[Item, str]], dry: bool) -> int:
    """Sustituye la «Versión editada» de cada slide del esquema; devuelve nº de cambios."""
    s = ruta.read_text(encoding="utf-8")
    notas = []  # (título, inicio del cuerpo editado, fin del bloque)
    for m in BLOQUE_ESQUEMA.finditer(s):
        e = EDITADA.search(m.group(2))
        if e:
            notas.append((m.group(1).strip(), m.start(2) + e.end(), m.end(2)))
    if len(notas) != len(slides):
        raise SystemExit(
            f"{ruta.name}: {len(notas)} bloques con «Versión editada» y "
            f"{len(slides)} slides visibles con nota"
        )
    for (titulo, _a, _b), (item, _texto) in zip(notas, slides):
        if titulo != item.titulo:
            raise SystemExit(
                f"{ruta.name}: títulos no coinciden: esquema «{titulo}» vs deck «{item.titulo}»"
            )
    cambios = 0
    for (titulo, a, b), (item, texto) in reversed(list(zip(notas, slides))):
        viejo = s[a:b]
        cola = viejo[len(viejo.rstrip()):] or "\n\n"
        if viejo.rstrip() != texto:
            cambios += 1
        s = s[:a] + texto + cola + s[b:]
    if not dry:
        ruta.write_text(s, encoding="utf-8")
    return cambios


def sustituir_nota_seccion(ruta: Path, titulo: str, texto: str, dry: bool) -> None:
    """Reemplaza el ``::: {.notes}`` de la sección ``#`` con ese título en el deck fuente."""
    lineas = ruta.read_text(encoding="utf-8").splitlines(keepends=True)
    en_codigo = False
    cabecera = None
    for i, linea in enumerate(lineas):
        if linea.startswith("```"):
            en_codigo = not en_codigo
            continue
        if en_codigo:
            continue
        m = HEADING.match(linea)
        if m and len(m.group(1)) == 1 and limpiar_titulo(m.group(2)) == titulo:
            if cabecera is not None:
                raise SystemExit(f"{ruta.name}: sección «{titulo}» duplicada")
            cabecera = i
    if cabecera is None:
        raise SystemExit(f"{ruta.name}: no encuentro la sección «{titulo}»")

    a = b = None
    profundidad = 0
    for i in range(cabecera + 1, len(lineas)):
        st = lineas[i].strip()
        if a is None and HEADING.match(lineas[i]):
            raise SystemExit(f"{ruta.name}: la sección «{titulo}» no tiene bloque de notas")
        if a is None:
            if re.match(r"^:{3,}\s*\{[^}]*\.notes", st):
                a = i
                profundidad = 1
            continue
        if re.match(r"^:{3,}\s*(\{|[A-Za-z.#])", st):
            profundidad += 1
        elif re.match(r"^:{3,}\s*$", st):
            profundidad -= 1
            if profundidad == 0:
                b = i
                break
    if a is None or b is None:
        raise SystemExit(f"{ruta.name}: bloque de notas de «{titulo}» sin cerrar")
    lineas[a:b + 1] = ["::: {.notes}\n" + texto + "\n:::\n"]
    if not dry:
        ruta.write_text("".join(lineas), encoding="utf-8")


# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--deck", default=".", help="carpeta del deck unificado")
    parser.add_argument("--guion", default="guion_lectura.qmd", help="guion editado, relativo a --deck")
    parser.add_argument("--dry-run", action="store_true", help="no escribe: solo informa")
    args = parser.parse_args()

    base = Path(args.deck)
    partes_items = [recorrer(base / fichero) for _t, _m, fichero in PARTES]

    esperados = bloques_guion(redactar(partes_items))
    editados = bloques_guion((base / args.guion).read_text(encoding="utf-8"))
    if len(esperados) != len(editados):
        raise SystemExit(
            f"el guion editado tiene {len(editados)} bloques y el regenerado {len(esperados)}: "
            "alguna marca \\guionmarca se ha añadido o borrado a mano"
        )
    for k, (e, g) in enumerate(zip(esperados, editados)):
        if e.marca != g.marca:
            raise SystemExit(f"marca nº {k + 1} alterada en el guion editado:\n  {g.marca[:100]}…")

    duenos = duenos_de_bloques(partes_items)
    assert len(duenos) == len(esperados), "desajuste interno bloques/ítems"
    for (p, item), e in zip(duenos, esperados):
        if item is not None and e.texto != "\n\n".join(item.notas).strip():
            raise SystemExit(f"parser inconsistente en «{item.titulo}» (aviso al desarrollador)")

    # Cambios por bloque; fuera de las Partes 1 y 2 no se tolera ninguno.
    por_parte: dict[int, list[tuple[Item, str, bool]]] = {0: [], 1: []}
    for (p, item), e, g in zip(duenos, esperados, editados):
        cambiado = g.texto != e.texto
        if p in por_parte:
            por_parte[p].append((item, g.texto, cambiado))
        elif cambiado:
            donde = "Parte 3" if item is not None else "bloque de cierre"
            raise SystemExit(f"hay ediciones en el {donde}, fuera del alcance de este volcado")

    for p, ternas in por_parte.items():
        rotulo = PARTES[p][0]
        print(f"{rotulo}")
        for item, texto, cambiado in ternas:
            antes = sum(len(n.split()) for n in item.notas)
            marca = "≠guion" if cambiado else "  =  "
            print(f"  [{marca}] {item.tipo:7s} {item.titulo[:52]:52s} {antes:4d} → {len(texto.split()):4d} palabras")

        slides = [(it, tx) for it, tx, _c in ternas if it.tipo == "slide"]
        cambios = volcar_esquema(base / ESQUEMAS[p], slides, args.dry_run)
        print(f"  esquema {ESQUEMAS[p].name}: {len(slides)} «Versión editada» volcadas, {cambios} cambian")

        for item, texto, cambiado in ternas:
            if item.tipo == "seccion" and cambiado:
                sustituir_nota_seccion(base / DECKS_FUENTE[p], item.titulo, texto, args.dry_run)
                print(f"  nota de sección «{item.titulo}» sustituida en {DECKS_FUENTE[p].name}")

    if args.dry_run:
        print("(dry-run: no se escribe)")
    else:
        print("hecho; siguiente paso: inyectar_notas.py sobre ambos decks (ver AGENTS.md)")


if __name__ == "__main__":
    main()
