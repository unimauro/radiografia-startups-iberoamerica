# BACKLOG — Radiografía de las Startups en Iberoamérica

Backlog vivo. Última actualización: **17-nov-2026**.

## ✅ Hecho (v0.2 · 17-nov-2026)
- Repo renombrado de `radiografia-startups-chile-colombia` a `radiografia-startups-iberoamerica` (privado, sin Pages).
- Datos de 10 países con esquema común en `data/paises/*.json` + `data/latam_agregado.json` (LAVCA 2018–2025).
- Perú 2023 (≈US$50M, PECAP) ahora con fuente: El Comercio (HTTP 200); retirado de `sin_verificar`.
- Dashboard nuevo `index.html`: hero con KPIs animados (respeta reduced-motion), mapa coroplético d3 (recuadro ibérico y
  respaldo en mosaicos), ranking absoluto / por habitante / % PIB, evolución 2018–2025 con chips y escala log + total LatAm,
  deuda vs equity con advertencia metodológica, matriz de convocatorias 2025/2026, fichas por país con sparkline,
  "Perú en el espejo" (con opción solo equity), metodología + todos los `sin_verificar`, FAQ, bibliografía automática
  desde los JSON, descargas JSON/CSV.
- Gráficos se recolorean al cambiar tema; paleta por país distinta en claro y oscuro.
- `scripts/build_inline.py`: incrusta los JSON (funciona con `file://`) y genera `data/iberoamerica_*.csv`.
- `scripts/check_links.py`: ahora recorre `data/**` y las notas → 176/176 URL OK (17-nov-2026).
- Verificado en Chrome headless: 0 mensajes de consola (incluye cambio de tema y clic en todos los controles),
  sin scroll horizontal a 360 px (iframe de 360 px), modo claro y oscuro.
- v0.1 Chile–Colombia conservada en `chile-colombia.html`.

## 🔜 Pendiente
- [ ] Decidir si se publica (GitHub Pages) — **decisión del autor**; hoy privado y sin Pages.
- [ ] Imagen OG y `og:url` cuando haya URL pública.
- [ ] Paleta de 10 países: pasa luminosidad, croma y separación en visión normal, pero el par Ecuador (naranja) ↔ Brasil
      (verde) no pasa la prueba de daltonismo (deuteranopía). Se compensa con etiquetas directas y nombres en ejes; revisar
      si se quiere textura o agrupar.
- [ ] Ecuador: buscar VC 2023–2025 (ECUACAP u otra fuente) y StartupBlink 2025.
- [ ] Portugal: serie homogénea 2018–2023 (Dealroom) y deuda vs equity.
- [ ] España: serie Dealroom 2018–2025 para contrastar con El Referente.
- [ ] Chile, México, Argentina, Uruguay: % de deuda en el VC (LAVCA no lo publica por país).
- [ ] Brasil: serie Sling Hub/Distrito 2018–2024 comparable.
- [ ] Actualizar con LAVCA Trends in Tech 2027 (~feb-2027) y PECAP 2026 (~jun-2027); BIG13 de Start-Up Chile (cierra 24-nov-2026).
- [ ] StartUp Perú 14G: revisar si se publican bases antes de fin de 2026.
- [ ] Visados de emprendedor por nacionalidad en España y Portugal (pregunta clave sobre fundadores peruanos).
- [ ] **Avisar en el repo Perú** (no se modificó aquí): `data/vc_inversion_anual.json` rotula US$76,5M / 23 deals como
      2023; el comunicado COFIDE–PECAP (jun-2026) lo presenta como **2025**.

## ❓ Datos que NO se pudieron verificar (desde `sin_verificar` de cada JSON)
### Perú
- Operaciones 2023: sin dato.
- Mayores rondas 2024 y 2025: PECAP no las publica en las notas encontradas.
- Ganadores StartUp Perú 13G: el repo de Perú cuenta 478 'ganadores posibles' a partir de PDFs; no es la cifra oficial de adjudicados.
- Serie 2018: 9,1 (PECAP, Infomercado) frente a 16 (LAVCA); 2019: 20,6 o 21 según la nota.
### Chile
- Ventas 2025 ACVC (US$854M) solo en fuente secundaria (ecosistemastartup.com).
- Seleccionados de Semilla Inicia y Expande en 2025.
- Porcentaje de venture debt en el VC chileno 2025: LAVCA no lo publica por país.
- Unicornios: conteo por sede (multiples.vc, oct-2026: Cornershop y NotCo); Betterfly no figura; el criterio cambia entre fuentes.
- Sectores 2025: porcentajes leídos de un treemap del PDF (posición de etiquetas).
### Colombia
- Convocatoria ALDEA 2025 y 2026: no se encontró.
- Bancóldex Fondo de Fondos: no se halló convocatoria a gestores en 2026.
- Unicornios: multiples.vc (oct-2026) lista solo a Rappi por sede; Habi y ADDI no figuran; el criterio cambia entre fuentes.
- SENA Fondo Emprender 2025: sin dato de convocatorias.
### México
- Venture debt en México 2025: LAVCA no lo desagrega por país; la deuda estructurada de Plata (US$500M, Nomura) queda fuera de sus cifras.
- Ganadores de Proyectos Ciudadanos y de la convocatoria semilla ATDT–SECIHTI–Nafin: no publicados al corte.
- Montos por startup de la convocatoria semilla (Forbes México citado por fuente secundaria: hasta MXN 6M semilla / 20M avanzados).
- StartupBlink 2025: México #43 según El CEO; el ranking original (startupblink.com) bloquea bots.
- Unicornios: 8 por sede según multiples.vc (oct-2026), conteo sobre la parte visible de la tabla.
### Argentina
- Estado de la Secretaría PyME y de otros instrumentos de la Ley 27.349 (SAS, Fondo Aceleración/Expansión) bajo Milei.
- Venture debt en Argentina 2025.
- Unicornios: 2 por sede (Ualá, Despegar) según multiples.vc; Ámbito cuenta 11 por fundadores argentinos (Mercado Libre, Globant, Auth0, Vercel, etc.): el criterio cambia el resultado.
- Sectores 2025: porcentajes leídos de un treemap del PDF LAVCA.
### Uruguay
- Serie anual de VC 2018–2024 (LAVCA no la publica por país para Uruguay).
- Uruguay XXI/Urucap: ~35 rondas en 2024 (promedio ~US$400k), solo en resumen de prensa (El Observador, oct-2025).
- Beneficiarios anuales del capital semilla ANII 2025–2026.
- Sprint UY 2025: edición previa no verificada (2026 es la tercera).
- Sectores del VC 2025: sin dato.
- Unicornios: multiples.vc cuenta 2 por sede (MercadoLibre y dLocal); Uruguay XXI cuenta dLocal y Nowports.
### Ecuador
- VC 2025: un documento del BID mencionaría US$12,5M en 10 transacciones; el PDF devuelve 403 y no se pudo leer.
- VC 2018–2020 y 2023–2024: sin dato.
- StartupBlink 2025: Ecuador no aparece en las notas de prensa; la página actual de startupblink.com (bloquea bots) lo ubicaría en el puesto 94.
- Programas de capital semilla de MIPRO/CFN para startups en 2025–2026: no se encontraron convocatorias.
- Beneficiarios de los créditos Violeta.
### Brasil
- Serie Distrito/Sling Hub 2018–2024 comparable (solo se publicó el total 2025 de Sling Hub).
- Sectores 2025 distintos de Fintech: valores leídos del treemap de LAVCA (texto extraído con pdftotext); revisar el PDF antes de citar.
- Número de startups aprobadas en Centelha 3 a nivel nacional.
- Beneficiarios de BNDES Garagem ciclo 2025 e InovAtiva 2025.
- Edital de Finep Startup en 2025–2026.
- Monto total de la rodada 2 de Finep Mais Inovação (un boletín Firjan habla de R$3.300 M en 13 editais, pero el PDF responde 403).
### España
- Las cifras de El Referente se reexpresan entre informes (p. ej. 2022: 3.365 vs 3.270 M€; 2024: 2.350 vs una base implícita ~2.920 M€ en el cierre 2025). 2025 incluye deuda y 2023–2024 no: la serie no es homogénea.
- Serie Dealroom 2018–2024 para España (solo se obtuvo el total 2025: US$3.100M).
- Cifra alternativa Fundación Innovación Bankinter 2025 (3.108 M€ / 376 rondas): solo vista en resúmenes; emprendedores.es responde 403.
- Visados de emprendedor por nacionalidad (no hay datos públicos UGE/ENISA por país; peruanos sin cuantificar).
- Tipo de ronda (serie) de las 5 mayores de 2025.
- Convocatorias/resoluciones de Fond-ICO Next Tech en 2025–2026.
### Portugal
- Serie VC 2018–2023 homogénea: las cifras públicas usan perímetros distintos (sede en PT vs ADN portugués) y vintages de Dealroom distintos.
- Distribución sectorial del VC 2025.
- Top rondas de 2025 con montos verificables (la ECO cita Sword Health, Indie Campers, Tekever sin montos uniformes).
- Aprobaciones de Startup Visa y Tech Visa por año y nacionalidad (IAPMEI no publica balance; no hay dato de peruanos).
- Participación de deuda vs equity.
- Fechas de convocatorias 2025–2026 de Portugal Ventures y del IFIC Deep Tech (BPF/PRR).

---

# Anexo — backlog de la edición Chile–Colombia (v0.1)

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
