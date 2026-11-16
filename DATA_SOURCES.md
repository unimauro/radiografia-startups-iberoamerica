# Fuentes de datos — Radiografía de las Startups en Chile y Colombia

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
