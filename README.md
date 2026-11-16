# Radiografía de las Startups en Chile y Colombia 🇨🇱 🇨🇴

Observatorio de datos, hermano de [Radiografía de las Startups en Perú](https://github.com/unimauro/radiografia-startups-peru),
sobre el ecosistema de startups de **Chile** y **Colombia**, con **Perú como referencia**:
cuánto venture capital llega de verdad, quién gana los concursos del Estado y qué pasó con los
programas públicos (Start-Up Chile, Corfo, iNNpulsa, Bancóldex) en 2025–2026.

> Estado: **v0.1 (16-nov-2026)** · Repo privado. GitHub Pages **no** habilitado (decisión pendiente del autor).

## Qué hay
- `index.html` — dashboard autocontenido (Chart.js 4.4.1 desde cdnjs, Inter + Space Grotesk, modo claro/oscuro,
  mobile-first). Tres pestañas: **Chile**, **Colombia** y **Comparativo + Perú**. Cada gráfico cita su fuente.
- `data/` — datasets JSON/CSV con la URL de cada cifra (ver `data/README.md`).
- `DATA_SOURCES.md` — fuentes, metodologías y estado de verificación de cada enlace.
- `BACKLOG.md` — backlog vivo: hecho, pendiente y datos que no se pudieron verificar.
- `scripts/` — utilidades en Python (solo stdlib):
  - `check_links.py` — valida con `curl` que cada URL citada resuelva → `data/link_status.json`.
  - `build_csv.py` — genera los CSV desde los JSON.

## Cifras titulares (verificadas al 16-nov-2026)
| | Chile | Colombia | Perú |
|---|---|---|---|
| VC 2025 (US$ M) | 250 (LAVCA) | 552 (LAVCA) | 76,5 (PECAP; 72% deuda) |
| VC 2024 (US$ M) | 184 (LAVCA) | 513 (LAVCA) | 47 (PECAP) |
| VC por habitante 2025 | US$ 12,6 | US$ 10,4 | US$ 2,2 |
| VC / PIB 2025 | 0,076% | 0,131% | 0,026% |
| StartupBlink 2025 | #37 | #36 | #67 |

## Uso local
Abrir `index.html` en el navegador (no requiere servidor). Para scripts:
```bash
python3 -m venv ~/.venvs/startups-cl-co        # venv FUERA del repo
~/.venvs/startups-cl-co/bin/python scripts/build_csv.py
~/.venvs/startups-cl-co/bin/python scripts/check_links.py
```

## Principios
- Ninguna cifra sin URL. Si no se encontró: **"sin dato"** y entrada en `BACKLOG.md`.
- Series de distintas metodologías **no se mezclan** (LAVCA vs ACVC vs KPMG).
- Montos en USD convertidos por el observatorio se marcan como aproximados.
- Investigación asistida por IA, revisada contra las fuentes enlazadas.

Autor: **Carlos Mauro Cárdenas** · Más dashboards en [unimauro.github.io](https://unimauro.github.io)
