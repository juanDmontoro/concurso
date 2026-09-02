#!/usr/bin/env python3
"""Genera el guion de lectura del ejercicio (``guion_lectura.qmd``, render a PDF).

Recorre los tres ficheros de parte del deck unificado (``_parte1_cv.qmd``,
``_parte2_docente.qmd``, ``_parte3_investigacion.qmd``) y produce un documento
de ensayo para leer en papel: la prosa de las notas de orador fluye de
principio a fin (14 pt, doble espacio, sin encabezados), con un margen
izquierdo ancho donde una marca indica en cada momento la slide proyectada y,
cuando toca, el cambio de parte o de sección. Las slides de reserva
(``.content-hidden``) quedan fuera; las slides visibles sin nota aparecen como
marca atenuada «(sin nota)».

A diferencia de ``extraer_notas.py``, el parser ignora los encabezados que
están dentro de divs de contenido (callouts, columnas): solo los encabezados
con la pila de divs limpia son slides o secciones reales, de modo que cada
nota se atribuye a la slide que de verdad se proyecta.

Además de los ficheros de parte, el script lee las notas de orador de los
divisores «Parte N de 3» del maestro (``presentacion_ejercicio.qmd``), como
la entradilla protocolaria de la Parte 1: encabezan su parte en el guion y
sus palabras cuentan en la tabla y en los minutos estimados.

Solo lectura sobre los ``.qmd``; el único fichero que escribe es el guion.

Uso (desde ``0_ejercicio/deck``):

    python scripts/generar_guion.py [--salida guion_lectura.qmd]
    quarto render guion_lectura.qmd
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path

from extraer_notas import ATTR_BLOCK, FENCE_CODE, FENCE_DIV, HEADING, PARTES, PPM, limpiar_titulo, minutos

MAESTRO = "presentacion_ejercicio.qmd"


@dataclass
class Item:
    """Una slide o sección real (encabezado estructural) con sus notas."""

    tipo: str  # "seccion" (# real) | "slide" (## real)
    titulo: str
    oculta: bool
    notas: list[str] = field(default_factory=list)

    @property
    def palabras(self) -> int:
        return sum(len(t.split()) for t in self.notas)


def es_envoltorio(attrs: str) -> bool:
    """Divs que envuelven slides enteras sin formar parte de su contenido."""
    return ".content-hidden" in attrs or "content-visible" in attrs


def recorrer(ruta: Path) -> list[Item]:
    """Devuelve las slides/secciones reales de un .qmd, en orden, con sus notas."""
    items: list[Item] = []
    pila: list[str] = []  # atributos de los divs ::: abiertos
    en_codigo = False
    dentro_notas = False
    profundidad_notas = 0
    nota_oculta = False
    buffer: list[str] = []

    for linea in ruta.read_text(encoding="utf-8").splitlines():
        if FENCE_CODE.match(linea):
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
                if dentro_notas:
                    profundidad_notas += 1
                    buffer.append(linea)
                elif ".notes" in attrs:
                    dentro_notas = True
                    profundidad_notas = 0
                    nota_oculta = any(".content-hidden" in a for a in pila)
                    buffer = []
                pila.append(attrs)
                continue
            # cierre
            if dentro_notas:
                if profundidad_notas == 0:
                    if not nota_oculta and items and not items[-1].oculta:
                        items[-1].notas.append("\n".join(buffer).strip())
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
            # Solo es slide/sección si no hay abierto ningún div de contenido
            # (callout, columnas...): esos encabezados pertenecen a la slide.
            if not all(es_envoltorio(a) for a in pila):
                continue
            # Dentro de contenido solo-beamer no se cuentan encabezados
            # (RevealJS es el formato canónico; evita duplicados).
            if any('when-format="beamer"' in a for a in pila):
                continue
            items.append(
                Item(
                    tipo="seccion" if len(cab.group(1)) == 1 else "slide",
                    titulo=limpiar_titulo(cab.group(2)),
                    oculta=any(".content-hidden" in a for a in pila),
                )
            )

    return items


DIVISOR = re.compile(r"\[Parte (\d+) de 3\]")


def notas_divisores(ruta: Path) -> dict[int, list[str]]:
    """Notas de orador de los divisores «Parte N de 3» del deck maestro.

    El maestro puede añadir notas propias a sus divisores de parte (p. ej.
    la entradilla protocolaria de la Parte 1), que no viven en ningún
    fichero de parte. Devuelve {número de parte: notas}.
    """
    notas: dict[int, list[str]] = {}
    for item in recorrer(ruta):
        m = DIVISOR.search(item.titulo)
        if m and item.notas:
            notas[int(m.group(1))] = item.notas
    return notas


# ---------------------------------------------------------------------------
# Emisión del .qmd
# ---------------------------------------------------------------------------

LATEX_ESPECIALES = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def titulo_tex(titulo: str) -> str:
    """Título de slide como LaTeX: escapa especiales y convierte el énfasis Markdown."""
    s = "".join(LATEX_ESPECIALES.get(c, c) for c in titulo)
    s = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", s)
    s = re.sub(r"\*(.+?)\*", r"\\emph{\1}", s)
    return s


PREAMBULO = r"""
\usepackage{marginnote}
\usepackage{ragged2e}
\usepackage{xcolor}
\usepackage{needspace}
\usepackage{booktabs}
\reversemarginpar
\definecolor{GuionTeal}{HTML}{2D6A7A}
\definecolor{GuionCoral}{HTML}{C44536}
\definecolor{GuionGris}{HTML}{55595C}
\definecolor{GuionGrisClaro}{HTML}{9A9DA0}
% Una sola \marginnote por anclaje; dentro se apilan las marcas con \par.
\newcommand{\guionmarca}[1]{\marginnote{\RaggedRight\sffamily
  \hyphenpenalty=10000 \exhyphenpenalty=10000 #1}[0pt]}
\newcommand{\marcaparte}[3]{%
  {\color{GuionTeal}\scriptsize\bfseries #1\par}%
  {\color{GuionTeal}\normalsize\bfseries #2\par}%
  {\color{GuionCoral}\rule{\linewidth}{1.5pt}\par}%
  {\color{GuionGris}\scriptsize #3\par}}
\newcommand{\marcaseccion}[1]{{\color{GuionTeal}\footnotesize #1\par}}
\newcommand{\marcaslide}[2]{{\color{GuionGris}\footnotesize\textbf{#1}\enspace #2\par}}
\newcommand{\marcasinnota}[2]{{\color{GuionGrisClaro}\footnotesize\itshape #1\enspace #2 (sin nota)\par}}
"""


def cabecera_yaml() -> str:
    preambulo = "\n".join(f"        {l}" for l in PREAMBULO.strip().splitlines())
    return f"""---
title: "Guion de lectura del ejercicio"
subtitle: "Concurso de acceso 78/2026 · Catedrático de Universidad · Universitat de València"
lang: es
format:
  pdf:
    documentclass: scrartcl
    fontsize: 14pt
    linestretch: 2
    classoption: [parskip=half]
    geometry:
      - a4paper
      - left=7.5cm
      - right=2cm
      - top=2.5cm
      - bottom=2.8cm
      - marginparwidth=5.6cm
      - marginparsep=0.6cm
    number-sections: false
    include-in-header:
      text: |
{preambulo}
---
"""


def redactar(partes_items: list[list[Item]], entradillas: list[list[str]]) -> str:
    out: list[str] = []
    add = out.append

    add("<!-- NO EDITAR: generado por scripts/generar_guion.py a partir de los")
    add("     ficheros de parte del deck unificado. Las correcciones de las notas")
    add("     se hacen en sus fuentes y se re-sincroniza (ver AGENTS.md). -->")
    add("")
    add(cabecera_yaml())

    # --- Portadilla: medición y leyenda -----------------------------------
    add(
        "Guion de ensayo para leer en papel: la narrativa de las notas de orador "
        "corre sin interrupciones de principio a fin; el margen izquierdo indica "
        "en cada momento qué slide está proyectada. Documento generado por "
        "`scripts/generar_guion.py` — no editar a mano."
    )
    add("")
    # Tabla compacta en LaTeX crudo: a espacio sencillo y en una sola página
    # (una tabla longtable a doble espacio y 14 pt se partiría entre páginas).
    add("\\begin{center}")
    add("\\begin{singlespace}")
    add("\\footnotesize")
    add("\\begin{tabular}{@{}lrrrrr@{}}")
    add("\\toprule")
    add("Parte & Asignado & Slides & Notas & Palabras & $\\approx$ min\\\\")
    add("\\midrule")
    tot_slides = tot_notas = tot_pal = 0
    for (titulo, tiempo, _fichero), items, entr in zip(PARTES, partes_items, entradillas):
        visibles = [x for x in items if not x.oculta]
        slides = [x for x in visibles if x.tipo == "slide"]
        notas = sum(len(x.notas) for x in visibles) + len(entr)
        pal = sum(x.palabras for x in visibles) + sum(len(t.split()) for t in entr)
        tot_slides += len(slides)
        tot_notas += notas
        tot_pal += pal
        rotulo, nombre = (s.strip() for s in titulo.split("·", 1))
        etiqueta = f"{rotulo.split()[1]} · {titulo_tex(nombre)}"
        add(
            f"{etiqueta} & {tiempo} & {len(slides)} & {notas} & {pal} & "
            f"{minutos(pal).replace('.', ',')}\\\\"
        )
    add("\\midrule")
    add(
        f"\\textbf{{Total}} & \\textbf{{50 min}} & \\textbf{{{tot_slides}}} & "
        f"\\textbf{{{tot_notas}}} & \\textbf{{{tot_pal}}} & "
        f"\\textbf{{{minutos(tot_pal).replace('.', ',')}}}\\\\"
    )
    add("\\bottomrule")
    add("\\end{tabular}")
    add("")
    add(f"\\smallskip \\scriptsize Minutos estimados a {PPM} palabras por minuto.")
    add("\\end{singlespace}")
    add("\\end{center}")
    add("")
    add(
        "Leyenda del margen: **parte** (teal, con filete y tiempos), sección "
        "(teal fino), **n** título de slide (gris) y *n título (sin nota)* en "
        "gris claro para slides proyectadas sin texto que decir."
    )
    add("")
    add("\\clearpage")
    add("")

    # --- Cuerpo: texto continuo con marcas en el margen -------------------
    pendientes: list[str] = []  # marcas LaTeX a la espera de una nota-ancla
    rango = "slide"  # rango más fuerte entre las marcas pendientes
    num = 0

    def volcar(nota: str) -> None:
        """Ancla las marcas pendientes al primer párrafo de `nota` y la emite."""
        nonlocal rango
        if pendientes:
            if rango == "parte":
                add("\\needspace{3\\baselineskip}")
                add("\\vspace{2\\baselineskip}")
            elif rango == "seccion":
                add("\\needspace{2\\baselineskip}")
                add("\\bigskip")
            else:
                add("\\medskip")
            add("")
            marcas = "\\smallskip ".join(pendientes)
            add(f"\\guionmarca{{{marcas}}} {nota}")
            pendientes.clear()
            rango = "slide"
        else:
            add("\\medskip")
            add("")
            add(nota)
        add("")

    for (titulo_parte, tiempo, _fichero), items, entr in zip(PARTES, partes_items, entradillas):
        visibles = [x for x in items if not x.oculta]
        pal = sum(x.palabras for x in visibles) + sum(len(t.split()) for t in entr)
        rotulo, nombre = (s.strip() for s in titulo_parte.split("·", 1))
        pendientes.append(
            f"\\marcaparte{{{rotulo.upper()}}}{{{titulo_tex(nombre)}}}"
            f"{{{tiempo} · $\\approx$\\,{minutos(pal).replace('.', ',')} min a {PPM} ppm}}"
        )
        rango = "parte"
        # Nota del divisor del maestro (entradilla): abre la parte, anclada
        # a la marca de parte, antes de la primera slide.
        if entr:
            volcar(entr[0])
            for extra in entr[1:]:
                add(extra)
                add("")
        for item in visibles:
            if item.tipo == "seccion":
                pendientes.append(f"\\marcaseccion{{{titulo_tex(item.titulo).upper()}}}")
                if rango == "slide":
                    rango = "seccion"
            else:
                num += 1
                if item.notas:
                    pendientes.append(f"\\marcaslide{{{num}}}{{{titulo_tex(item.titulo)}}}")
                else:
                    pendientes.append(f"\\marcasinnota{{{num}}}{{{titulo_tex(item.titulo)}}}")
                    continue
            if item.notas:
                volcar(item.notas[0])
                for extra in item.notas[1:]:
                    add(extra)
                    add("")

    # Cierre del deck unificado (Agradecimientos + portada repetida), fuera
    # de los ficheros de parte; también ancla marcas rezagadas sin nota.
    pendientes.append("\\marcaseccion{CIERRE}")
    if rango == "slide":
        rango = "seccion"
    volcar("*Slide de agradecimientos y portada final.*")

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
        default="guion_lectura.qmd",
        help="fichero .qmd de salida, relativo a --deck",
    )
    args = parser.parse_args()

    base = Path(args.deck)
    partes_items: list[list[Item]] = []
    for _titulo, _tiempo, fichero in PARTES:
        ruta = base / fichero
        if not ruta.exists():
            raise SystemExit(f"No encuentro {ruta}: ejecuta el script desde 0_ejercicio/deck.")
        partes_items.append(recorrer(ruta))

    maestro = base / MAESTRO
    por_parte = notas_divisores(maestro) if maestro.exists() else {}
    if not maestro.exists():
        print(f"aviso: no encuentro {maestro}; guion sin notas de divisores")
    entradillas = [por_parte.get(n, []) for n in range(1, len(PARTES) + 1)]

    salida = base / args.salida
    salida.write_text(redactar(partes_items, entradillas), encoding="utf-8")

    for (titulo, _tiempo, fichero), items, entr in zip(PARTES, partes_items, entradillas):
        visibles = [x for x in items if not x.oculta]
        slides = [x for x in visibles if x.tipo == "slide"]
        sin_nota = [x for x in slides if not x.notas]
        pal = sum(x.palabras for x in visibles) + sum(len(t.split()) for t in entr)
        divisor = f" (+{len(entr)} nota de divisor)" if entr else ""
        print(
            f"  {fichero}: {len(slides)} slides visibles ({len(sin_nota)} sin nota), "
            f"{sum(len(x.notas) for x in visibles)} notas{divisor}, {pal} palabras, "
            f"≈{minutos(pal)} min"
        )
    print(f"escrito {salida}")
    print(f"render: quarto render {args.salida}")


if __name__ == "__main__":
    main()
