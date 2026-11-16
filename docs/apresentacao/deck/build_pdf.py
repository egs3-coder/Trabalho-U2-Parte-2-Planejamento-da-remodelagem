"""Gera os PDFs dos slides a partir dos arquivos desta pasta (mesmo conteúdo do deck no Claude).
Uso (na raiz do repositório): python3 docs/apresentacao/deck/build_pdf.py"""
import json, re, subprocess, pathlib
DECK = pathlib.Path(__file__).resolve().parent
ROOT = DECK.parents[2]; IMG = ROOT / "docs/arquitetura/img"; OUT = ROOT / "docs/entregas"
BLOBS = {"b1ad863105abe646ec8d02b92de20bd8": "agregado-requisicao", "5fe0b21f4cadbabb55e07a603975670c": "alto",
         "425a1660dbe2e548f4f15b9e67508c4d": "baixo", "5329e8d58edfc2938b723884af495731": "comunicacao",
         "c9b65dcd5f27ea557783832b4511b047": "mapa-de-contextos", "75dcfc64e7eb739b19daa96756873be9": "moderado",
         "869dfe2da5992e03ddf9ed54aea35121": "regra-de-dependencia", "7b9ab33b20b07428509cb60d6cd91e58": "saga-atender-requisicao"}
FINAL = json.loads((DECK / "deck.json").read_text(encoding="utf-8"))["order"]
PRE = ["pre-capa", "pre-quem-fala", "subdominios", "glossario", "mapa", "camadas", "c-pacotes", "perguntas"]
css = (DECK / "deck.css").read_text(encoding="utf-8")

def montar(ordem, extra=""):
    corpo = ""
    for sid in ordem:
        h = (DECK / "slides" / f"{sid}.html").read_text(encoding="utf-8")
        h = re.sub(r"<aside>.*?</aside>", "", h, flags=re.S)
        for k, v in BLOBS.items():
            h = h.replace("/_blob/" + k, (IMG / f"{v}.png").as_uri())
        corpo += h
    return ("<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>"
            "@page{size:1920px 1080px;margin:0} body{margin:0} section{width:1920px;height:1080px;box-sizing:border-box;overflow:hidden;break-after:page}"
            + css + " *{animation:none!important}" + extra + "</style></head><body>" + corpo + "</body></html>")

for nome, ordem, extra in [("Hemotrack-Rota-Vital-Parte-2-Slides", FINAL, ""),
                           ("Hemotrack-Pre-entrega-Secoes-A-e-C-Slides", PRE, "")]:
    h = DECK / f"_{nome}.html"; h.write_text(montar(ordem, extra), encoding="utf-8")
    subprocess.run(["node", str(ROOT / "docs/entregas/fonte/print.js"), str(h), str(OUT / f"{nome}.pdf"), "slides"], check=True)
    h.unlink()
