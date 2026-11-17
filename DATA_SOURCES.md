# Fuentes de datos — Radiografía de las Startups en Iberoamérica

Todas las URLs de `data/**/*.json`, las notas, `DATA_SOURCES.md`, `index.html` y `chile-colombia.html` se validaron con
`curl -L` (UA de navegador) el **17-nov-2026**: **176 de 176 respondieron 2xx/3xx** (`data/link_status.json`,
regenerable con `scripts/check_links.py`). La bibliografía del dashboard se genera sola a partir de las URL de los JSON.

## 1. Venture capital por país (`vc_anual`)
| País | Serie | URL principal | Comparable con LAVCA |
|---|---|---|---|
| Brasil, México, Colombia, Chile, Argentina | **LAVCA** Tech Report 2019 (2018), VC Tech Report 2020 (2019), Trends in Tech 2025 (2020), Trends in Tech 2026 (2021–2025) | https://www.lavca.org/wp-content/uploads/2026/02/LAVCA_Trends-in-Tech-2026.pdf | Sí |
| Uruguay | LAVCA 2026 (2025, treemap por país); 2023 vía El Observador (fuente original no explícita) | ídem | Solo 2025 |
| Perú | **PECAP** (2018 Infomercado; 2019–2021 Forbes; 2022 Forbes; 2023 El Comercio; 2024 EcoStartup; 2025 COFIDE) | https://www.cofide.com.pe/wp-content/uploads/2026/06/NP-COFIDE-y-PECAP-presentan-informe.pdf | No (incluye 72% de deuda en 2025) |
| Ecuador | ECUACAP vía Ekos (2021–2022) | https://ekosnegocios.com/articulo/ecuacap-lanza-el-primer-reporte-de-venture-capital-en-ecuador | No; 2025 sin dato |
| España | **El Referente** (Observatorio de Startups), M€ → US$ con BCE | https://elreferente.es/actualidad/espana-cierra-2025-con-3-170-millones-de-euros-de-inversion-en-startups-y-un-crecimiento-sostenido/ | No (2025 incluye 312 M€ de deuda) |
| Portugal | **Dealroom** vía Startup Portugal (2024–2025) | https://ecoreport.startupportugal.com/ | No |

- Total LatAm 2018–2025, venture debt y % por país: `data/latam_agregado.json` (LAVCA 2026, p. 2–3 y 9).
- **Perú 2023 (≈US$50M, PECAP):** El Comercio — https://elcomercio.pe/economia/dia-1/inversion-en-startups-como-le-fue-a-latinoamerica-y-peru-en-el-ultimo-ano-empresas-estrategia-negocios-venture-capital-noticia/ (añadida el 17-nov-2026; HTTP 200).
- Tipo de cambio: BCE, serie EXR.A.USD.EUR.SP00.A — https://data-api.ecb.europa.eu/service/data/EXR/A.USD.EUR.SP00.A?format=csvdata&startPeriod=2018&endPeriod=2025
- Población y PIB 2024: API del Banco Mundial (SP.POP.TOTL, NY.GDP.MKTP.CD), URL en `fuente_macro` de cada JSON.

## 2. Deuda vs. equity (`deuda_vs_equity`)
| País | % deuda | Fuente | Qué cuenta |
|---|---:|---|---|
| Perú 2025 | 72 | COFIDE–PECAP | venture debt dentro del total PECAP |
| Brasil 2025 | 56,5 | Sling Hub vía startups.com.br | (FIDC + deuda) / US$4.500M; base distinta de LAVCA |
| Colombia 2025 | 55,5 | KPMG ColombiaTech vía Bloomberg Línea | venture debt / US$857M; no comparable con LAVCA |
| España 2025 | 9,8 | El Referente | 312 / 3.170 M€ (cálculo propio) |
| LatAm 2025 | 14,0 | LAVCA 2026, p. 3 | solo venture debt de fondos cerrados; excluye >US$2.000M de crédito y FIDC |

## 3. Unicornios, StartupBlink y programas
- **Unicornios:** multiples.vc (oct-2026, por sede) para MX, CL, AR, CO, PE; Distrito (BR); Dealroom (ES, PT); Uruguay XXI (UY); Ekos (EC).
- **StartupBlink 2025:** Bloomberg Línea Brasil (CO, CL, AR, UY, PE, BR), El CEO (MX), PDF original para ES y PT; startupblink.com bloquea bots.
- **Programas públicos:** URL por programa en `programas_publicos[].fuente` (y `fuentes_convocatorias` en BR/ES/PT). Detalle en `data/notas_latam.md` y `data/notas_br_es_pt.md`.

## 4. Bloqueos a bots (no se citan)
startupblink.com (web), mexicobusiness.news, PDF del BID sobre Ecuador, emprendedores.es, firjan.com.br, diario.madrid.es, iadb.org, madridinnovation.es, ambitojuridico.com.

## Notas de recolección
- Investigación web asistida por IA, con cada URL comprobada por `curl`. PDF leídos con `pdftotext`; los valores leídos de
  gráficos (treemaps, barras apiladas) se asignaron por posición de etiquetas: revisar el PDF antes de citar un valor aislado.
- Mapa base: world-atlas 2.0.2 (Natural Earth 1:110m) desde jsdelivr.

---

# Anexo — fuentes de la edición Chile–Colombia (v0.1, `chile-colombia.html`)

Todas las URLs citadas en `data/*.json` e `index.html` se validaron con `curl -L` (UA de navegador) el
**16-nov-2026**: **91 de 91 respondieron 2xx/3xx** (ver `data/link_status.json`, regenerable con
`scripts/check_links.py`). Leyenda: ✅ verificada y leída · 🔎 verificada (HTTP 200) pero el dato viene de un
resumen de búsqueda o fuente secundaria · ⚠️ bloquea bots (no citada como fuente directa).

## 1. Chile — venture capital
- ✅ **LAVCA Trends in Tech 2026** (Chile 2021–2025: 889 / 535 / 269 / 184 / 250 US$M) · https://www.lavca.org/wp-content/uploads/2026/02/LAVCA_Trends-in-Tech-2026.pdf
- ✅ **LAVCA Tech Report 2019 / VC Tech Report 2020** (Chile 2018 = 46 / 49 deals; 2019 = 63 / 40) · https://www.lavca.org/wp-content/uploads/2023/10/FINAL2-2019-LAVCA-Tech-Report-04.30.19.pdf · https://www.lavca.org/wp-content/uploads/2023/10/FINAL3-LAVCA-VC-Tech-Report-2020-08.27.20.pdf
- ✅ **ACVC vía InvestChile** (2020 = 160 / 89; 2021 = 2.915 / 104) · https://blog.investchile.gob.cl/venture-capital-investment-chile-2021
- ✅ **ACVC Impact Report 2025 vía DF** (2024 = 311 / 347; −65%) · https://www.df.cl/df-lab/innovacion-y-startups/inversion-en-capital-de-riesgo-en-chile-cayo-un-65-en-2024
- ✅ **Reporte 2024 de Inversiones Chilenas vía DF** (2023 = 898; 2024 = 514,7; sectores) · https://www.df.cl/df-lab/innovacion-y-startups/inversion-chilena-en-startups-registro-fuerte-caida-en-2024
- 🔎 **2025 ACVC (854 / 274)** — solo fuente secundaria · https://ecosistemastartup.com/?p=93392
- ✅ **entorno.vc vía descubre.vc** (2022 = 1.019) · https://www.descubre.vc/noticia/1d66c9b3-672a-4b0e-8e8e-6e7ca5c04b66
- ✅ **Endeavor Chile — Venture Capital 2025** (líneas Corfo F1–FET, Cornershop) · https://endeavor.cl/wp-content/uploads/2025/10/20251002_Endeavor_Venture-Capital-2025_FW_V2.pdf

## 2. Chile — Start-Up Chile y Corfo
- ✅ Programas: https://startupchile.org/postula/build/ · https://startupchile.org/postula/ignite/ · https://startupchile.org/postula/growth/ · https://startupchile.org/en/blog/big-7-big-changes-eng/
- ✅ Generaciones: blogs oficiales BIG3, BIG5, BIG7, BIG8, BIG9, BIG10, BIG12 (URL por fila en `data/chile_startup_chile.json`); BIG4 vía Emol; BIG11 vía El Desconcierto.
- ✅ BIG13 (cierra 24-nov-2026): https://startupchile.org/postula/ · Emol 4-nov-2026 · T13 · bases en Diario Oficial https://www.diariooficial.interior.gob.cl/publicaciones/2026/11/03/44589/01/2893766.pdf
- 🔎 Peruanas en BIG12 y extranjeros 40%: EcoStartup citando a DF (secundaria).
- ✅ Corfo Semilla Inicia / Expande: 24horas, Emol (2024, 2026), La Tercera, T13 (URLs en `data/chile_corfo_fondos.json`).
- ✅ Corfo fondos VC acumulado: DF (15-abr-2025), G5 Noticias. Fondo de Fondos (proyecto de ley): Portal Innova.

## 3. Colombia — venture capital
- ✅ **LAVCA** (2018: Tech Report 2019; 2019: VC Tech Report 2020; 2020: Trends in Tech 2025; 2021–2025: Trends in Tech 2026) · https://www.lavca.org/wp-content/uploads/2025/02/LAVCA_Trends-in-Tech-2025.pdf
- ✅ **KPMG ColombiaTech vía Bloomberg Línea** (incluye venture debt; no comparable) · https://www.bloomberglinea.com/negocios/las-10-startups-en-colombia-que-mas-inversiones-recibieron-en-2025-segun-kpmg/
- ✅ **Cuantico VP + Startuplinks vía La República** (solo equity 2025: CO 224, CL 250, PE 35) · https://www.larepublica.co/globoeconomia/colombia-cuarta-en-financiacion-de-startups-con-us-224-millones-en-inversiones-4349331
- **ColCapital**: no publica serie anual de VC en startups encontrable (su cifra de US$31.500M es todo el capital privado).

## 4. Colombia — iNNpulsa y Bancóldex
- ✅ ALDEA: Semana (acumulado 2020), MinCIT (2023), Vanguardia (2024 + desglose de gasto iNNpulsa).
- ✅ Crisis 2025: Bloomberg Línea (6-jun-2025), El Tiempo (Res. 1627), MinCIT (relanzamiento/fusión), Fiducoldex (informes Q4-2025 y Q1-2026).
- 🔎 Presupuesto 2021 → 2024 (150.000 → 69.000 COP M): columna de opinión en Enter.co, **no oficial**.
- 🔎 Convocatorias 2026: MinCIT (iNNpulsa Mujeres), PDF iNNpulsa Emprendimiento Digital; Forbes (resolución de reactivación).
- ✅ Bancóldex: Reporte anual 2024, comunicado 531 (2010), MinCIT Fondo de Fondos (2019), Forbes (2025), Portafolio (2026).
- ⚠️ ambitojuridico.com (PDFs SENA y comunicado de fusión) responde 403: no se cita.

## 5. Comparativo
- ✅ **Banco Mundial (API)** población y PIB 2024 · https://api.worldbank.org/v2/country/CHL;COL;PER/indicator/SP.POP.TOTL?date=2024&format=json · https://api.worldbank.org/v2/country/CHL;COL;PER/indicator/NY.GDP.MKTP.CD?date=2024&format=json
  (las páginas data.worldbank.org devolvían 500 y el IMF datamapper 403 al momento de la consulta).
- ✅ **PECAP 2025 vía COFIDE** (US$76,5M, 23 deals, 72% deuda) · https://www.cofide.com.pe/wp-content/uploads/2026/06/NP-COFIDE-y-PECAP-presentan-informe.pdf
- 🔎 **PECAP 2024** (US$47M, 33 deals) vía EcoStartup · https://ecosistemastartup.com/?p=82717
- ✅ **StartupBlink 2025** vía Bloomberg Línea Brasil (CO 36, CL 37, PE 67) · conflicto Revista Mercado (PE 60) · ciudades vía superscout.co (agregador) y Portal Innova.
- ⚠️ **startupblink.com** bloquea bots (403): no se pudo verificar en la fuente original.

## Notas de recolección
- Investigación web asistida por IA (4 líneas paralelas: Start-Up Chile, VC Chile + Corfo, iNNpulsa + Bancóldex,
  VC Colombia + comparativo), con cada URL comprobada por `curl`.
- Textos extraídos de PDFs LAVCA con `pdftotext`; los valores de gráficos se asignaron por posición de columna: revisar
  el PDF antes de citar un número de operaciones aislado.
