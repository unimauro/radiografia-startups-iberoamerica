# Radiografía de las Startups en Iberoamérica

Observatorio de datos, hermano de [Radiografía de las Startups en Perú](https://github.com/unimauro/radiografia-startups-peru),
sobre el ecosistema de startups de **10 países**: Perú, Chile, Colombia, México, Argentina, Uruguay, Ecuador, Brasil, España y Portugal.

> **¿Dónde está el dinero para emprender en Iberoamérica… y dónde no?**

> Estado: **v0.2.1 (21-nov-2026)** · Publicado en **https://unimauro.github.io/radiografia-startups-iberoamerica/** · Edición Perú: https://unimauro.github.io/radiografia-startups-peru/
> Antes se llamaba `radiografia-startups-chile-colombia`; la v0.1 (Chile–Colombia) se conserva en `chile-colombia.html`.

## Qué hay
- `index.html` — dashboard autocontenido, mobile-first (sin scroll horizontal a 360 px), modo claro/oscuro, sidebar,
  fuente bajo cada gráfico. Chart.js 4.4.1 (cdnjs) + mapa con d3 7.9.0, topojson-client 3.1.0 y world-atlas 2.0.2 (jsdelivr).
  Secciones:
  1. Hero con KPIs (contador animado; respeta `prefers-reduced-motion`).
  2. Mapa coroplético del VC 2025 (con recuadro de la península ibérica; si el CDN no carga, cae a una grilla de mosaicos).
  3. Ranking con selector: US$ millones / US$ por habitante / % del PIB.
  4. Evolución 2018–2025 con chips por país, escala lineal/log y total LatAm (LAVCA).
  5. "El dinero es deuda": % de deuda por país, con la diferencia metodológica de cada fuente.
  6. ¿Quién abrió convocatoria en 2026? Matriz país × programa (sí / no / sin dato).
  7. Fichas por país (serie, sectores, rondas, unicornios, StartupBlink, programas, hallazgos, sin verificar).
  8. Perú en el espejo: cuántas veces más VC por habitante o % del PIB (con opción "Perú solo equity").
  9. Metodología y límites (fuentes por país, tipo de cambio BCE, todos los `sin_verificar`), FAQ,
     bibliografía generada desde los JSON y descargas.
- `chile-colombia.html` — edición anterior (v0.1) con el detalle de Start-Up Chile, Corfo, iNNpulsa y Bancóldex.
- `data/paises/{pe,cl,co,mx,ar,uy,ec,br,es,pt}.json` — un JSON por país con esquema común (ver `data/README.md`).
- `data/latam_agregado.json` — total LatAm LAVCA 2018–2025, venture debt y % por país.
- `data/iberoamerica_vc_anual.csv`, `data/iberoamerica_programas.csv` — CSV planos (generados).
- `data/notas_latam.md`, `data/notas_br_es_pt.md` — notas de investigación y conflictos entre fuentes.
- `DATA_SOURCES.md` — fuentes y metodologías. `BACKLOG.md` — backlog vivo (hecho / pendiente / sin verificar).

## Cifras titulares (VC 2025, verificadas al 17-nov-2026)
| País | US$ M | Fuente | US$/hab | % PIB | StartupBlink 2025 |
|---|---:|---|---:|---:|---:|
| España | 3.582 (3.170 M€) | El Referente* | 73,4 | 0,208% | 14 |
| Brasil | 1.670 | LAVCA | 7,9 | 0,076% | 27 |
| México | 1.427 | LAVCA | 10,9 | 0,078% | 43 |
| Colombia | 552 | LAVCA | 10,4 | 0,131% | 36 |
| Portugal | 535 (473 M€) | Dealroom* | 50,0 | 0,170% | 29 |
| Chile | 250 | LAVCA | 12,7 | 0,076% | 37 |
| Argentina | 216 | LAVCA | 4,7 | 0,034% | 46 |
| Perú | 76,5 (72% deuda) | PECAP* | 2,2 | 0,026% | 67 |
| Uruguay | 51 | LAVCA | 15,0 | 0,062% | 61 |
| Ecuador | sin dato | — | — | — | sin dato |

\* Metodología distinta de LAVCA: no comparable 1 a 1.

## Uso
Abrir `index.html` en el navegador: funciona con `file://` porque los JSON van incrustados. Servido por HTTP, la página
vuelve a leer `data/paises/*.json` con `fetch()`. Tras editar cualquier JSON:
```bash
python3 -m venv ~/.venvs/startups-cl-co                     # venv FUERA del repo (solo stdlib)
~/.venvs/startups-cl-co/bin/python scripts/build_inline.py  # reincrusta los JSON y regenera los CSV
~/.venvs/startups-cl-co/bin/python scripts/check_links.py   # valida todas las URL → data/link_status.json
```

## Principios
- Ninguna cifra sin URL. Si no se encontró: **"sin dato"** y entrada en `sin_verificar` / `BACKLOG.md`.
- Series de distintas metodologías **no se mezclan**; las alternativas van en `vc_anual_alternativas`.
- Euros → dólares con el tipo medio anual del BCE (cálculo propio, marcado como tal).
- Investigación asistida por IA, revisada contra las fuentes enlazadas.

Autor: **Carlos Mauro Cárdenas** · Más dashboards en [unimauro.github.io](https://unimauro.github.io)
