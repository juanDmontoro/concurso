"""Sincroniza el deck unificado del ejercicio con sus dos decks fuente.

Extrae el cuerpo (sin YAML) de presentacion_cv.qmd y propuesta_docente.qmd
a _parte1_cv.qmd y _parte2_docente.qmd, y copia a esta carpeta las figuras
referenciadas, _theme.scss y title-slide.js. Los decks fuente son de solo
lectura: este script solo lee de ellos.

Ejecutar desde 0_ejercicio/deck/:  python scripts/sync_partes.py
"""

import re
import shutil
import sys
from pathlib import Path

DECK = Path(__file__).resolve().parent.parent

FUENTES = [
    (DECK.parent / "cv" / "deck" / "presentacion_cv.qmd", "_parte1_cv.qmd"),
    (DECK.parent / "propuesta_docente" / "sol" / "propuesta_docente.qmd", "_parte2_docente.qmd"),
]

ASSETS_DIR = DECK.parent / "cv" / "deck"  # _theme.scss y title-slide.js (bit-idénticos en ambos decks)

FIG_RE = re.compile(r"\]\((figures/[^)\s]+\.svg)\)")


def extraer_cuerpo(texto: str, origen: Path) -> str:
    partes = texto.split("\n---\n", 2)
    if not texto.startswith("---\n") or len(partes) < 2:
        sys.exit(f"ERROR: no se encuentra el bloque YAML en {origen}")
    cuerpo = partes[1] if len(partes) == 2 else "\n---\n".join(partes[1:])
    # El aviso va al final: un bloque raw justo tras el "# Parte N" del maestro
    # haría que Pandoc creara un frame vacío extra en beamer.
    aviso = (
        f"<!-- Generado por scripts/sync_partes.py desde {origen.name} — NO EDITAR;\n"
        f"     editar el deck fuente y re-sincronizar. -->\n"
    )
    return cuerpo.lstrip("\n").rstrip("\n") + "\n\n" + aviso


def sincronizar_figuras(cuerpo: str, origen_dir: Path) -> tuple[list[str], list[str]]:
    destino = DECK / "figures"
    destino.mkdir(exist_ok=True)
    copiadas, sin_pdf = [], []
    for ref in sorted(set(FIG_RE.findall(cuerpo))):
        svg = origen_dir / ref
        if not svg.exists():
            sys.exit(f"ERROR: figura referenciada inexistente: {svg}")
        shutil.copy2(svg, destino / svg.name)
        copiadas.append(svg.name)
        pdf = svg.with_suffix(".pdf")
        if pdf.exists():
            shutil.copy2(pdf, destino / pdf.name)
        else:
            sin_pdf.append(svg.name)
    return copiadas, sin_pdf


def main() -> None:
    for fuente, salida in FUENTES:
        texto = fuente.read_text(encoding="utf-8")
        cuerpo = extraer_cuerpo(texto, fuente)
        (DECK / salida).write_text(cuerpo, encoding="utf-8")
        copiadas, sin_pdf = sincronizar_figuras(cuerpo, fuente.parent)
        print(f"{salida}: {len(cuerpo.splitlines())} líneas desde {fuente.name}")
        print(f"  figuras copiadas ({len(copiadas)}): {', '.join(copiadas)}")
        if sin_pdf:
            print(f"  sin gemelo PDF (beamer usará rsvg-convert): {', '.join(sin_pdf)}")

    for asset in ("_theme.scss", "title-slide.js"):
        shutil.copy2(ASSETS_DIR / asset, DECK / asset)
        print(f"{asset}: copiado desde {ASSETS_DIR.relative_to(DECK.parent)}")


if __name__ == "__main__":
    main()
