#!/usr/bin/env python3
"""Valida que cada URL citada en data/*.json, DATA_SOURCES.md e index.html resuelva.

Uso (venv fuera del repo):
    python3 -m venv ~/.venvs/startups-cl-co
    ~/.venvs/startups-cl-co/bin/python scripts/check_links.py

Usa `curl` (sigue redirecciones, UA de navegador). Escribe data/link_status.json con
{url: {"status": int, "ok": bool, "archivos": [...]}}. Un 403/429 suele ser bloqueo a bots
(la página existe pero no deja verificar automáticamente): se marca "bloquea_bots".
"""
import json
import pathlib
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
URL_RE = re.compile(r"https?://[^\s\"'<>\]`]+")
IGNORAR = ("fonts.googleapis.com", "fonts.gstatic.com", "cdnjs.cloudflare.com",
           "googletagmanager.com", "github.com/unimauro", "unimauro.github.io")


def recolectar():
    urls = {}
    archivos = list((ROOT / "data").glob("*.json")) + [ROOT / "DATA_SOURCES.md", ROOT / "index.html"]
    for f in archivos:
        if not f.exists() or f.name == "link_status.json":
            continue
        for u in URL_RE.findall(f.read_text(encoding="utf-8")):
            u = u.rstrip(".,;:")
            while u.endswith(")") and u.count(")") > u.count("("):
                u = u[:-1]
            if any(i in u for i in IGNORAR):
                continue
            urls.setdefault(u, set()).add(str(f.relative_to(ROOT)))
    return urls


def status(url):
    cmd = ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-L", "--max-time", "25",
           "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36",
           url]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=40).stdout.strip()
        return int(out or 0)
    except Exception:
        return 0


def main():
    urls = recolectar()
    with ThreadPoolExecutor(max_workers=8) as ex:
        res = dict(zip(urls, ex.map(status, urls)))
    out = {}
    for u, s in sorted(res.items()):
        estado = "ok" if 200 <= s < 400 else ("bloquea_bots" if s in (401, 403, 429, 503) else "caido")
        out[u] = {"status": s, "estado": estado, "archivos": sorted(urls[u])}
    (ROOT / "data" / "link_status.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    malos = {u: v for u, v in out.items() if v["estado"] != "ok"}
    print(f"{len(out)} URLs · {len(out) - len(malos)} ok · {len(malos)} con problema")
    for u, v in malos.items():
        print(f"  [{v['status']}] {v['estado']:12} {u}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
