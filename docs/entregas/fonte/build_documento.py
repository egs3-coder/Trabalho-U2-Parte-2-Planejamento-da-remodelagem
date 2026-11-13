"""Gera os PDFs do documento a partir de docs/arquitetura/documento.md.
Uso (na raiz do repositório): python3 docs/entregas/fonte/build_documento.py"""
import re, subprocess, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
ARQ = ROOT / "docs/arquitetura"; OUT = ROOT / "docs/entregas"; SRC = pathlib.Path(__file__).parent
md = (ARQ / "documento.md").read_text(encoding="utf-8")
md = re.sub(r"^> Versão em PDF.*\n\n", "", md, flags=re.M)
titulo, resto = md.split("\n", 1)
sub, corpo = resto.strip().split("\n", 1)

def secoes(texto, nomes):
    partes = re.split(r"(?m)^(?=## )", texto)
    return "".join(p for p in partes if any(p.startswith("## " + n) for n in nomes))

def html(corpo_md, extra=""):
    frag = subprocess.run(["pandoc", "-f", "gfm", "-t", "html5"], input=corpo_md, capture_output=True, text=True, check=True).stdout
    frag = re.sub(r'<img src="img/(agregado-requisicao|comunicacao)\.png"', r'<img class="alto" src="img/\1.png"', frag)
    frag = frag.replace('<img src="img/saga-atender-requisicao.png"', '<img class="saga" src="img/saga-atender-requisicao.png"')
    css = (SRC / "documento.css").read_text()
    t = titulo.lstrip("# ").strip()
    return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Rota Vital — Parte 2</title><base href="file://{ARQ}/"><style>{css}</style></head><body><h1>{t}</h1><p class="sub">Squad Hemotrack · Infraestrutura de Software · ADS · CESAR School · novembro de 2026</p>{extra}{frag}</body></html>'

alvos = [("Hemotrack-Rota-Vital-Parte-2", corpo, ""),
         ("Hemotrack-Pre-entrega-Secoes-A-e-C", secoes(corpo, ["Identificação", "A.", "C."]), '<p class="parcial">Pré-entrega (versão parcial, 17/11): seções A e C</p>')]
for nome, c, extra in alvos:
    h = SRC / f"{nome}.html"; h.write_text(html(c, extra), encoding="utf-8")
    subprocess.run(["node", str(SRC / "print.js"), str(h), str(OUT / f"{nome}.pdf"), "a4"], check=True)
    h.unlink()
