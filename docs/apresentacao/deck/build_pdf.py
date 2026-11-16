"""Gera os PDFs dos slides a partir dos arquivos desta pasta (mesmo conteúdo do deck no Claude).
Uso (na raiz do repositório): python3 docs/apresentacao/deck/build_pdf.py"""
import json, re, subprocess, pathlib
DECK = pathlib.Path(__file__).resolve().parent
ROOT = DECK.parents[2]; IMG = DECK / "img"; OUT = ROOT / "docs/entregas"; FONTS = DECK / "fonts"
BLOBS = {"8e965e7bb1c32ee072afa0f81a0bf924": "logo-panel", "6e9bd68fc5ccff93b0c5d92246bebebf": "agregado-requisicao", "36d28693c75b2e9a3dbc06bee22a15a2": "alto",
         "90573943fb63d5a376784a9cfa3bcbf4": "baixo", "b3ae574bc278d2f8448f22775a565e04": "comunicacao",
         "6c3e3cdd4f4bead624198df7129ccb36": "mapa-de-contextos", "4c1f1329ff0784e1d12f72cde1641cd2": "moderado",
         "fa6c7ddbbee185c67d7ac88991c5bbdd": "regra-de-dependencia", "41fbc7f64901d6dfd6fbdd01a5261e46": "saga-atender-requisicao"}
FINAL = json.loads((DECK / "deck.json").read_text(encoding="utf-8"))["order"]
PRE = ["pre-capa", "pre-quem-fala", "subdominios", "glossario", "mapa", "camadas", "c-pacotes", "perguntas"]
css = (DECK / "deck.css").read_text(encoding="utf-8")
FACES = "".join(f"@font-face{{font-family:'{fam}';src:url('{(FONTS / arq).as_uri()}') format('woff2');font-weight:{peso};{faixa}}}"
                for fam, arq, peso, faixa in [("Noto Sans", "noto-sans-latin-wght-normal.woff2", "100 900", ""),
                                              ("Noto Sans", "noto-sans-latin-ext-wght-normal.woff2", "100 900", "unicode-range:U+0100-024F,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF;"),
                                              ("JetBrains Mono", "jetbrains-mono-latin-400-normal.woff2", "400", ""),
                                              ("JetBrains Mono", "jetbrains-mono-latin-500-normal.woff2", "500", "")])

def montar(ordem, extra=""):
    corpo = ""
    for sid in ordem:
        h = (DECK / "slides" / f"{sid}.html").read_text(encoding="utf-8")
        h = re.sub(r"<aside>.*?</aside>", "", h, flags=re.S)
        for k, v in BLOBS.items():
            h = h.replace("/_blob/" + k, (IMG / f"{v}.png").as_uri())
        corpo += h
    return ("<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>"
            + FACES + "@page{size:1920px 1080px;margin:0} body{margin:0} section{width:1920px;height:1080px;box-sizing:border-box;overflow:hidden;break-after:page;position:relative}"
            + css + " *{animation:none!important}" + extra + "</style></head><body>" + corpo + "</body></html>")

for nome, ordem, extra in [("Hemotrack-Rota-Vital-Parte-2-Slides", FINAL, ""),
                           ("Hemotrack-Pre-entrega-Secoes-A-e-C-Slides", PRE, "")]:
    h = DECK / f"_{nome}.html"; h.write_text(montar(ordem, extra), encoding="utf-8")
    subprocess.run(["node", str(ROOT / "docs/entregas/fonte/print.js"), str(h), str(OUT / f"{nome}.pdf"), "slides"], check=True)
    h.unlink()
