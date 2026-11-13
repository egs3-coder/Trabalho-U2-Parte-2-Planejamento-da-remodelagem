"""Troca os slides 6, 7, 9, 10 e 11 do PDF da apresentação pelas versões de slides-revisados.html.
Uso (na raiz do repositório): python3 docs/entregas/fonte/build_slides.py"""
import subprocess, pathlib
from pypdf import PdfReader, PdfWriter
SRC = pathlib.Path(__file__).resolve().parent; OUT = SRC.parent / "Hemotrack-Rota-Vital-Parte-2-Slides.pdf"
tmp = SRC / "_revisados.pdf"
subprocess.run(["node", str(SRC / "print.js"), str(SRC / "slides-revisados.html"), str(tmp), "slides"], check=True)
novos = PdfReader(tmp).pages; troca = {6: 0, 7: 1, 9: 2, 10: 3, 11: 4}
orig = PdfReader(OUT); w = PdfWriter()
for i, p in enumerate(orig.pages, start=1):
    w.add_page(novos[troca[i]] if i in troca else p)
data = OUT.with_suffix(".tmp.pdf"); w.write(data); data.replace(OUT); tmp.unlink()
