#!/usr/bin/env python3
"""Genera CSV planos a partir de los JSON de data/ (series de VC y comparativo).

Uso: ~/.venvs/startups-cl-co/bin/python scripts/build_csv.py   (solo stdlib)
"""
import csv
import json
import pathlib

D = pathlib.Path(__file__).resolve().parent.parent / "data"


def series_csv(src, dst, pais):
    d = json.loads((D / src).read_text(encoding="utf-8"))
    with open(D / dst, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["pais", "fuente", "anio", "usd_m", "operaciones", "url", "nota"])
        for s in d["series"]:
            for r in s["datos"]:
                w.writerow([pais, s["fuente"], r["anio"], r.get("usd_m"), r.get("operaciones"),
                            r.get("url", ""), r.get("nota", "")])


def startup_chile_csv():
    d = json.loads((D / "chile_startup_chile.json").read_text(encoding="utf-8"))
    cols = ["gen", "anio", "anuncio", "seleccionadas", "postulaciones", "build", "ignite", "growth",
            "pct_chilenos", "peruanas", "url", "nota"]
    with open(D / "chile_startup_chile_generaciones.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for g in d["generaciones"]:
            w.writerow([g.get(c, "") if g.get(c) is not None else "" for c in cols])


def comparativo_csv():
    d = json.loads((D / "comparativo.json").read_text(encoding="utf-8"))
    pp, r = d["poblacion_pib_2024"], d["ratios_calculo_propio"]
    with open(D / "comparativo.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["pais", "anio", "vc_usd_m", "poblacion_2024", "pib_2024_usd", "vc_usd_por_hab", "vc_pct_pib",
                    "startupblink_2025"])
        for anio in ("2024", "2025"):
            for p in ("Chile", "Colombia", "Peru"):
                w.writerow([p, anio, d["vc"][anio][p], pp[p]["poblacion"], pp[p]["pib_usd"],
                            r[anio][p]["usd_por_hab"], r[anio][p]["pct_pib"], d["startupblink_2025"]["paises"][p]])


if __name__ == "__main__":
    series_csv("chile_vc_anual.json", "chile_vc_anual.csv", "Chile")
    series_csv("colombia_vc_anual.json", "colombia_vc_anual.csv", "Colombia")
    startup_chile_csv()
    comparativo_csv()
    print("CSV generados en data/")
