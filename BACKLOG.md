# BACKLOG — Radiografía de las Startups en Chile y Colombia

Backlog vivo. Última actualización: **16-nov-2026**.

## ✅ Hecho (v0.1 · 16-nov-2026)
- Repo creado con la estructura del observatorio Perú (`index.html`, `data/`, `scripts/`, `DATA_SOURCES.md`, `README.md`).
- Dashboard con pestañas Chile / Colombia / Comparativo + Perú; Chart.js 4.4.1 (cdnjs); claro/oscuro; sidebar; FAQ;
  bibliografía; crédito y footer Yape.
- Datos con URL por cifra: VC Chile (LAVCA, ACVC, otras), Start-Up Chile (programas, BIG3–BIG13, peruanas),
  Corfo (Semilla Inicia/Expande, líneas de fondos), VC Colombia (LAVCA, KPMG, Cuantico), iNNpulsa (ALDEA, crisis 2025,
  fusión, 2026), Bancóldex (fondo de fondos), comparativo (Banco Mundial, PECAP, StartupBlink).
- `scripts/check_links.py`: 91/91 URLs responden (16-nov-2026). `scripts/build_csv.py`: CSV planos.
- Verificado sin scroll horizontal a 360 px en las tres pestañas (Chrome headless, iframe de 360 px).

## 🔜 Pendiente
- [ ] Decidir si se publica (GitHub Pages) — **decisión del autor**; hoy repo privado y sin Pages.
- [ ] Imagen OG (`og-image.png`) y metadatos `og:url` cuando haya URL pública.
- [ ] Actualizar con **BIG13** (resultados ~ene/feb-2027) y el ACVC Impact Report 2026 (primario).
- [ ] Parsear las listas oficiales de Start-Up Chile por generación (país de sede, sector) en un script reproducible
      (hoy el conteo de peruanas y % chilenas se hizo a mano sobre las listas).
- [ ] Serie ALDEA/CEmprende completa desde datos abiertos de iNNpulsa o derechos de petición.
- [ ] Agregar series LAVCA 2020 para Chile (está en Trends in Tech 2025/2021, no extraída).
- [ ] **Avisar en el repo Perú** (no se modificó aquí): `data/vc_inversion_anual.json` rotula US$76,5M / 23 deals como
      **2023**, pero el comunicado COFIDE–PECAP (jun-2026) lo presenta como el año siguiente a 2024 (33 → 23 deals, −30%;
      47 → 76,5, +64%), o sea **2025**. Revisar el valor real de 2023 en Perú.

## ❓ Datos que NO se pudieron verificar ("sin dato")
### Chile
- ACVC 2018 y 2019; ACVC 2022 propio (solo H1 2022 = US$550M); LAVCA Chile 2020.
- ACVC 2025 (US$854M / 274): solo fuente secundaria; documento primario no encontrado.
- Diferencia de metodología entre las dos cifras ACVC 2024 (US$311M vs US$514,7M).
- Start-Up Chile: tamaño y fecha de BIG1, BIG2 y BIG6; página oficial de BIG11 y su conteo por país;
  total histórico de fundadores peruanos; número actual oficial de países (último dato: 85 países, 2018);
  fechas exactas de apertura/cierre de las convocatorias 2025; línea presupuestaria de Start-Up Chile en la Ley de
  Presupuestos 2026; presupuesto Corfo 2027 (−9%) solo vía prensa secundaria.
- Conteo de peruanas en BIG12: lista oficial = 6; prensa dice 3 o 5. La página dice 59 seleccionadas pero lista 64 (The Clinic: 65).
- Semilla Inicia/Expande: seleccionados y montos por año 2020–2025.
- Montos actuales comprometidos por línea FT/FC/FET.
- Rondas sin fuente primaria: Xepelin, Fintual, Fintoc, Toku (Serie A 2025), ComunidadFeliz.
### Colombia
- ALDEA 2018, 2019, 2021, 2022, 2025 y 2026; no se encontró convocatoria ALDEA 2025.
- CEmprende: número de centros/nodos, convocatorias, beneficiarios.
- "Capital Semilla iNNpulsa", "Más Allá del Capital", "Crece Mujer": sin fuente con cifras.
- Línea presupuestaria específica de iNNpulsa en el PGN 2025 y 2026 (los recortes de COP 12 + 4,2 billones son del PGN completo).
- Presupuesto 2021→2024 solo por columna de opinión (no oficial).
- Serie anual de ColCapital sobre VC en startups.
- Si LAVCA contó la Serie F de Rappi 2020 como colombiana; inconsistencia LAVCA 2018 (rondas de Rappi > total país).
- Rondas de Habi, La Haus, Frubana, Bold 2021–22 en fuente primaria.
- Aportes efectivos de SoftBank y CAF al Fondo de Fondos; el "US$100M" que circula no está respaldado.
### Comparativo
- StartupBlink: Perú 2025 = 67 (Bloomberg Línea) vs 60 (Revista Mercado); Perú 2024 sin dato; startupblink.com bloquea bots.
- Ciudades StartupBlink vía agregador (superscout.co), no la fuente original (salvo Santiago, confirmado por Portal Innova).
- Año del dato PECAP US$76,5M inferido por aritmética (el comunicado no dice el año explícitamente).
- LAVCA no publica Perú por separado → Perú se compara con PECAP (metodología distinta; 72% deuda en 2025).
