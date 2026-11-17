#!/usr/bin/env python3
"""Incrusta los JSON de data/ en index.html (para que funcione abriendo el archivo con file://)
y genera CSV planos para descarga.

Uso (venv fuera del repo, solo stdlib):
    ~/.venvs/startups-cl-co/bin/python scripts/build_inline.py

- Lee data/paises/{pe,cl,co,mx,ar,uy,ec,br,es,pt}.json y data/latam_agregado.json.
- Reemplaza el contenido de <script id="datos-inline" type="application/json">…</script> en index.html.
- Escribe data/iberoamerica_vc_anual.csv y data/iberoamerica_programas.csv.
En http(s) la página vuelve a leer los JSON con fetch(); la copia incrustada es el respaldo.
"""
import csv
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "data"
ORDEN = ["pe", "cl", "co", "mx", "ar", "uy", "ec", "br", "es", "pt"]


def cargar():
    paises = {iso: json.loads((D / "paises" / f"{iso}.json").read_text(encoding="utf-8")) for iso in ORDEN}
    latam = json.loads((D / "latam_agregado.json").read_text(encoding="utf-8"))
    return {"paises": paises, "latam": latam}


def incrustar(datos):
    html_path = ROOT / "index.html"
    html = html_path.read_text(encoding="utf-8")
    payload = json.dumps(datos, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    pat = re.compile(r'(<script id="datos-inline" type="application/json">)(.*?)(</script>)', re.S)
    if not pat.search(html):
        raise SystemExit("No se encontró <script id=\"datos-inline\"> en index.html")
    html = pat.sub(lambda m: m.group(1) + payload + m.group(3), html, count=1)
    html_path.write_text(html, encoding="utf-8")
    return len(payload)


def csvs(datos):
    with open(D / "iberoamerica_vc_anual.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["iso", "pais", "anio", "usd_m", "eur_m", "operaciones", "metodo", "fuente", "nota"])
        for iso in ORDEN:
            p = datos["paises"][iso]
            for r in p["vc_anual"]:
                w.writerow([iso, p["pais"], r["anio"], r.get("usd_m"), r.get("eur_m"), r.get("operaciones"),
                            r.get("metodo"), r.get("fuente"), r.get("nota", "")])
        for r in datos["latam"]["anual"]:
            w.writerow(["latam", "América Latina (total)", r["anio"], round(r["usd_bn"] * 1000, 1), "",
                        r.get("operaciones"), r.get("metodo"), r.get("fuente"), ""])
    with open(D / "iberoamerica_programas.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["iso", "pais", "programa", "organismo", "tipo", "monto", "convocatoria_2025",
                    "convocatoria_2026", "beneficiarios_ultimo_dato", "fuente", "nota"])
        for iso in ORDEN:
            p = datos["paises"][iso]
            for g in p["programas_publicos"]:
                w.writerow([iso, p["pais"], g["nombre"], g.get("organismo"), g.get("tipo"), g.get("monto"),
                            g.get("convocatoria_2025"), g.get("convocatoria_2026"),
                            g.get("beneficiarios_ultimo_dato"), g.get("fuente"), g.get("nota", "")])


if __name__ == "__main__":
    datos = cargar()
    n = incrustar(datos)
    csvs(datos)
    print(f"index.html: {n:,} bytes de datos incrustados · CSV en data/iberoamerica_*.csv")
