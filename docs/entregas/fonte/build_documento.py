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
    deck = ROOT / "docs/apresentacao/deck"
    faces = "".join(f"@font-face{{font-family:'{fam}';src:url('{(deck / 'fonts' / arq).as_uri()}') format('woff2');font-weight:{peso}}}"
                    for fam, arq, peso in [("Noto Sans", "noto-sans-latin-wght-normal.woff2", "100 900"),
                                           ("JetBrains Mono", "jetbrains-mono-latin-400-normal.woff2", "400"),
                                           ("JetBrains Mono", "jetbrains-mono-latin-500-normal.woff2", "500")])
    t = titulo.lstrip("# ").strip()
    logo = (deck / "img/logo-panel.png").as_uri()
    banner = (f'<div class="banner"><img src="{logo}" alt="HemoTrack"><div><p class="k">Squad Hemotrack · Infraestrutura de Software</p>'
              f'<h1>{t}</h1><p class="sub">ADS · CESAR School · 2026.2</p>{extra}</div></div>')
    return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Rota Vital — Parte 2</title><base href="file://{ARQ}/"><style>{faces}{css}</style></head><body>{banner}{frag}</body></html>'

alvos = [("Hemotrack-Rota-Vital-Parte-2", corpo, '<p class="parcial">Entrega final · 26/11</p>'),
         ("Hemotrack-Pre-entrega-Secoes-A-e-C", secoes(corpo, ["Identificação", "A.", "C."]), '<p class="parcial">Pré-entrega · versão parcial para devolutiva · 19/11 · seções A e C</p>')]
for nome, c, extra in alvos:
    h = SRC / f"{nome}.html"; h.write_text(html(c, extra), encoding="utf-8")
    subprocess.run(["node", str(SRC / "print.js"), str(h), str(OUT / f"{nome}.pdf"), "a4"], check=True)
    h.unlink()
