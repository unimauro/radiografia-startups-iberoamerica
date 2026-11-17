# Notas: Brasil, España y Portugal (`data/paises/br.json`, `es.json`, `pt.json`)

Verificado al **17-nov-2026**. Las **48 URLs** citadas en los tres JSON respondieron **HTTP 200** con `curl -L` (UA de navegador).
Convenciones: igual que `data/README.md`. `null` significa que el dato se buscó y no se encontró de forma verificable.

## Campos añadidos al esquema común (opcionales)
- `eur_m`: monto original en millones de euros (España y Portugal). En esos registros, `usd_m` es **cálculo propio** con el tipo
  medio anual del BCE (`tipo_cambio`, https://data-api.ecb.europa.eu/service/data/EXR/A.USD.EUR.SP00.A?format=csvdata&startPeriod=2018&endPeriod=2025).
  Los valores USD/EUR van de 1,0531 (2022) a 1,1827 (2021).
- `vc_anual_alternativas`: otras series del mismo país con distinta metodología. **No se deben mezclar con `vc_anual`.**
- `fuentes_convocatorias` (en programas): URLs que prueban que hubo convocatoria en 2025 o 2026.
- `fundadores_latam` (en es/pt): datos sobre fundadores peruanos o latinoamericanos.
- `nota`, `verificado_al`.

## Metodología de las series VC (`vc_anual`)
| País | Fuente | Comparable con CL/CO | Comentario |
|---|---|---|---|
| Brasil | LAVCA (Tech Report 2019, VC Tech Report 2020, Trends in Tech 2025 y 2026) | **Sí** | Es la misma familia de reportes que se usa para Chile y Colombia. 2018 viene redondeado ("US$1.3b"). Las cifras de 2021–2025 se leyeron por posición de columna en el gráfico (pdftotext). |
| España | El Referente (Observatorio de Startups) | No (base distinta) | 2018–2020 vienen del cierre 2020; 2021–2023 de la versión revisada que publicó El Referente en ene-2024. **2025 incluye deuda (312 M€) y 2023–2024 no**, así que la serie no es homogénea. El Referente reexpresa años anteriores entre informes. |
| Portugal | Dealroom vía informe Startup Portugal 2026 | No | Solo 2024 y 2025 tienen el mismo perímetro (sede o fundadas en PT). 2021–2023 aparecen en `vc_anual_alternativas` con perímetros distintos: con o sin "ADN portugués" fuera del país. |

Alternativas registradas: Brasil Sling Hub 2025, que suma US$4.500M en 459 rondas e incluye FIDC y deuda; España Dealroom 2025, con US$3.100M; Portugal ECO/Dealroom e IDC/Startup Portugal.

## Cifras principales
- **Brasil (LAVCA):** 1.300 (2018), 2.490, 2.550, 7.774, 3.184, 1.867, 2.032 y **1.670 US$M en 296 operaciones (2025)**. Fintech representa 44%. Según Sling Hub, 56,5% del capital 2025 fue deuda o FIDC (cálculo propio). Tiene 22 unicornios (Distrito 2026) y ocupa el puesto 27 en StartupBlink 2025.
- **España (El Referente):** 1.227 (2018), 1.098, 1.102, 4.256, 3.365, 1.525, 2.350 y **3.170 M€ en 303 operaciones (2025)**, unos US$3.582M. La IA representa 11,4% y la deuda 9,8%. Tiene 18 unicornios (Dealroom) y ocupa el puesto 14 en StartupBlink 2025.
- **Portugal (Dealroom/Startup Portugal):** 407 M€ en 193 rondas (2024) y **473 M€ en 157 rondas (2025)**. Hasta septiembre de 2026 suma 694 M€, con Tekever 527 M€. Tiene 7 unicornios y ocupa el puesto 29 en StartupBlink 2025 (31 en 2026).
- StartupBlink 2025 se verificó en el PDF original (https://www.startupblink.com/startupecosystemreport2025.pdf), sección "Top Countries".
- Macro: API del Banco Mundial (SP.POP.TOTL y NY.GDP.MKTP.CD, 2024).

## Programas: ¿hubo convocatoria en 2025 / 2026?
| País | Programa | 2025 | 2026 | Dato clave |
|---|---|---|---|---|
| BR | Centelha 3 (Finep + FAPs) | si | si | Editais estatales 2025 (ES, RS, PE…) y 2026 (MS, AL, RO, MG) |
| BR | BNDES Garagem | si | si | Ciclo 2026 con inscripciones hasta 30-nov-2026; hasta 100 negocios |
| BR | InovAtiva | si | si | 2026 confirmado solo en la modalidad de Impacto |
| BR | Finep Mais Inovação (subvención) | sin dato | si | Edital regional ampliado a R$450M; no es exclusivo de startups |
| BR | Finep Startup | sin dato | sin dato | No se encontró edital vigente |
| BR | FIP Conexões Startups (BNDES/Finep) | sin dato | si | Fondo de R$250M; selección de gestora desde jun-2026 |
| ES | ENISA (préstamos participativos) | si | si | 514 préstamos por 86,2 M€ en 2025; ventanilla permanente |
| ES | CDTI NEOTEC | si | si | 2025: 40 M€ para 130 pymes; 2026: 43,38 M€ |
| ES | Ley de Startups (certificación y visado) | si | si | >2.100 certificadas (2023 a mar-2026) |
| ES | Fond-ICO Next Tech | sin dato | sin dato | Ventanilla para gestoras; sin resolución específica hallada |
| PT | StartUP Voucher (IAPMEI) | si | si | 900 €/mes x 9 meses; 5 M€ |
| PT | Startup Visa / Tech Visa (IAPMEI) | sin dato | si | Activos (ventanilla); sin estadísticas públicas |
| PT | Portugal Ventures (BPF) | sin dato | sin dato | 12,7 M€ en 20 empresas en 2025 |
| PT | BPF Fondo de Fondos | no | sin dato | Anunciado en oct-2025 para 2026 |

## Fundadores peruanos y latinoamericanos
- **España:** no hay estadística pública de visados de emprendedor por nacionalidad. Las residencias de la Ley 14/2013 pasaron de 23.608 (2020) a 91.170 (2024), sin desglose por país (SEDIA, 24-jun-2026). Datos sobre Perú:
  - En **Puentes de Talento V (Madrid + BID Lab, 2025)**, Perú fue el país con más startups entre los 15 fundadores (The Standard CIO).
  - Perú participó en la I edición (2023).
  - La peruana **Excuela** estuvo entre las 17 startups de España-Latam Scale Up 2023 (ICEX).
  - Se citó que 30% de los usuarios de los viveros de Madrid Emprende son latinoamericanos, pero diario.madrid.es e iadb.org responden 403 a bots, así que **no se incluyó**.
- **Portugal:** IAPMEI no publica aprobaciones de Startup Visa por nacionalidad. Lo único disponible es que 11% de las startups tiene capital extranjero (Informa D&B 2026), sin desglose. No hay dato sobre peruanos.

## Huecos principales
1. Portugal no tiene serie VC homogénea para 2018–2023, ni distribución sectorial, ni top rondas 2025 con montos, ni datos de deuda frente a equity.
2. La serie española no es homogénea: incluye deuda solo en 2025 y tiene reexpresiones. Falta la serie Dealroom 2018–2024.
3. Brasil no tiene una serie Sling Hub o Distrito comparable para 2018–2024. Los sectores distintos de fintech se leyeron de un treemap.
4. No se encontraron cifras de beneficiarios para Centelha 3 (nacional), BNDES Garagem 2025 ni InovAtiva 2025.
5. Faltan visados de emprendedor por nacionalidad en ES y PT, que es la pregunta clave sobre peruanos.
6. Bloqueos a bots (403): emprendedores.es, firjan.com.br, diario.madrid.es, iadb.org y madridinnovation.es. **No se citan.**

## Proceso
- La investigación web se hizo con asistencia de IA. Los PDF (LAVCA, StartupBlink, Startup Portugal y Portugal Ventures) se leyeron con `pdftotext`. Los artículos de El Referente se leyeron con `curl` porque WebFetch recibe 403.
- Los JSON se generaron con un script de Python, usando el venv `~/.venvs/startups-cl-co`. No se tocaron otros archivos.
