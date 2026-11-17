# Notas — datos LatAm (CL, CO, PE, MX, AR, UY, EC)

Verificado al 17-nov-2026. Archivos: `data/paises/{cl,co,pe,mx,ar,uy,ec}.json` y `data/latam_agregado.json`.

## Serie comparable: LAVCA
- **2021–2025:** LAVCA Trends in Tech 2026 (p. 2 total LatAm, p. 9 por país, p. 10 por sector). https://www.lavca.org/wp-content/uploads/2026/02/LAVCA_Trends-in-Tech-2026.pdf
- **2020:** LAVCA Trends in Tech 2025 (p. 8 por país). https://www.lavca.org/wp-content/uploads/2025/02/LAVCA_Trends-in-Tech-2025.pdf
- **2018:** LAVCA Tech Report 2019 ("Mapping the major markets"). https://www.lavca.org/wp-content/uploads/2023/10/FINAL2-2019-LAVCA-Tech-Report-04.30.19.pdf
- **2019:** LAVCA VC Tech Report 2020. https://www.lavca.org/wp-content/uploads/2023/10/FINAL3-LAVCA-VC-Tech-Report-2020-08.27.20.pdf
- Las ediciones 2022–2024 de Trends in Tech requieren membresía (HTTP 403). LAVCA revisa años previos entre ediciones; para cada año se usa la edición más reciente que lo cubre.
- **Cobertura por país:** CL, CO, MX y AR tienen la serie completa 2018–2025. Perú solo tiene 2018 (16/11), 2019 (3/6) y 2024 (30). Uruguay solo tiene 2025 (51). Ecuador no aparece.
- **Lectura de gráficos:** los PDF se extrajeron con `pdftotext -layout` y `-bbox`. Los montos por país están rotulados. Las operaciones 2018–2024 del total LatAm, el venture debt por año y los sectores (treemap) se asignaron por la posición de las etiquetas, así que conviene revisar el PDF antes de citar un valor aislado.
- **Deuda en LatAm:** el venture debt sale de la barra apilada de la p. 3 (0,9 / 1,2 / 0,9 / 0,8 / 0,6 US$b entre 2021 y 2025). Las barras de 2018–2020 no tienen etiqueta de deuda. El porcentaje es cálculo propio. LAVCA excluye líneas de crédito, deuda bancaria y FIDCs, que en 2025 sumaron más de US$2.000M aparte.

## Perú (otra metodología: PECAP)
- Serie tomada del repo `radiografia-startups-peru` (con la corrección del 16-nov-2026) y vuelta a buscar con URL para cada año. Sin URL primaria: **2023 ≈ US$50M** (el repo lo atribuye a El Comercio; La Cámara lo cita, pero la página no muestra el texto).
- 2025: US$76,5M, 23 operaciones, 72% deuda (COFIDE–PECAP, jun-2026). Sectores 2025: fintech 76,9% y proptech 19,9% (Gestión).
- StartUp Perú: la 13G se lanzó el 29-dic-2025 y cerró el 16-ene-2026; la 14G no tiene bases al corte. Se registra como convocatoria **2025: sí / 2026: no**.
- No se mezcla con LAVCA. Diferencias: 2018 da 9,1 (PECAP) frente a 16 (LAVCA); 2019 da 21 frente a 3.

## Conflictos y criterios
- **Unicornios:** `multiples.vc` (oct-2026, por sede, incluye adquiridas y listadas) da MX 8, CL 2, AR 2, UY 2, CO 1, EC 1 y PE 0. El conteo se hizo sobre la parte visible de la tabla (50 de 55 filas). Otros criterios dan otros números: Ámbito cuenta 11 unicornios argentinos por fundadores; Uruguay XXI cuenta dLocal y Nowports. Para UY y EC el JSON usa la fuente nacional (Uruguay XXI y Ekos).
- **StartupBlink 2025:** startupblink.com responde 403 a bots, así que los rankings vienen de prensa: Bloomberg Línea Brasil (CO 36, CL 37, AR 46, UY 61, PE 67) y El CEO (MX 43). Ecuador queda sin dato.
- **Colombia, deuda:** el 55,5% de KPMG (2025) no es comparable con LAVCA.
- **Uruguay 2023:** los US$62M vienen de El Observador, que no nombra la fuente; la misma nota da US$835M para México, mientras LAVCA dice 1.144.

## Programas: estado de convocatorias 2026
- **Con convocatoria 2026:**
  - Chile: Start-Up Chile BIG12 y BIG13, Semilla Inicia y Expande.
  - Colombia: iNNpulsa Emprendimiento Digital, iNNpulsa Mujeres y SENA Fondo Emprender.
  - Perú: Concursos Regionales de ProInnóvate y Venture Ready (EE.UU.).
  - México: Proyectos Ciudadanos (Fondo de Fondos, 25-feb a 30-abr) y la convocatoria semilla ATDT–SECIHTI–Nafin.
  - Uruguay: ANII Emprendimientos Innovadores (postulación permanente) y Sprint UY.
  - Argentina: solo la convocatoria provincial de Córdoba.
  - Ecuador: créditos BanEcuador Violeta y Emprende Violeta (microcrédito, no capital de riesgo).
- **Sin convocatoria 2026:**
  - StartUp Perú.
  - INADEM / Fondo Nacional Emprendedor (extinguido en 2019).
  - Fondo Semilla y FONDCE de Argentina (el FONDCE se disolvió por Decreto 1048/2024).
  - Fondo de Fondos de Chile (sigue como proyecto de ley).

## Verificación de enlaces
- Todas las URLs de los 8 JSON se comprobaron con `curl -L` (UA de navegador) el 17-nov-2026. Todas responden 200.
- Se reemplazaron dos URLs que fallaban:
  - El PDF del calendario de ProInnóvate en cdn.www.gob.pe (403) se cambió por startup.proinnovate.gob.pe.
  - El proyecto de ley FONDCE en rest.hcdn.gob.ar no respondía (timeout); solo se menciona en el texto.
- No se pudieron leer, y por eso no se citan como fuente: el PDF del BID "Apoyo al emprendimiento dinámico en el Ecuador" (403), startupblink.com (403) y mexicobusiness.news (403).
- Banco Mundial: la API devuelve errores del WAF de forma intermitente; los valores se obtuvieron reintentando consultas país por país.
