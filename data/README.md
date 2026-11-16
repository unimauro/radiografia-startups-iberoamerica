# Datasets — Radiografía de las Startups en Chile y Colombia

Cifras recopiladas de fuentes públicas (verificadas al 16-nov-2026). Cada registro trae su `url`.
Las cifras de inversión varían según la fuente y la metodología; **no se mezclan series**.

## Archivos
| Archivo | Contenido | Fuentes principales |
|---|---|---|
| `chile_vc_anual.json` / `.csv` | VC en Chile 2018–2025: series LAVCA, ACVC y otras (separadas), sectores 2024, rondas | LAVCA, ACVC (vía InvestChile/DF), entorno.vc |
| `chile_startup_chile.json` | Start-Up Chile: programas Build/Ignite/Growth, generaciones BIG3–BIG13, peruanas por generación, convocatorias 2025–2026 | startupchile.org, Emol, T13, Diario Oficial |
| `chile_startup_chile_generaciones.csv` | Tabla plana de generaciones | idem |
| `chile_corfo_fondos.json` | Corfo: líneas de fondos de VC (F1–FET), Semilla Inicia y Expande | Endeavor Chile, DF, Emol, 24horas |
| `colombia_vc_anual.json` / `.csv` | VC en Colombia 2018–2025: LAVCA, KPMG, Cuantico; rondas; concentración (efecto Rappi) | LAVCA, Bloomberg Línea, La República |
| `colombia_innpulsa.json` | iNNpulsa: ALDEA y otros programas, presupuesto, crisis 2025, fusión, convocatorias 2026 | MinCIT, Bloomberg Línea, El Tiempo, Fiducoldex |
| `colombia_bancoldex_fdf.json` | Bancóldex: fondo de fondos, compartimentos 2024, hitos | Bancóldex, MinCIT, Forbes, Portafolio |
| `comparativo.json` / `.csv` | Población y PIB 2024, VC 2024–2025, VC/hab y VC/PIB, grants por año, StartupBlink 2025 | Banco Mundial, LAVCA, PECAP/COFIDE, Bloomberg Línea |
| `link_status.json` | Código HTTP de cada URL citada (generado por `scripts/check_links.py`) | — |

## Convenciones
- `usd_m`: millones de US$. `cop_m`: millones de pesos colombianos. `monto_clp_m`: millones de pesos chilenos.
- `null` = **sin dato** (buscado y no encontrado de forma verificable).
- Campos `nota` explican conflictos entre fuentes. Los ratios marcados "cálculo propio" se derivan de datos citados.
