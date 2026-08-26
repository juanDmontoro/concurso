#!/usr/bin/env python3
"""Vuelca todos los entornos ``::: {.notes}`` del ejercicio a un único .md de auditoría.

Lee los tres ficheros de parte del deck unificado (``_parte1_cv.qmd``,
``_parte2_docente.qmd``, ``_parte3_investigacion.qmd``, generados por
``sync_partes.py`` desde los decks fuente) y escribe
``presentacion_ejercicio_esquema.md``: una entrada por nota, en el orden de
exposición, con el título de la slide a la que pertenece, si esa slide está en
``.content-hidden`` (reserva: no se proyecta ni aparece en la vista de orador) y
el recuento de palabras.

Solo lectura sobre los ``.qmd``; el único fichero que escribe es el esquema.

Uso (desde ``0_ejercicio/deck``):

    python scripts/extraer_notas.py [--salida presentacion_ejercicio_esquema.md]
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path

PPM = 140  # palabras por minuto: mismo baremo que los esquemas de las Partes 1 y 2

PARTES = [
    ("Parte 1 de 3 · Currículum vitae", "15 min", "_parte1_cv.qmd"),
    ("Parte 2 de 3 · Propuesta docente", "15 min", "_parte2_docente.qmd"),
    ("Parte 3 de 3 · Propuesta investigadora", "20 min", "_parte3_investigacion.qmd"),
]

FUENTES = {
    "_parte1_cv.qmd": "`0_ejercicio/cv/deck/presentacion_cv.qmd`",
    "_parte2_docente.qmd": "`0_ejercicio/propuesta_docente/sol/propuesta_docente.qmd`",
    "_parte3_investigacion.qmd": (
        "`external/jcr_presentation/propuesta_investigacion.qmd` (proyecto hermano `2026_jcr`)"
    ),
}

FENCE_DIV = re.compile(r"^(:{3,})\s*(.*?)\s*$")
FENCE_CODE = re.compile(r"^\s*(`{3,}|~{3,})")
HEADING = re.compile(r"^(#{1,2})\s+(.*?)\s*$")
ATTR_BLOCK = re.compile(r"\{[^{}]*\}\s*$")


@dataclass
class Nota:
    parte: str
    fichero: str
    linea: int
    nivel: int  # nivel del encabezado al que cuelga la nota (1 = sección, 2 = slide)
    slide: str
    oculta: bool
    texto: str
    palabras: int = field(init=False)

    def __post_init__(self) -> None:
        self.palabras = len(self.texto.split())


def limpiar_titulo(bruto: str) -> str:
    """Quita los atributos Pandoc del título (`{.shrink}`, `{background-color=...}`)."""
    titulo = ATTR_BLOCK.sub("", bruto).strip()
    if titulo:
        return titulo
    # Slides sin título (cierres a toda página): se identifican por sus atributos.
    return f"(slide sin título: `{bruto.strip()}`)" if bruto.strip() else "(slide sin título)"


def extraer(ruta: Path, parte: str) -> list[Nota]:
    """Recorre un .qmd y devuelve sus notas en orden de aparición."""
    notas: list[Nota] = []
    pila: list[str] = []  # atributos de los divs ::: abiertos
    en_codigo = False
    slide, nivel = "(antes del primer título)", 0
    dentro_notas = False
    profundidad_notas = 0
    buffer: list[str] = []
    linea_inicio = 0

    for n, linea in enumerate(ruta.read_text(encoding="utf-8").splitlines(), start=1):
        if FENCE_CODE.match(linea):
            # Los bloques de código no abren divs ni encabezados, pero sí pueden
            # aparecer dentro de una nota: se copian tal cual.
            en_codigo = not en_codigo
            if dentro_notas:
                buffer.append(linea)
            continue
        if en_codigo:
            if dentro_notas:
                buffer.append(linea)
            continue

        div = FENCE_DIV.match(linea)
        if div:
            attrs = div.group(2)
            if attrs:  # apertura
                pila.append(attrs)
                if dentro_notas:
                    profundidad_notas += 1
                    buffer.append(linea)
                elif ".notes" in attrs:
                    dentro_notas = True
                    profundidad_notas = 0
                    buffer = []
                    linea_inicio = n
                continue
            # cierre
            if dentro_notas:
                if profundidad_notas == 0:
                    notas.append(
                        Nota(
                            parte=parte,
                            fichero=ruta.name,
                            linea=linea_inicio,
                            nivel=nivel,
                            slide=slide,
                            oculta=any(".content-hidden" in a for a in pila[:-1]),
                            texto="\n".join(buffer).strip(),
                        )
                    )
                    dentro_notas = False
                else:
                    profundidad_notas -= 1
                    buffer.append(linea)
            if pila:
                pila.pop()
            continue

        if dentro_notas:
            buffer.append(linea)
            continue

        cab = HEADING.match(linea)
        if cab:
            nivel = len(cab.group(1))
            slide = limpiar_titulo(cab.group(2))

    return notas


def minutos(palabras: int) -> str:
    return f"{palabras / PPM:.1f}"


def redactar(notas: list[Nota], base: Path) -> str:
    total_pal = sum(x.palabras for x in notas)
    visibles = [x for x in notas if not x.oculta]
    ocultas = [x for x in notas if x.oculta]

    out: list[str] = []
    add = out.append

    add("# Ejercicio completo — todas las notas de orador")
    add("")
    add(
        "Volcado de auditoría de los entornos `::: {.notes}` de las tres partes del "
        "ejercicio, en el orden en que se exponen. Generado por "
        "`scripts/extraer_notas.py` a partir de los ficheros de parte del deck "
        "unificado (`_parte1_cv.qmd`, `_parte2_docente.qmd`, "
        "`_parte3_investigacion.qmd`), que `sync_partes.py` copia de los decks fuente."
    )
    add("")
    add(
        "**Este documento no es una fuente editable.** Sirve para leer y auditar las "
        "notas juntas. Cualquier corrección se hace en la fuente que corresponda y se "
        "vuelve a sincronizar:"
    )
    add("")
    add(
        "- Partes 1 y 2: «Versión editada» del esquema respectivo "
        "(`presentacion_cv_esquema.md`, `propuesta_docente_esquema.md`) → "
        "`python 0_ejercicio/deck/scripts/inyectar_notas.py <esquema> <deck.qmd>` → "
        "renderizar el deck fuente."
    )
    add(
        "- Parte 3: deck fuente del proyecto hermano `2026_jcr` "
        "(`external/jcr_presentation/propuesta_investigacion.qmd`); nunca la copia local."
    )
    add(
        "- Después, en `0_ejercicio/deck`: "
        "`python scripts/sync_partes.py && quarto render presentacion_ejercicio.qmd` "
        "y regenerar este esquema."
    )
    add("")
    add(
        "Las notas marcadas **[reserva]** cuelgan de slides dentro de "
        "`::: {.content-hidden}`: no se proyectan ni llegan a la vista de orador, y "
        "varias son notas de trabajo (con `[Sources]` y cautelas editoriales), no prosa "
        "oral. Se incluyen para que la auditoría vea todo lo que hay en el `.qmd`."
    )
    add("")

    add("## Medición")
    add("")
    add(
        f"{len(notas)} notas en los `.qmd` · {len(visibles)} en slides visibles "
        f"(las que rinde el HTML como `<aside class=\"notes\">`) · {len(ocultas)} en "
        f"slides de reserva."
    )
    add("")
    add(
        f"Solo las visibles: {sum(x.palabras for x in visibles)} palabras ≈ "
        f"{minutos(sum(x.palabras for x in visibles))} min a {PPM} palabras/min "
        f"(el ejercicio dura 50 min: 15 + 15 + 20)."
    )
    add("")
    add("| Parte | Tiempo asignado | Notas visibles | Palabras | ≈ min | Notas de reserva |")
    add("|---|---|---:|---:|---:|---:|")
    for titulo, tiempo, fichero in PARTES:
        v = [x for x in visibles if x.fichero == fichero]
        o = [x for x in ocultas if x.fichero == fichero]
        pal = sum(x.palabras for x in v)
        add(
            f"| {titulo} | {tiempo} | {len(v)} | {pal} | {minutos(pal)} | {len(o)} |"
        )
    add(
        f"| **Total** | **50 min** | **{len(visibles)}** | "
        f"**{sum(x.palabras for x in visibles)}** | "
        f"**{minutos(sum(x.palabras for x in visibles))}** | **{len(ocultas)}** |"
    )
    add("")
    add(f"Palabras incluyendo las notas de reserva: {total_pal}.")
    add("")
    add(
        f"Los minutos son una cota superior mecánica: suponen leer en voz alta el texto "
        f"íntegro de cada nota a {PPM} palabras/min, sin pausas. Las notas de las Partes 1 "
        f"y 2 son guion oral (densidad acordada ≈150–180 palabras por nota); las de la "
        f"Parte 3 vienen del deck fuente de `2026_jcr` y son más extensas, con pasajes de "
        f"apoyo que no están pensados para decirse enteros."
    )
    add("")

    add("## Índice de notas")
    add("")
    add("| # | Parte | Slide | Palabras |")
    add("|---:|---|---|---:|")
    for i, nota in enumerate(notas, start=1):
        marca = " *[reserva]*" if nota.oculta else ""
        parte_corta = nota.parte.split("·")[0].strip()
        slide = nota.slide.replace("|", "\\|")
        add(f"| {i} | {parte_corta} | {slide}{marca} | {nota.palabras} |")
    add("")

    i = 0
    for titulo, tiempo, fichero in PARTES:
        add("---")
        add("")
        add(f"# {titulo}")
        add("")
        add(f"Fuente: {FUENTES[fichero]} · copia sincronizada en `{fichero}`.")
        add("")
        for nota in [x for x in notas if x.fichero == fichero]:
            i += 1
            marca = " · **[reserva: slide en `.content-hidden`]**" if nota.oculta else ""
            add(f"## {i}. {nota.slide}{marca}")
            add("")
            add(
                f"<sub>`{nota.fichero}:{nota.linea}` · encabezado de nivel "
                f"{nota.nivel} · {nota.palabras} palabras</sub>"
            )
            add("")
            add(nota.texto)
            add("")

    return "\n".join(out) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--deck",
        default=".",
        help="carpeta del deck unificado (por defecto, el directorio actual)",
    )
    parser.add_argument(
        "--salida",
        default="presentacion_ejercicio_esquema.md",
        help="fichero .md de salida, relativo a --deck",
    )
    args = parser.parse_args()

    base = Path(args.deck)
    notas: list[Nota] = []
    for titulo, _tiempo, fichero in PARTES:
        ruta = base / fichero
        if not ruta.exists():
            raise SystemExit(f"No encuentro {ruta}: ejecuta el script desde 0_ejercicio/deck.")
        notas.extend(extraer(ruta, titulo))

    salida = base / args.salida
    salida.write_text(redactar(notas, base), encoding="utf-8")

    visibles = sum(1 for x in notas if not x.oculta)
    print(f"{len(notas)} notas ({visibles} visibles, {len(notas) - visibles} de reserva)")
    for _titulo, _tiempo, fichero in PARTES:
        v = [x for x in notas if x.fichero == fichero and not x.oculta]
        print(
            f"  {fichero}: {len(v)} visibles, {sum(x.palabras for x in v)} palabras, "
            f"≈{minutos(sum(x.palabras for x in v))} min"
        )
    print(f"escrito {salida}")


if __name__ == "__main__":
    main()
