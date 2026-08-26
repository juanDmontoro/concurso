# Ejercicio completo — todas las notas de orador

Volcado de auditoría de los entornos `::: {.notes}` de las tres partes del ejercicio, en el orden en que se exponen. Generado por `scripts/extraer_notas.py` a partir de los ficheros de parte del deck unificado (`_parte1_cv.qmd`, `_parte2_docente.qmd`, `_parte3_investigacion.qmd`), que `sync_partes.py` copia de los decks fuente.

**Este documento no es una fuente editable.** Sirve para leer y auditar las notas juntas. Cualquier corrección se hace en la fuente que corresponda y se vuelve a sincronizar:

- Partes 1 y 2: «Versión editada» del esquema respectivo (`presentacion_cv_esquema.md`, `propuesta_docente_esquema.md`) → `python 0_ejercicio/deck/scripts/inyectar_notas.py <esquema> <deck.qmd>` → renderizar el deck fuente.
- Parte 3: deck fuente del proyecto hermano `2026_jcr` (`external/jcr_presentation/propuesta_investigacion.qmd`); nunca la copia local.
- Después, en `0_ejercicio/deck`: `python scripts/sync_partes.py && quarto render presentacion_ejercicio.qmd` y regenerar este esquema.

Las notas marcadas **[reserva]** cuelgan de slides dentro de `::: {.content-hidden}`: no se proyectan ni llegan a la vista de orador, y varias son notas de trabajo (con `[Sources]` y cautelas editoriales), no prosa oral. Se incluyen para que la auditoría vea todo lo que hay en el `.qmd`.

## Medición

78 notas en los `.qmd` · 60 en slides visibles (las que rinde el HTML como `<aside class="notes">`) · 18 en slides de reserva.

Solo las visibles: 11199 palabras ≈ 80.0 min a 140 palabras/min (el ejercicio dura 50 min: 15 + 15 + 20).

| Parte | Tiempo asignado | Notas visibles | Palabras | ≈ min | Notas de reserva |
|---|---|---:|---:|---:|---:|
| Parte 1 de 3 · Currículum vitae | 15 min | 19 | 2994 | 21.4 | 7 |
| Parte 2 de 3 · Propuesta docente | 15 min | 17 | 2592 | 18.5 | 3 |
| Parte 3 de 3 · Propuesta investigadora | 20 min | 24 | 5613 | 40.1 | 8 |
| **Total** | **50 min** | **60** | **11199** | **80.0** | **18** |

Palabras incluyendo las notas de reserva: 12003.

Los minutos son una cota superior mecánica: suponen leer en voz alta el texto íntegro de cada nota a 140 palabras/min, sin pausas. Las notas de las Partes 1 y 2 son guion oral (densidad acordada ≈150–180 palabras por nota); las de la Parte 3 vienen del deck fuente de `2026_jcr` y son más extensas, con pasajes de apoyo que no están pensados para decirse enteros.

## Índice de notas

| # | Parte | Slide | Palabras |
|---:|---|---|---:|
| 1 | Parte 1 de 3 | Trayectoria académica: evolución | 251 |
| 2 | Parte 1 de 3 | Perfil académico en cifras *[reserva]* | 74 |
| 3 | Parte 1 de 3 | Trayectoria investigadora | 222 |
| 4 | Parte 1 de 3 | Producción científica en cifras | 117 |
| 5 | Parte 1 de 3 | Publicaciones seleccionadas | 145 |
| 6 | Parte 1 de 3 | Capítulos de libro | 145 |
| 7 | Parte 1 de 3 | Comunicaciones en congresos | 125 |
| 8 | Parte 1 de 3 | Proyectos de I+D+i en convocatoria pública | 162 |
| 9 | Parte 1 de 3 | Contratos y convenios de transferencia (art. 83 LOU / 60 LOSU) | 159 |
| 10 | Parte 1 de 3 | Estancias de investigación | 176 |
| 11 | Parte 1 de 3 | Dirección de tesis doctorales | 192 |
| 12 | Parte 1 de 3 | Trayectoria docente | 172 |
| 13 | Parte 1 de 3 | Docencia reglada | 93 |
| 14 | Parte 1 de 3 | Docencia internacional | 181 |
| 15 | Parte 1 de 3 | Internacionalización docente *[reserva]* | 77 |
| 16 | Parte 1 de 3 | Evaluación de la docencia | 90 |
| 17 | Parte 1 de 3 | Innovación docente | 127 |
| 18 | Parte 1 de 3 | Gestión universitaria | 130 |
| 19 | Parte 1 de 3 | Liderazgo docente e internacionalización | 129 |
| 20 | Parte 1 de 3 | Liderazgo investigador | 195 |
| 21 | Parte 1 de 3 | Otras actividades de liderazgo y participación en la vida universitaria | 183 |
| 22 | Parte 1 de 3 | (slide sin título: `{background-color="#2D6A7A" .center}`) *[reserva]* | 22 |
| 23 | Parte 1 de 3 | Reserva · Otras publicaciones indexadas *[reserva]* | 3 |
| 24 | Parte 1 de 3 | Reserva · Transferencia: entidades y papel *[reserva]* | 7 |
| 25 | Parte 1 de 3 | Reserva · Quinquenios y DOCENTIA: detalle *[reserva]* | 8 |
| 26 | Parte 1 de 3 | Reserva · Alcance geográfico de los congresos *[reserva]* | 34 |
| 27 | Parte 2 de 3 | Herramientas y Técnicas del Análisis de Datos | 132 |
| 28 | Parte 2 de 3 | Herramientas y técnicas de análisis de datos | 110 |
| 29 | Parte 2 de 3 | Técnicas avanzadas de predicción en negocios | 99 |
| 30 | Parte 2 de 3 | El conjunto de datos de referencia | 199 |
| 31 | Parte 2 de 3 | Metodología docente *[reserva]* | 13 |
| 32 | Parte 2 de 3 | Metodología docente: carga de trabajo | 143 |
| 33 | Parte 2 de 3 | Metodología docente: secuencia de aprendizaje | 142 |
| 34 | Parte 2 de 3 | Recursos didácticos *[reserva]* | 19 |
| 35 | Parte 2 de 3 | Recursos didácticos | 113 |
| 36 | Parte 2 de 3 | Evaluación | 142 |
| 37 | Parte 2 de 3 | Proyecto del cuatrimestre | 145 |
| 38 | Parte 2 de 3 | Rúbrica del proyecto | 158 |
| 39 | Parte 2 de 3 | Nota individual del proyecto *[reserva]* | 62 |
| 40 | Parte 2 de 3 | Uso de inteligencia artificial | 181 |
| 41 | Parte 2 de 3 | Experimentos aleatorios controlados: el patrón de referencia | 247 |
| 42 | Parte 2 de 3 | Aprendizaje automático para la estimación de efectos causales | 140 |
| 43 | Parte 2 de 3 | Aplicación *naive* de métodos de aprendizaje automático | 168 |
| 44 | Parte 2 de 3 | Double (Debiased) Machine Learning | 194 |
| 45 | Parte 2 de 3 | Práctica con datos reales | 159 |
| 46 | Parte 2 de 3 | Nivel y alcance del Tema 7 | 120 |
| 47 | Parte 3 de 3 | Esquema | 177 |
| 48 | Parte 3 de 3 | ¿Se ha convertido la música en un deporte de equipo? | 222 |
| 49 | Parte 3 de 3 | Proximidad estética: un aspecto recurrente en la literatura | 334 |
| 50 | Parte 3 de 3 | Marco conceptual | 343 |
| 51 | Parte 3 de 3 | Afinidad estética y emparejamiento multidimensional | 221 |
| 52 | Parte 3 de 3 | Por qué etiquetas y no géneros de plataforma | 246 |
| 53 | Parte 3 de 3 | Proximidad estética | 205 |
| 54 | Parte 3 de 3 | La red previa amplía las oportunidades relacionales | 189 |
| 55 | Parte 3 de 3 | Composición de la red | 137 |
| 56 | Parte 3 de 3 | Definición de la respuesta a modelizar | 207 |
| 57 | Parte 3 de 3 | Diseño: conjunto de riesgo y resultado | 201 |
| 58 | Parte 3 de 3 | ¿Por qué no un ERGM? | 319 |
| 59 | Parte 3 de 3 | Especificaciones: proximidades y modelos anidados | 243 |
| 60 | Parte 3 de 3 | ¿Optimo interior? | 208 |
| 61 | Parte 3 de 3 | Resultado base: especificación cuadrática | 254 |
| 62 | Parte 3 de 3 | Lectura crítica del óptimo interior | 169 |
| 63 | Parte 3 de 3 | La asociación estética crece y se aplana dentro del soporte | 235 |
| 64 | Parte 3 de 3 | Lectura *[reserva]* | 185 |
| 65 | Parte 3 de 3 | Capacidad predictiva por bloques | 282 |
| 66 | Parte 3 de 3 | Constraste no paramétrico de la forma funcional | 137 |
| 67 | Parte 3 de 3 | Comprobaciones de los resultados | 245 |
| 68 | Parte 3 de 3 | Corrección de sesgo de Firth | 188 |
| 69 | Parte 3 de 3 | Logit condicional | 252 |
| 70 | Parte 3 de 3 | La formación es multidimensional | 290 |
| 71 | Parte 3 de 3 | Limitaciones y extensiones | 309 |
| 72 | Parte 3 de 3 | Tres líneas extienden el programa de investigación *[reserva]* | 101 |
| 73 | Parte 3 de 3 | Reserva · Calibración de los modelos predictivos *[reserva]* | 30 |
| 74 | Parte 3 de 3 | Reserva · Aciertos en el top-k (2024) *[reserva]* | 33 |
| 75 | Parte 3 de 3 | Reserva · Estabilidad temporal del perfil *[reserva]* | 33 |
| 76 | Parte 3 de 3 | Reserva · Detalle del test de forma *[reserva]* | 34 |
| 77 | Parte 3 de 3 | Reserva · Cobertura de etiquetas por año *[reserva]* | 34 |
| 78 | Parte 3 de 3 | Reserva · Importancia de variables (SHAP) *[reserva]* | 35 |

---

# Parte 1 de 3 · Currículum vitae

Fuente: `0_ejercicio/cv/deck/presentacion_cv.qmd` · copia sincronizada en `_parte1_cv.qmd`.

## 1. Trayectoria académica: evolución

<sub>`_parte1_cv.qmd:32` · encabezado de nivel 2 · 251 palabras</sub>

Buenos días. Con la venia de la comisión, comienzo la presentación del currículum con la línea temporal, que resume treinta años en la Universitat de València, desde la finalización de la licenciatura en Ciencias Económicas y Empresariales en 1991 hasta la acreditación a catedrático de universidad por la ANECA en octubre de 2024. 

La primera etapa es la de formación y estabilización: tesis doctoral en 1996, plaza de ayudante en 1997 en el área de Economía Aplicada, titularidad de escuela en 2002, habilitación nacional en la universidad de Alcalá de Henares en 2004 que me permite acceder a la plaza de titular de universidad en 2005. La segunda, de internacionalización,  arranca con la adscripción al área de Métodos Cuantitativos en 2007 y concentra la coordinación del título de ADE/GEDE, el proyecto ATLANTIS de la UE y la fundación y vicepresidencia de IMBRA. La tercera, desde 2016, de consolidación, con la evaluación positiva del sexenio de transferencia y tercer y cuarto sexenios de investigación, la dirección del grupo de investigación CREAMARKT y la codirección del grupo consolidado de innovación docente.

En cifras: cuatro sexenios de investigación y uno de transferencia, cuarenta y seis artículos, treinta y seis en revistas indexadas, más de ochocientas citas; cinco quinquenios y una evaluación DOCENTIA excelente, doscientos sobre doscientos; la dirección de un grupo de investigación, dos tesis con cum laude y la coordinación de una titulación internacional.

La exposición sigue el orden del currículum: investigación y transferencia, docencia, y dirección y liderazgo. Empiezo por la investigación.

## 2. Perfil académico en cifras · **[reserva: slide en `.content-hidden`]**

<sub>`_parte1_cv.qmd:80` · encabezado de nivel 2 · 74 palabras</sub>

Presentación personal breve. La tabla-ficha no se lee: comentar solo las tres líneas de cifras de la derecha. Las cifras se desarrollan en los bloques siguientes.

Guion de la presentación: Tres bloques, en el orden del CV presentado: **investigación y transferencia**, **docencia** y **dirección y liderazgo**.

[Sources]
CV_final.qmd: títulos (l. 4205–4226), acreditación CU (l. 4231–4257), sexenios y quinquenios (l. 3511–3535), DOCENTIA (l. 2740–2752), artículos (§2.1), resumen (l. 63–137). Citas: snapshot data/metricas_perfiles.md (03-08-2026; GS 807).

## 3. Trayectoria investigadora

<sub>`_parte1_cv.qmd:105` · encabezado de nivel 2 · 222 palabras</sub>

La tabla ordena la trayectoria investigadora en tres etapas, con los trabajos representativos y los principales coautores. La leo como una línea acumulativa donde cada etapa toma métodos y preguntas de la anterior.

La primera, de 1995 a 2003, centrada en economía computacional, se articula en torno a la elaboración de la tesis doctoral sobre simulación y detección de caos macroeconómico (dirigida por José Vicente Paz) que da lugar a dos capítulos en Computational Mechanics Publications y un artículo en el Journal of Macroeconomics en 1998. 

La segunda, de 1998 a 2010, se centra en la elección pública con diversos trabajos junto a Miguel Puchades-Navarroy José Casas-Pardo: artículos en CIRIEC-España, Constitutional Political Economy, Computational Economics y  capítulos en el homenaje al nobel James Buchanan de Springer y en una monografía en Edward Elgar en 2013. 

La tercera, desde 2008, centrada en la economía de la cultura y el consumo cultural: la transición entre estas dos últimas viene del trabajo sobre propiedad intelectual, con el artículo de 2008 en el European Journal of Law and Economics. Los trabajos se realizan junto a Manuel Cuadrado-García, y más recientemente con María Caballer-Tarazona y María Luisa Palma-Martos, y se exploran diversos aspectos  siguió de la participación cultural, las industrias creativas y el big data, en publicaciones como el Journal of Cultural Economics, Poetics y Empirical Economics.

## 4. Producción científica en cifras

<sub>`_parte1_cv.qmd:132` · encabezado de nivel 2 · 117 palabras</sub>

La diapositiva  cuantifica la producción científica agrupada por año y categoría y muestra  una producción continua desde 1998 con una concentración creciente en economía de la cultura a partir de 2008.

Los titulares de los principales índices bibliométricos se complementan con información que los cualifica: una serie ascendente de citas (cerca del sesenta por ciento de las citas de Google Scholar se ha recibido desde 2021) y más del noventa por ciento de las de Web of Science son externas y dos citas en documentos de política pública. Añado dos datos que no caben en la tabla: treinta y cinco revisiones por pares verificadas, en el percentil 91.

De ese conjunto selecciono ocho publicaciones por su relevancia.

## 5. Publicaciones seleccionadas

<sub>`_parte1_cv.qmd:156` · encabezado de nivel 2 · 145 palabras</sub>

De las ocho, me detengo en tres bloques.

El primero es el artículo de 2011 en el Journal of Cultural Economics sobre consumo de música en vivo y grabada, el más citado del área en mi perfil: cuarenta y cuatro citas en Web of Science, cincuenta y cuatro en Scopus y ciento veinticuatro en Google Scholar. 

El segundo bloque son los dos artículos en Poetics, primer cuartil de sociología: el de 2020, sobre los festivales de música como mediadores, y el de 2025, un análisis bibliométrico de la investigación sobre consumo cultural y diversidad. 

El tercero es la revisión de veinte años de investigación sobre consumo de música en el International Journal of Consumer Studies, de 2021, (y primer cuartil de business) que supone una sistematización de la investigación en el campo generada hasta el momento y permite definir la agenda de investigación en adelante.

## 6. Capítulos de libro

<sub>`_parte1_cv.qmd:183` · encabezado de nivel 2 · 145 palabras</sub>

Junto a los artículos, la otra vía de publicación han sido los capítulos de libro.

Esta tabla recoge siete capítulos seleccionados por la relevancia de la editorial, Springer, Emerald, Edward Elgar, Routledge y Oxford University Press, entre 2001 y 2022, de los veintinueve capítulos y libros que constan en el currículum.

La serie acompaña a la trayectoria investigadora: un capítulo eminentemente computacional en 2001 sobre evolución y aprendizaje en modelos de decisión colectiva, o el capítulo de Edward Elgar que modifica los modelos teóricos de búsqueda de rentas, de autoría única, cierra la etapa de elección pública. La mayor parte de la producción, en economía de la cultura, abarca consumo de música grabada e infracción de derechos de autor y piratería digital o participación cultural desde la doble perspectiva en vivo y digital.

Esta producción se ha presentado y discutido de forma continuada en congresos.

## 7. Comunicaciones en congresos

<sub>`_parte1_cv.qmd:203` · encabezado de nivel 2 · 125 palabras</sub>

La figura ordena las comunicaciones a congresos, la mayor parte internacionales, por serie y por año. Tres hechos sobresalen.

La primera es la recurrencia en las series de referencia del ámbito de economía de la cultura: comunicaciones en AIMAC, ACEI,  IMBRA o el Workshop en Economía y Gestión de la Cultura. La segunda es el relevo temático, que reproduce la trayectoria investigadora: la participación en la sociedad europea de elección pública la sustituyen las series del área cultural. La tercera es la vigencia: el último punto de AIMAC está en 2026, con dos comunicaciones presentandas en Río de Janeiro. El círculo rojo marca AIMAC 2007 en València, donde copresidí el comité científico; las veintiocho comunicaciones de innovación docente las recupero en el bloque de docencia.

## 8. Proyectos de I+D+i en convocatoria pública

<sub>`_parte1_cv.qmd:227` · encabezado de nivel 2 · 162 palabras</sub>

La actividad investigadora se ha apoyado en dos pilares: por un lado los proyectos financiados en convocatoria pública.

La tabla lista los proyectos en convocatoria pública, con la entidad financiadora, los años y mi participación. Cabe subrayar la continuidad, de 1998 a 2019, y los tres niveles de convocatoria: autonómica, nacional y europea.

Los primeros siguen la trayectoria que he contado: los dos proyectos sobre teoría del caos, el de la CICYT sobre el funcionamiento de las instituciones democráticas y el de protección del cliente en el sistema financiero; después, la colaboración virtual entre universidades europeas, en 2008 y 2009, y la regulación de la economía colaborativa, de 2016 a 2019.

Me detengo en el MBA-TABSA financiado por la Comisión Europea entre 2010 y 2014, proyecto que dirigí: se trata de un proyecto transatlántico que combina el análisis del impacto de la movilidad del alumnado entre instituciones con el de la creación de vinculos entre investigadores (gestionado junto con la Hochschule Bremen).

## 9. Contratos y convenios de transferencia (art. 83 LOU / 60 LOSU)

<sub>`_parte1_cv.qmd:260` · encabezado de nivel 2 · 159 palabras</sub>

La segunda fuente de financiación, y de datos, para l aactividad investigadora ha sido la transferencia con el sector cultural.

Esta tabla recoge los diez contratos y convenios más recientes con el tejido cultural, desde el estudio de públicos del festival Tercera Setmana con AVETID en 2017. En total son dieciséis desde 2012, seis como investigador principal, una actividad que está reconocida con el sexenio de transferencia del periodo 2012–2017.

Es importante transmitir que la transferencia forma parte de la investigación: los convenios generan datos y preguntas que acaban en publicaciones. Un ejemplo: el  convenio con Francachela Teatro ha dado lugar al artículo de 2022 en el Journal of Homosexuality, segundo cuartil JCR. Además cabe señalar que La relación con el sector es estable, de las asociaciones de artes escénicas a la Generalitat, ICOM o BIOPARC.

En todos ellos el trabajo se hace en equipo, bajo la dirección de Manuel Cuadrado-García y, en varios de ellos, con mi codirección.

## 10. Estancias de investigación

<sub>`_parte1_cv.qmd:288` · encabezado de nivel 2 · 176 palabras</sub>

Un aApecto final de la dimensión investigadora son las estancias.

La tabla lista las seis estancias oficiales de investigación, con la financiación y el periodo: seis estancias en cinco países, unos dieciocho meses acumulados y todas con financiación competitiva, de la Generalitat Valenciana o de la Universitat de València.

Describen el mismo perfil que la trayectoria investigadora. En 1998, seis meses en el Center for Study of Public Choice de George Mason, el centro de Buchanan. En 2001, cuatro meses en el CREED de la Universidad de Ámsterdam, el centro de economía experimental, donde presenté un seminario. Y en 2013, tres meses en el Institut für Kulturmanagement de la Universidad de Música y Artes Escénicas de Viena, ya en economía y gestión de la cultura. Las dos estancias en HEC Montréal, en 1999 y 2007, conectan con la vertiente de marketing de las artes, la de los casos docentes y de buena parte de los coautores, y la de la London School of Economics en 2007 está en el origen del proyecto docente que presento después.

## 11. Dirección de tesis doctorales

<sub>`_parte1_cv.qmd:311` · encabezado de nivel 2 · 192 palabras</sub>

Cierro este bloque con la dirección de tesis doctorales. En la tabla se recogen cuatro tesis, dos leídas y dos en curso, con el doctorando, su afiliación actual, el año y las observaciones.

Las dos tesis leídas lo fueron en el programa de doctorado en Marketing, con mención de calidad, y las dos obtuvieron sobresaliente cum laude. La de Desamparados Lluch, de 2017, sobre segmentación y exhibición cinematográfica en el mercado español con modelos de clases latentes, recibió además el Premio Fundación SGAE de Investigación de 2018. La de Piergiacomo Mion Dalle Carbonare, de 2022, analiza el efecto del entorno de servicio ampliado sobre la satisfacción y la lealtad de los visitantes de museos.

Las dos en curso siguen la misma línea: la de Ariadna Martin Alfaro, sobre el consumidor de música clásica, y la de Giuliano Picchi, en el MIT, sobre el comportamiento del visitante y las intervenciones urbanas en el arte contemporáneo. Picchi coautoriza una de las comunicaciones aceptadas en AIMAC 2026, mientras que con Martin tenemos un JCR en revisión, señal de que la línea sigue produciendo.

Con esto cierro investigación y transferencia y paso al bloque de docencia.

## 12. Trayectoria docente

<sub>`_parte1_cv.qmd:340` · encabezado de nivel 2 · 172 palabras</sub>

La tabla organiza treinta años de docencia en tres etapas, por área, con las asignaturas. En términos agregados la docencia se distribuye en siete centros, trece titulaciones, dieciocho asignaturas distintas y docencia en castellano,  valenciano (en la actualidad acredito un nivel C1 de la lengua propian de la universitat de València) e inglés (que representa la mitad de la docencia total).

La primera etapa, desde 1997, en Economía Política, con docencia en castellano y en valenciano. La segunda empieza con el cambio de área en el curso 2006-2007 y es la de la estadística introductoria e inferencial, con la integración de esas troncales en el grupo de alto rendimiento académico, en inglés. La tercera, desde 2019, cubre mayoritariamente aprendizaje estadístico: Datos No Estructurados y Técnicas Avanzadas de Predicción en el grado en Inteligencia y Analítica de Negocios y cuatro asignaturas de máster, entre ellas Inferencia Causal y Aprendizaje Máquina en el máster en Ciencia de Datos y Big Data en Economía en el máster en Economía, con un peso creciente del posgrado.

## 13. Docencia reglada

<sub>`_parte1_cv.qmd:355` · encabezado de nivel 2 · 93 palabras</sub>

Esta figura refleja la trayectoria temporal de mi experiencia docente, distribuida en cada uno de los tres bloques mencionados y codificada por idioma en el que se imparte la docencia  agrupada .

Subrayar la superposición en las diferentes etapas (que no se sustituyen de forma abrupta sino que se solapan) y el peso del inglés desde 2007, que se corresponde a mi integración en  la docencia en el grupo internacional, una apuesta por el equipo directivo de la Facultat d'Economia dirijida por la decana Trinidad Casasús Estellés, para  profundizar la internacionalización del centro.

## 14. Docencia internacional

<sub>`_parte1_cv.qmd:382` · encabezado de nivel 2 · 181 palabras</sub>

Esa docencia en inglés tiene su prolongación fuera de la Universitat, en la participación en la docencia y las estancias docentes que la tabla muestra: siete estancias docentes oficiales, en grado y posgrado, entre 2000 y 2019.

Para instituciones de Estados Unidos, imparto dos cursos de grado en la State University of New York en Albany en el año 2000, dentro de un programa con la Politècnica de València, y en 2013 Econometrics en la University of North Florida y Statistics e International Marketing en la University of North Carolina en Wilmington. En el Reino Unido, el seminario sobre economía y música en la London School of Economics en 2007, que coincide con la estancia de investigación, y un curso sobre la gestión de la pequeña empresa en la industria musical en Hertfordshire en 2011. En Buenos Aires, en 2013, un seminario de maestría sobre información y toma de decisiones en gestión cultural. Y en Bremen, Statistik I en la Hochschule en 2018 y Global Economics en el MBA del International Graduate Center en 2018 y 2019, las dos en inglés.

## 15. Internacionalización docente · **[reserva: slide en `.content-hidden`]**

<sub>`_parte1_cv.qmd:405` · encabezado de nivel 2 · 77 palabras</sub>

Invitación al panel "Double Degrees — An Emerging Trend in Business Education Globally" (International Business Conference, Univ. of North Florida, 2013).

Fechas de GEDE unificadas en 2010–2014 (cargo unipersonal desde 26/02/2010, l. 3103; la prosa del Resumen dice "2009" — divergencia anotada). Comisiones: Intercambio de Estudiantes UV 14/01/2010–22/12/2012 (l. 3055); Relaciones Internacionales UV 23/12/2010–25/09/2014 (l. 3128); intercambio de la Facultat 14/01/2010–31/08/2014 (l. 3062, duplicada en l. 3089).

[Sources]
CV_final.qmd, Resumen (l. 85), §3.3.2, §3.7, §4.1 (l. 3046–3131).

## 16. Evaluación de la docencia

<sub>`_parte1_cv.qmd:424` · encabezado de nivel 2 · 90 palabras</sub>

La diapositiva reúne las dos evaluaciones externas de la docencia. A la izquierda, el programa DOCENTIA del periodo 2017–2021, nivel avanzado, con la calificación de excelente y doscientos puntos sobre doscientos.

A la derecha, la valoración media del alumnado por curso, en una escala de uno a cinco, desde 1996 hasta 2024: una serie ascendente, estable por encima de cuatro con tres desde 2017, con el máximo de cuatro con setenta y ocho en el curso 2023-24.

Quiero pensar que parte de esa evaluación está vinculada a la innovación docente.

## 17. Innovación docente

<sub>`_parte1_cv.qmd:451` · encabezado de nivel 2 · 127 palabras</sub>

Innovación docente que queda resumida en catorce proyectos, tres como investigador principal, la codirección de un grupo de innovación consolidado, veintiocho comunicaciones y cinco artículos más un capítulo de libro.

El grupo de innovación, que canaliza los proyectos de innovación docente, es multiaprendizaje, transversalidad y creatividad (continúa al grupo Innova multidisciplinar de 2009 a 2012) y obtuvo la mención de grupo consolidado en 2023, renovada en 2026. He dirigido tres proyectos  recientemente y he presentado veintiocho comunicaciones que se reparten en las series de referencia de la innovación: CIDUI, las jornadas de innovación educativa de la Universitat, las redes INNOVAESTIC, WCES y el congreso internacional de innovación docente de 2022. Gran parte de esta actividad en innovación se h atraducido en publicaciones en diversas revistas y/o monografías.

## 18. Gestión universitaria

<sub>`_parte1_cv.qmd:481` · encabezado de nivel 2 · 130 palabras</sub>

En lo que respecta a liderazgo y gestión, la tabla lista los cargos de gestión con  periodo y  ámbito, que se resumen en diecisiete cargos y tareas de gestión, donde la mayoría se concentra en la internacionalización.

Entre 2010 y 2014 siendo coordinador de intercambios de las dobles titulaciones de ADE-GEDE y de International Business, fui el representé de la Facultat d'Economia (por delegaciónde la vicedecana Delfina Soria Bonet) en la Transatlantic Business School Alliance y ; en el mismo periodo fui miembro de la Comisión de Intercambio de Estudiantes y de la Comisión de Relaciones Internacionales de la Universitat, y de la comisión de intercambio de la Facultat. En otro orden de cosas, desde 2021 formo parte de la comisión de coordinación académica del máster en Ciencia de Datos.

## 19. Liderazgo docente e internacionalización

<sub>`_parte1_cv.qmd:502` · encabezado de nivel 2 · 129 palabras</sub>

El liderazgo de perfil docente se materializa en la dirección de cuatro proyectos docentes y de innovación. Además, he coordinado  el Graduado Europeo en Dirección de Empresas, titulación propia de la Universitat, entre 2010 y 2014, un cargo académico unipersonal. He sido coordinador de la unidad docente de Estadística del área en el curso 2020-21, formé parte de la comisión delegada para la reforma de la estadística introductoria en 2016-17, coordiné un grupo de estudiantes compitiendo en el programa MOTIVEM en 2021 así como guías docentes de grado y posgrado. Y en internacionalización he sido coordinador responsable del convenio con la Zarb School of Business de Hofstra University, en Nueva York, de 2014 a 2019, y de los intercambios de las dobles titulaciones de la Facultat d'Economia hasta 2014.

## 20. Liderazgo investigador

<sub>`_parte1_cv.qmd:522` · encabezado de nivel 2 · 195 palabras</sub>

El liderazgo investigador se materializa en cinco vertientes. La primera es el grupo de investigación CREAMARKT, que dirijo desde noviembre de 2022 centrado en cuatro líneas de investigación: big data aplicado a las industrias creativas, microeconometría de la participación cultural, consumidor 2.0 y diversidad en los mercados culturales.

La segunda es mi participación en  asociaciones científicas: fundador de IMBRA, la International Music Business Research Association, y su vicepresidente entre 2015 y 2019 y miembro de la junta ejecutiva hasta 2023, y miembro de ACEI y de AIMAC. 

La tercera, la labor editorial: he sido co-editor invitado del número especial sobre consumo de las artes, diversidad e inclusión del International Journal of Arts Management en 2023. 

La cuarta, participación en comités: copresidí el comité científico de AIMAC 2007 en València, he participado en los paneles de evaluación de once ediciones de AIMAC y formé parte de los comités de los dos primeros Workshop en Economía y Gestión de la Cultura y del congreso de marketing público y no lucrativo de 2009. 

La quinta, la evaluación científica: treinta y cinco revisiones verificadas para quince revistas, percentil 91, y el reconocimiento de Poetics a esa actividad en 2026.

## 21. Otras actividades de liderazgo y participación en la vida universitaria

<sub>`_parte1_cv.qmd:552` · encabezado de nivel 2 · 183 palabras</sub>

Cierro la presentación del curriculum con una recapitulación de la que destaco tres grupos de actividades.

El primero es la proyección internacional: las conferencias y seminarios por invitación, del CREED de Ámsterdam en 2001 a la London School of Economics, Viena o Buenos Aires, y la evaluación externa de tesis y trabajos en Télécom ParisTech, Berlín, Hannover, Estocolmo y Girona. 

El segundo es el servicio al sistema universitario: tres tribunales de tesis y tres comisiones de plazas de profesorado, en el País Vasco, Valladolid y el CEU. 

El tercero es la proyección social: cinco jornadas académico-profesionales con el sector cultural entre 2015 y 2021 y la divulgación en el Observatorio Social de la Caixa y en EconomistsTalkArt. Las invitaciones de 2026, en la Universidad de Oviedo sobre aprendizaje automático y en el curso de verano de Almagro, muestran que las dos líneas del perfil siguen activas.

El balance es el del resumen del currículum: una investigación consolidada con una estructura estable e internacional, liderazgo editorial y asociativo en el área, una docencia evaluada como excelente, internacional y una transferencia sostenida al sector cultural.

## 22. (slide sin título: `{background-color="#2D6A7A" .center}`) · **[reserva: slide en `.content-hidden`]**

<sub>`_parte1_cv.qmd:593` · encabezado de nivel 2 · 22 palabras</sub>

Cierre: las cuatro fortalezas del Resumen del historial académico, tal como constan en el CV presentado.

[Sources]
CV_final.qmd, Resumen (l. 134), §6.3.1.

## 23. Reserva · Otras publicaciones indexadas · **[reserva: slide en `.content-hidden`]**

<sub>`_parte1_cv.qmd:618` · encabezado de nivel 2 · 3 palabras</sub>

[Sources]
CV_final.qmd §2.1.

## 24. Reserva · Transferencia: entidades y papel · **[reserva: slide en `.content-hidden`]**

<sub>`_parte1_cv.qmd:637` · encabezado de nivel 2 · 7 palabras</sub>

[Sources]
CV_final.qmd, Resumen (l. 132), §2.4, §4.2.

## 25. Reserva · Quinquenios y DOCENTIA: detalle · **[reserva: slide en `.content-hidden`]**

<sub>`_parte1_cv.qmd:658` · encabezado de nivel 2 · 8 palabras</sub>

[Sources]
CV_final.qmd §3.5 (l. 2740–2788), §4.6 (l. 3521–3529).

## 26. Reserva · Alcance geográfico de los congresos · **[reserva: slide en `.content-hidden`]**

<sub>`_parte1_cv.qmd:672` · encabezado de nivel 2 · 34 palabras</sub>

Reserva por si el tribunal pregunta por el alcance geográfico de los congresos (la slide principal muestra la recurrencia por series).

[Sources]
CV_final.qmd §2.5 (l. 697–1890). Figura: scripts/fig_mapa_congresos.py, datos data/ponencias_geo.csv (agregado por país, 03-08-2026).

---

# Parte 2 de 3 · Propuesta docente

Fuente: `0_ejercicio/propuesta_docente/sol/propuesta_docente.qmd` · copia sincronizada en `_parte2_docente.qmd`.

## 27. Herramientas y Técnicas del Análisis de Datos

<sub>`_parte2_docente.qmd:48` · encabezado de nivel 1 · 132 palabras</sub>

Paso a presentar la propuesta docente que abarca la asignatura Técnicas Avanzadas de Predicción en Negocios, obligatoria de tercer curso del grado en Inteligencia y Analítica de Negocios. La exposición tiene tres partes: la asignatura y su organización; el proyecto del cuatrimestre, que es el eje de la evaluación; y el desarrollo de un Tema, predicción y efectos causales, que muestra la manera de trabajar del curso.

En la diapositiva muestro  la ficha resumida del grado (Facultat d'Economia, cuatro cursos y doscientos cuarenta créditos, cincuenta plazas de nueva entrada), su principal objetivo que integra tres ámbitos (economía y empresa,  métodos cuantitativos y tecnología).

La asignatura, dentro de la materia Herramientas y Técnicas del Análisis de Datos se orienta al uso de métodos computacionales y modelos predictivos tanto para predecir como para explicar.

## 28. Herramientas y técnicas de análisis de datos

<sub>`_parte2_docente.qmd:73` · encabezado de nivel 2 · 110 palabras</sub>

La tabla presenta las siete asignaturas de la materia, junto a su información básica.

Es en tercer curso cuando los estudiantes llegan a Técnicas Avanzadas de Predicción en Negocios (tras haber cursado en segundo curso Minería de Datos en Negocios y las dos asignaturas de predicción, con datos transversales y temporales). El curso cubre diversos estimadores (ensambles, máquinas de vectores de soporte, redes neuronales) y diferencia entre predicción y explicación con una introducción a efectos causales.

Señalar la ubicación de la asignatura que llega tras explorar datos y predecir con modelos sencillos, y aplia el catálogo predictivo con métodos más flexibles y su utilización para predecir y estimar parámetros estructurales.

## 29. Técnicas avanzadas de predicción en negocios

<sub>`_parte2_docente.qmd:127` · encabezado de nivel 2 · 99 palabras</sub>

La ficha de la asignatura concreta ese punto de partida, y muestra

1. Por un lado los datos formales: carácter, ubicación, y carga docente y de trabajo.

2.  Por otro lado lo que la signatura asume y lo que ofrece. 

Quizá es ese tercer objetivo lo que diferencia el enfoque de la asignatura: predecir bien no responde por sí solo a la pregunta del negocio, que muchas veces conlleva una afirmación de tipo  causal, y el estudiante tiene que saber reconocer cuándo lo es. El Tema 7 lo desarrolla con un caso de negocio, al final de la exposición.

## 30. El conjunto de datos de referencia

<sub>`_parte2_docente.qmd:158` · encabezado de nivel 1 · 199 palabras</sub>

La tabla muestra la distribución de los siete temas de la asignatura en las quince semanas del cuatrimestre; la tercera columna vincula cada tema con su práctica y con los hitos de un proyecto en equipos que los estudiantes desarrollan.

El recorrido va de lo simple a lo flexible: fundamentos y entorno de trabajo reproducible en la primera semana; selección y evaluación de modelos en la dos y la tres, cuando se forman los grupos del proyecto; el modelo lineal generalizado con regularización, que es el modelo base del curso y del proyecto; después los ensambles, las máquinas de vectores de soporte y las redes neuronales, con la revisión intermedia del proyecto; y las semanas trece y catorce son el Tema 7, con la simulación de los sesgos, el flujo de trabajo con DoubleML y una posible extensión causal en el proyecto, antes de la defensa oral en la quince.

Una decisión de diseño aplicable a toda la tabla: durante las prácticas, la asignatura usa un mismo conjunto de datos de referencia, sobre el que se aplican todas las técnicas. Eso permite comparar los modelos en un contexto común y ver qué método conviene según el objetivo del negocio.

## 31. Metodología docente · **[reserva: slide en `.content-hidden`]**

<sub>`_parte2_docente.qmd:221` · encabezado de nivel 2 · 13 palabras</sub>

[Sources]
- Guía docente 36520, curso 2026-27: volumen de trabajo y metodología docente.

## 32. Metodología docente: carga de trabajo

<sub>`_parte2_docente.qmd:245` · encabezado de nivel 2 · 143 palabras</sub>

La tabla desglosa las ciento cincuenta horas del estudiante por actividades, con su carga semanal y total: sesenta horas presenciales y noventa no presenciales.

La semana tipo tiene cuatro horas presenciales: una de teoría, en la que se presenta el problema, los conceptos y la discusión, y tres de práctica en aula informática, con un notebook guiado, trabajo autónomo y entregas. 

La proporción refleja el carácter de la asignatura: tres cuartas partes del tiempo presencial transcurren implementado soluciones estadísticas a preguntas de negocios, y la teoría ocupa una hora para plantear el problema y discutir y comparar los estimadores. El notebook guiado es el punto de partida de cada sesión; lo que cuenta son las evidencias de aprendizaje que salen de esa práctica cada semana y alimentan las entregas y el proyecto. Dentro de cada tema, ese trabajo sigue siempre la misma secuencia.

## 33. Metodología docente: secuencia de aprendizaje

<sub>`_parte2_docente.qmd:266` · encabezado de nivel 2 · 142 palabras</sub>

La secuencia que sigue cada tema se puede reumir en cinco pasos: pregunta, exploración, comparación, formalización y decisión. Es un recorrido que va de la narrativa a lo visual, de lo visual al código y del código a lo formal.

Primero se plantea un problema de negocio; después se explora con datos, gráficos y simulaciones; en tercer lugar se codifican, evalúan y comparan soluciones; solo entonces se formaliza el método y se revisan sus supuestos; y al final se interpreta el resultado y se justifica una elección. El orden es deliberado: el formalismo llega cuando el estudiante ya ha visto el problema, ha manipulado los datos y ha comparado modelos, de modo que las fórmulas responden a preguntas que ya se ha hecho. 

Las sesiones prácticas desarrollan así los contenidos de la teoría y producen evidencias de aprendizaje durante todo el cuatrimestre.

## 34. Recursos didácticos · **[reserva: slide en `.content-hidden`]**

<sub>`_parte2_docente.qmd:327` · encabezado de nivel 2 · 19 palabras</sub>

[Sources]
- Guía docente 36520, curso 2026-27, bibliografía.
- Fernández-Villaverde y Nuño (2023), Machine Learning for Economists, bloque 1.

## 35. Recursos didácticos

<sub>`_parte2_docente.qmd:353` · encabezado de nivel 2 · 113 palabras</sub>

Los recursos didácticos se agrupan en ocho tipos: software y entornos de trabajo, materiales expositivos y prácticos, recursos interactivos, recursos para la evaluación y para la reproducibilidad, y bibliografía.

El software es Python con librerías scikit-learn, Keras y DoubleML. ¿Por qué Python si los alumnos llegan con conocimientos amplios de R?  Python ofrece  librerías de referencia para  métodos avanzados, es la herramienta habitual en la industria de datos, se puede usar en la nube a través de Colab sin instalación local y, sobre todo, permite transferir los conocimientos: cambia la herramienta, no el concepto. Los entornos, Jupyter, Colab y un entorno conda versionado, hacen que el trabajo sea reproducible desde el primer día.

## 36. Evaluación

<sub>`_parte2_docente.qmd:372` · encabezado de nivel 2 · 142 palabras</sub>

La práctica y la evluación continua tienen un peso sutantivo en la evaluación en una barra: un treinta y cinco por ciento corresponde al proyecto final con su defensa oral; un treinta por ciento las entregas individuales en aula y un diez por ciento la participación. El veinticinco por ciento restante corresponde al examen final escrito (exige un mínimo de coinco sobre diez). 

El diseño responde a la metodología: si el aprendizaje se produce mayoritariamente en la práctica semanal y a través del proyecto, la mayor parte de la nota tiene que salir de ahí. El examen conserva un peso suficiente para comprobar que cada estudiante domina individualmente los conceptos, y el mínimo evita que una buena nota de proyecto compense la falta de esa base.

El proyecto es la pieza central de esa evaluación y el segundo bloque de la exposición.

## 37. Proyecto del cuatrimestre

<sub>`_parte2_docente.qmd:391` · encabezado de nivel 2 · 145 palabras</sub>

El desarrollo del proyecto se organiza a lo largo de una serie de entregas parciales o hitos durante el cuatrimestre. Los grupos, de tres o cuatro estudiantes, eligen en la semana dos su propio conjunto de datos y su propio problema; después entregan el análisis exploratorio y el pipeline de preprocesado, el modelo base, un GLM regularizado, y los ensambles; hacia la mitad del cuatrimestre hay una  entrega con retroalimentación; en la semana trece, como aspecto opcional, se puede formular una extensión causal al modelo predictivo; y en la quince, la memoria, el repositorio y la defensa oral. Cada hito usa el contenido desarrollado en las semanas anteriores, de manera que el proyecto avanza con el temario. Durante todo el recorrido el uso de inteligencia artificial está permitido, declarado y auditado. La entrega final, repositorio reproducible, memoria y defensa oral, se califica con una rúbrica.

## 38. Rúbrica del proyecto

<sub>`_parte2_docente.qmd:407` · encabezado de nivel 2 · 158 palabras</sub>

Ésta tiene cinco dimensiones con su peso, lo que se observa en cada una y los descriptores de tres niveles: excelente, apto y no apto. Importante mencionar que la defensa oral individual pesa un treinta por ciento.

Más que los pesos, importa qué premia y qué penaliza. Premia una pregunta orientada a la toma de decisiones y susceptible de respuesta empírica, un repositorio que reproduce todo desde los datos crudos con un entorno versionado, la comparación de los modelos en un test común y la traducción de los resultados a una decisión de negocio que incorpore la incertidumbre. Y es explícita en los no aptos: una fuga de información, elegir las métricas a posteriori o que un miembro del grupo no sepa explicar su propio código. El nivel excelente de la defensa exige que cada miembro explique y modifique en vivo cualquier parte del código.

La última pieza del proyecto es la política de uso de inteligencia artificial.

## 39. Nota individual del proyecto · **[reserva: slide en `.content-hidden`]**

<sub>`_parte2_docente.qmd:442` · encabezado de nivel 1 · 62 palabras</sub>

**Observaciones**

- **Retroalimentación a lo largo del curso:** hito intermedio (S10) con la rúbrica provisional aplicada sin nota; defensa final (S15) con la definitiva
- **Penalizaciones** (publicadas): entrega tardía -1 punto/día; fuga de información detectada → dimensión de modelización a no apto
- **Condición previa**:  compromiso con las entregas de acuerdo con planificación; caso contrario  la nota máxima del proyecto es 4/10

## 40. Uso de inteligencia artificial

<sub>`_parte2_docente.qmd:492` · encabezado de nivel 2 · 181 palabras</sub>

La política de inteligencia artificial se resume en tres conceptos: la IA está permitida, debe ser declarada y es auditada. Los estudiantes pueden usar libremente asistentes para programar, depurar y redactar, con un uso crítico y responsable. A cambio hay una obligación: el registro completo de los prompts, no una selección, se entrega como apéndice del proyecto y de las entregas relevantes. Y ese registro se evalúa: se cruza con el código y con la memoria buscando coherencia entre lo que se preguntó y lo que se entregó. La transparencia se premia; un producto que excede con mucho lo que su registro explica es una señal de alerta.

Además, hay tres verificaciones que la inteligencia artificial no puede suplantar: la defensa oral individual, el diez por ciento de participación en el aula, que exige presencialidad, y el examen presencial, con su veinticinco por ciento y el mínimo de cinco. En lugar de prohibir una herramienta que muy probablemente van a usar en su trabajo, la asignatura permite usarla, exige declararla y comprueba en persona que el estudiante domina lo que entrega.

## 41. Experimentos aleatorios controlados: el patrón de referencia

<sub>`_parte2_docente.qmd:552` · encabezado de nivel 1 · 247 palabras</sub>

Finalizo la propuesta docente presntando brevemente el Tema 7, que empieza con una decisión de negocio: los alumnos están famliariazdos con el concepto de churn (o abandono) y su predicción (riesgo de abandono). En este tema comenzamos con una pregunta práctica: a quién dirigir una campaña de retención de clientes. 

Formulamos dos reglas de priorización: la regla RISK actúa sobre los clientes con mayor probabilidad de abandonar, un problema predictivo; la regla LIFT, sobre aquellos en los que la intervención produce una mayor reducción de esa probabilidad, un problema de inferencia causal.

El experimento de Ascarza, de 2018, permite compararlas: un operador de telefonía móvil de prepago asignó al azar a doce mil clientes inactivos un SMS con crédito adicional condicionado a una recarga, y observó si la línea seguía activa treinta días después. Se trata de un experimento aleatorio controlado.

Con los datos del mismo, la autora simula una campaña dirigida al cuarenta por ciento de los clientes con cada regla y observa el resultado en términos de disminución del abandono. Seleccionar por riesgo reduce el abandono en uno con nueve puntos; seleccionar por sensibilidad a la intervención lo reduce en seis: cuatro con uno puntos porcentuales de diferencia.

La lección: predecir el riesgo de abandono no responde por sí solo a la pregunta de gestión, a qué clientes nos dirigimos; para eso hay que estimar el efecto causal de la intervención. La pregunta que sigue es cómo estimar ese efecto sin experimento, con datos observacionales.

## 42. Aprendizaje automático para la estimación de efectos causales

<sub>`_parte2_docente.qmd:657` · encabezado de nivel 2 · 140 palabras</sub>

Traducimos el contexto a un modelo: el objetivo es estimar el efecto de la intervención $D$ sobre la respuesta (parámetro $\tau$): la respuesta y además depende de un conjunto de variables
X; asumimos que esa dependencia puede ser compleja, de ahí proponer una forma funcional flexible $g$. Además, es importante incidir que con datos observacionales los controles pueden confundir la relación, si la elección del tratamiento se ve afectada $X$ necesitamos incorporar el proceso a través de la función $m$.

El grafo visualiza el mecanismo generador de datos.

**El objetivo del tema es incorporar técnicas de aprendizaje máquina para la estimación de tau** ¿Por qué? Tres razones: elevada dimensionalidad de X  (p.e. inclusión de datos no tabulares como texto o imágenes); posible complejidad de $g$ o $m$ que podemos aproximar a través de modelos flexibles sin que tengamos que especificarlos.

## 43. Aplicación *naive* de métodos de aprendizaje automático

<sub>`_parte2_docente.qmd:756` · encabezado de nivel 2 · 168 palabras</sub>

El enfoque ingenuo tiene dos problemas, que son los que Double Machine Learning corrige. El procedimiento de la derecha parece razonable: aprender de los datos un modelo flexible para g, residualizar la respuesta restando esa predicción y recuperar tau con la regresión del residuo sobre el tratamiento.

El primer problema es el sesgo de regularización. Los modelos de aprendizaje automático regularizan los predictores, de forma explícita o implícita, y seleccionan las variables por su capacidad para predecir y. Un control poco correlacionado con y pero muy relevante para explicar el tratamiento puede quedar atenuado o fuera del modelo, y entonces la segunda etapa atribuye a tau parte de la relación de ese control con D: un sesgo de variable omitida. 

El segundo es el sesgo por sobreajuste: si entrenamos g y predecimos sobre las mismas observaciones, los residuos de y absorben parte del efecto causal y la varianza residual del tratamiento se distorsiona, de modo que la estimación de tau y su error estándar dejan de ser fiables.

## 44. Double (Debiased) Machine Learning

<sub>`_parte2_docente.qmd:793` · encabezado de nivel 2 · 194 palabras</sub>

Double Machine Learning es un estimador en dos etapas que permite corregir los sesgos de regularización y sobreajuste. 

En la primera etapa se entrenan dos funciones, g para la respuesta y m para el tratamiento, y se generan  versiones residualizadas de ambos (respuesta y tratamiento). El proceso separa las observaciones con las que se entrena de aquellas sobre las que se predice. 

En la segunda etapa se estima la regresión del residuo de y sobre el residuo de D: la pendiente es tau.

El esquema de la derecha ordena la lógica completa. De la aplicación
del enfoque ML ingenuo surgen dos problemas: el sesgo de regularización (omisión de predictores débiles de lam respuesta que son relevantes para el tratamiento) y el sesgo de sobreajuste (uso de los mismos datos para entrenar y para predecir). Cada uno tiene su solución: la ortogonalización o regresión de residuos sobre residuos o Frisch–Waugh–Lovell con modelos flexibles para el primero, y el cross-fitting, predicciones fuera de la muestra de entrenamiento, para el segundo. La combinación de ambas constituye Double Machine Learning: un estimador raíz de n consistente con inferencia válida.

Todo esto se pone en práctica con datos reales.

## 45. Práctica con datos reales

<sub>`_parte2_docente.qmd:956` · encabezado de nivel 2 · 159 palabras</sub>

La práctica del Tema 7 tiene un flujo de trabajo simple para los estudiantes ya familiarizados con Python+scikit-learn.

La práctica (a quién enviar una campaña de emailing) parte de datos públicos (Hillstrom): sesenta y cuatro mil clientes asignados al azar a un email de productos de hombre, un email de productos de mujer o un control sin email, con visitas, compras y gasto observados durante dos semanas. Los estudiantes estiman el efecto promedio de la intervención y comparan dos reglas de priorización, por probabilidad de respuesta positiva o por efecto estimado de la campaña, las reglas del caso de Ascarza con otros datos. En la etapa final introducimos selección observacional en la asignación y validamos DoubleML frente al resultado experimental, que aquí conocemos.

La salida es la que pide el objetivo del tema: los modelos de primera etapa se evalúan con validación cruzada, y dml devuelve el efecto estimado, su intervalo de confianza y la sensibilidad a confusión residual.

## 46. Nivel y alcance del Tema 7

<sub>`_parte2_docente.qmd:991` · encabezado de nivel 2 · 120 palabras</sub>

Cierro con el nivel y el alcance del Tema 7, porque conviene ser explícito sobre qué se pide a estudiantes de tercero de grado. El límite: no se evalúan demostraciones asintóticas ni el desarrollo formal de la ortogonalidad de Neyman. 

Lo que sí se evalúa: distinguir predicción e intervención; reconocer los dos sesgos mediante simulación; aplicar ortogonalización y cross-fitting; estimar un efecto y leer su intervalo de confianza; y discutir supuestos y límites.

Ese nivel es coherente con todo lo anterior: el de una asignatura forma profesionales capaces de usar métodos computacionales y modelos predictivos en economía y negocios tanto para predecir como para explicar, con práctica sobre datos reales, trabajo reproducible y un uso crítico de la inteligencia artificial.

---

# Parte 3 de 3 · Propuesta investigadora

Fuente: `external/jcr_presentation/propuesta_investigacion.qmd` (proyecto hermano `2026_jcr`) · copia sincronizada en `_parte3_investigacion.qmd`.

## 47. Esquema

<sub>`_parte3_investigacion.qmd:12` · encabezado de nivel 2 · 177 palabras</sub>

Presento la propuesta de investigación *Creative Collaborations*, un trabajo conjunto con Manuel Cuadrado-García y María Luisa Palma-Martos que estudia la formación de colaboraciones entre artistas en la música grabada. La pregunta que organiza toda la exposición es fácil de formular: entre todas las parejas de artistas que podrían colaborar, ¿por qué unas llegan a hacerlo y otras no?

La exposición sigue seis bloques. Empiezo por la motivación, la pregunta, el marco conceptual y la contribución de este trabajo. Después presento los datos y, en particular, cómo medimos la proximidad estética entre dos artistas y cómo describimos la red de colaboraciones previa. El tercer bloque es el núcleo empírico: el diseño del conjunto de riesgo, la estrategia de estimación y el resultado sobre la forma de la relación entre similitud estética y colaboración. El cuarto pasa de la asociación dentro de muestra a la capacidad de ordenar colaboraciones en un año que el modelo no ha visto. El quinto resume las comprobaciones para calibrar la sensibilidad de los hallazgos y el último recoge resultados, límites y líneas futuras.

## 48. ¿Se ha convertido la música en un deporte de equipo?

<sub>`_parte3_investigacion.qmd:26` · encabezado de nivel 2 · 222 palabras</sub>

A comienzos de los setenta, menos del 3% de las entradas anuales del Billboard Hot 100 correspondían a colaboraciones. Entre 2016 y 2020 esa misma tasa asciende al 40%: casi dos de cada cinco. La colaboración pasa de ser una anomalía entre los grandes éxitos a una práctica habitual en la producción cultural. Lo que se observa es un cambio de régimen que emerge en paralelo a la digitalización de la música y que se asienta en un nuevo equilibrio (elevada tasa de colaboración presente en los éxitos) con la implantación de un modelo de negocio en la industria basado en el acceso, no en la propiedad (el streaming).

El interés económico del fenómeno va más allá de la suma de créditos en una producción cultural: supone investigar los incentivos que llevan a combinar temporalmente competencias o recursos físico y simbólicos (identidades estéticas), reputación y acceso a públicos. Por limitaciones de tiempo, soslayaré el sustrato teórico que subyace al ejercicio 
empírico de esta propuesta.


No obstante introduzco un apunte: en la creación de equipos creativos, orientados a la producción cultural o en la academia (equipos científicos) existe una tensión entre similitud entre los participantes (que puede facilitar coordinación o compatibilidad) y la distancia (que puede aportar novedad y complementariedad). Y este es uno de los aspectos centrales que estudiamos en esta propuesta.

## 49. Proximidad estética: un aspecto recurrente en la literatura

<sub>`_parte3_investigacion.qmd:56` · encabezado de nivel 1 · 334 palabras</sub>

Para hacer contrastable esa pregunta hay que fijar la unidad de análisis. Trabajamos con pares de artistas activos en un mismo año en las listas globales de Spotify, y el evento es su primera colaboración como artista principal y artista invitado (lead y feature). No preguntamos cuántas colaboraciones acumula un artista, sino qué distingue a las parejas que forman una por primera vez de las muchas que podrían haberlo hecho y no lo hicieron.

Entendemos esa formación como un emparejamiento en el que intervienen varias dimensiones a la vez. 

1. La primera es la estética: cuánto se parecen dos artistas en un espacio que generamos a partir de la percepción que la audiencia tiene de su producción anterior. 

2. La segunda agrupa la proximidad cultural, territorial e institucional: compartir escena lingüística, coincidir en el país registrado, haber pasado por los mismos sellos pueden ayudar a formar el emparejamiento.
 
3. La tercera recoge actividad y trayectoria profesional: el nivel de experiencia de los dos, lo simétrico que es el par y el tiempo que llevan expuestos a una oportunidad conjunta. 

4. La cuarta es la topología de la red previa de colaboraciones: socios compartidos, centralidad, alcanzabilidad y distancia entre ambos en esa red.

La estética es la dimensión focal porque sobre ella hay dos hipótesis en competencia con implicaciones observables distintas.  
- Por un lado la existencia de una distancia estética óptima (la compatibilidad facilita el trabajo conjunto y la diferencia aporta novedad) lleva a la propensión a colaborar a crecer con la similitud para disminuir después. 
- Si lo que opera es un umbral de compatibilidad, la distancia estética es una barrera que, alcanzado suficiente terreno común, se inactiva. La proximidad  
excesiva no se penaliza.

Las demás dimensiones entran simultáneamente en el modelo y condicionan la interpretación que hagamos de la compatibilidad estética. En todos los casos estimamos asociaciones condicionales, no mecanismos causales.

Este planteamiento obliga a separar dos preguntas que la literatura suele tratar por vías distintas: formación y beneficios de las colaboraciones.

## 50. Marco conceptual

<sub>`_parte3_investigacion.qmd:100` · encabezado de nivel 2 · 343 palabras</sub>

Aquí convergen dos literaturas. La primera estudia las consecuencias de colaborar, y en música la evidencia es clara: los *featurings* elevan la demanda de *streaming*, resultado central de McKenzie y coautores, y los duetos sobreviven más tiempo en las listas, como documentan Kaimann y coautores. 

La segunda estudia la formación del vínculo. Rivera, Soderstrom y Uzzi ordenan los mecanismos de formación de díadas en tres familias: asortativos, basados en la similitud; relacionales, basados en lazos previos, socios comunes y posición en la red; y de proximidad geográfica e institucional. Gulati y Gargiulo añaden que las redes se reproducen a sí mismas, porque los lazos previos generan la información y la confianza que hacen más probables los nuevos. Nuestros bloques de predictores son la traducción de esas tres familias.

La tensión entre parecidos y complementarios tiene también una larga tradición. Mitsuhashi y Greve distinguen compatibilidad (rasgos similares que facilitan el trabajo conjunto) de complementariedad (recursos distintos que crean valor al combinarse). La resolución habitual es un óptimo interior: Nooteboom y coautores lo formalizan como distancia cognitiva óptima; Uzzi y coautores muestran que la ciencia de mayor impacto combina una base convencional con elementos atípicos; y Smith y coautores lo estiman en la formación de equipos científicos, con una U invertida en el solapamiento temático.

En música, en cambio, la evidencia sobre distancia óptima es sobre resultados. Askin y Mauskapf muestran que la diferenciación óptima de una canción predice su éxito en listas, y Ordanini, Nunes y Nanni, que emparejar artistas de géneros distintos amplía la audiencia. Eso habla de qué funciona una vez existe la colaboración, no de qué parejas se seleccionan. Los pocos trabajos que estudian la formación en música se ciñen a una escena o un género, sin medida explícita de similitud y no estiman sobre la población completa de pares en riesgo. Esa es la brecha que cubre este trabajo: contrastar la forma de la relación estética sin presuponerla, integrada con las demás dimensiones de proximidad y con la topología de la red.
La contribución consiste en hacer esa integración operativa.

## 51. Afinidad estética y emparejamiento multidimensional

<sub>`_parte3_investigacion.qmd:122` · encabezado de nivel 2 · 221 palabras</sub>

La contribución se apoya en cuatro elementos. El primero es la integración: un único modelo combina la homofilia estética, cultural, territorial e institucional y por actividad y la estructura de la red previa, de modo que la forma de la relación estética se estima manteniendo constantes las demás proximidades y oportunidades.

El segundo es la medición. Representamos a cada artista con un vector de etiquetas generadas por los usuarios de dos redes sociales en música. Las etiquetas en $t$ se refieren a lanzamientos de un artista previos a $t$ lo que impide que la colaboración que queremos predecir entre mecánicamente como predictor a través de las etiquetas que ella misma genera. 

El tercero es el contraste para medir la proximidad estética. Combinamos especificaciones alternativas: además de la cuadrática se implementa un test de forma prespecificado, con *spline* y reversión de signo, que pregunta si el máximo interior que aparece en este diseño procede de los datos o de la función impuesta. 

El cuarto es el diseño y la validación: el evento es la primera colaboración principal–invitado, estimamos sobre el conjunto de riesgo completo sin muestrear negativos, la inferencia admite dependencia entre díadas que comparten artista y descomponemos la aportación de cada bloque dentro y fuera de muestra.

Para ello necesitamos combinar fuentes que midan tres cosas distintas: resultados, percepciones y relaciones.

## 52. Por qué etiquetas y no géneros de plataforma

<sub>`_parte3_investigacion.qmd:172` · encabezado de nivel 1 · 246 palabras</sub>

Combinamos tres fuentes. La primera son las listas globales semanales de Spotify, de septiembre de 2013 a diciembre de 2025, con los metadatos de pista, álbum y artista del API Web de Spotify. Las listas nos dan el registro de colaboraciones con el detalle de créditos que necesitamos: quién es el artista principal (lead) y quién el invitado (feature) en cada pista. Tras limpiar y deduplicar nos quedamos con 12.688 combinaciones pista–artista y 2.878 artistas en el ámbito del estudio.

La segunda son las etiquetas que los usuarios asignan en Last.fm y MusicBrainz, fechadas por lanzamiento: 794.309 filas de etiquetas para 2.402 artistas, que cubre el 83,5% del ámbito. Aquí conviene justificar una elección. Spotify tiene su propia clasificación de géneros, pero solo cubre 981 de los 2.878 artistas, aproximadamente un tercio, y refleja categorías seleccionadas por la plataforma. Las etiquetas cubren más del doble y, sobre todo, recogen cómo describe la audiencia a cada artista: géneros y subgéneros, pero también estilos, estados de ánimo y otras percepciones. Para medir la posición estética desde el punto de vista del público es la fuente adecuada.

La tercera son los metadatos de MusicBrainz: tipo de entidad, país, género cuando el artista es una persona y año del primer lanzamiento. A ellos se añade el historial de sellos, construido con los créditos de álbum observados en las listas hasta el año anterior.

La cuestión decisiva es cómo convertir esas etiquetas en una medida de proximidad coherente en el tiempo.

## 53. Proximidad estética

<sub>`_parte3_investigacion.qmd:193` · encabezado de nivel 2 · 205 palabras</sub>

Cada artista es un vector en el espacio de etiquetas. Su perfil en el año t acumula las etiquetas de todos sus lanzamientos fechados estrictamente antes de t, de modo que el perfil es acumulativo y está retardado por construcción. La proximidad de un par es la similitud coseno entre los dos vectores retardados: el ángulo entre los dos artistas en el espacio estético que define la audiencia.

La figura muerstra una proyección ilustrativa a dos dimensiones, si bien las medidas de similaridad son reales. Bad Bunny y J Balvin comparten buena parte del vocabulario con que se les describe y su coseno es 0,82; Bad Bunny y Ed Sheeran apenas comparten etiquetas y el coseno es 0,07.

Una observación sobre la cobertura: la proporción de pares con similitud observada cae del 93% en 2015 al 67% en 2024, porque los artistas que van entrando en las listas llegan con historiales de etiquetas más delgados. A este respecto, cuando un par carece de medida de proximidad estética  permanece en el modelo con un indicador de ausencia y el tramo cero.

Junto a esta proximidad sustantiva hay otra distinta, que no se mide en etiquetas sino en la red: la cercanía heredada de las colaboraciones anteriores.

## 54. La red previa amplía las oportunidades relacionales

<sub>`_parte3_investigacion.qmd:232` · encabezado de nivel 2 · 189 palabras</sub>

La red de colaboraciones cumulativa se densifica a lo largo de la década. Los artistas activos pasan de 327 en 2015 a 1.033 en 2024, el grado medio sube de 1,63 a 6,22 y la proporción de artistas sin ningún lazo previo cae del 33,3% al 16,1%. Las cifras describen la red de cada año; la figura muestra la red acumulada, sin aislados, con la misma disposición de nodos en los dos años para que se aprecie la consolidación.

El estado de la red en el año anterior no es solo un descriptivo: es el objeto sobre el que condicionamos. Para cada par de artistas en riesgo de colaborar en t calculamos, para la red acumulada hasta t-1, medidas de centralidad y posición en el grafo como número de socios comunes, si están conectados por algún camino, a qué distancia y qué posición ocupa cada artista. 

Con estas variables podemos preguntar si la historia estructural aporta información propia una vez observamos estética, cultura, instituciones y actividad. En este caso hablamos de oportunidad relacional observada, esto es, de que dos artistas cercanos en la red tienen mayor propensión a colaborar.

## 55. Composición de la red

<sub>`_parte3_investigacion.qmd:272` · encabezado de nivel 2 · 137 palabras</sub>

La composición visual de esa red ayuda a entender por qué cultura y topología deben medirse por separado.

Esta figura cumple una función ilustrativa. Es el subgrafo de mayor grado de la red acumulada hasta 2024, para el 5% superior de la distribución de la centralidad. Lo que se ve es que el núcleo denso lo ocupan dos escenas, la latina y la anglófona, con un número reducido de artistas puente entre ambas.

La imagen sugiere que la estructura relacional tiene una segmentación cultural, lo que justifica una decisión de medición. En concreto la existencia de conexiones parece emerger tanto por proximidad (estéticam cultural o geográfica) como por la ubicación en el grafo, p.e. el caso de conexiones que se cierran por vecinos compartidos o la existencia de intermediarios (o brokers) que actúan de puente entre escenas.

## 56. Definición de la respuesta a modelizar

<sub>`_parte3_investigacion.qmd:294` · encabezado de nivel 1 · 207 palabras</sub>

Decidir qué cuenta como colaboración implica definir el estimando, una decisión que no es inocua. En nuestro caso tratamos de evitar mezclar dos cosas distintas: la formación de una conexión nueva y la repetición de un vínculo que ya existía. Modelizarlas juntas es modelizar procesos distintos como si fueran uno.

Además, en las colaboraciones de más de dos artistas, evitamos contabilizar como vínculos la asociación de aquellos que son invitados (featuring), aunque tampoco los contamos como negativos.

Nuestra defición de riesgo es sensible al rol: la respuesta es positiva si el par colabora en el año t cuando uno es el principal (lead) y el otro el invitado (featuring) en una pista que entra en listas. Si el evento es de formación se exige además que no hubiera ningún lazo previo entre ambos, de ningún tipo. Las repeticiones se estudian aparte. 

El resultado agregado, que suma primeras y repetidas, tiene 1.811 eventos frente a los 1.064 de formación.

Añadir que en cualquier caso estamos ante  un evento muy raro: en el caso de formación encontramos 26,9 por cada 100.000 pares-año, con intervalo del 95% entre 25,3 y 28,5. Esa rareza condiciona el diseño y la inferencia.

Con el evento definido, construimos el conjunto completo de oportunidades plausibles.

## 57. Diseño: conjunto de riesgo y resultado

<sub>`_parte3_investigacion.qmd:320` · encabezado de nivel 2 · 201 palabras</sub>

Estimamos sobre el conjunto de riesgo completo: todos los pares no ordenados en riesgo en cada año, sin muestrear negativos. La ventaja es interpretativa: los coeficientes describen cómo se distinguen las colaboraciones realizadas de la población de pares que podían haber colaborado y no lo hicieron, sin las correcciones que exige un diseño caso–control (selección de una muestra de casos y otra de controles en proporciones que no necesariamente representan su frecuencia real en la población).

Lo decisivo es quién está en riesgo. Un par pertenece al conjunto de riesgo en t si la colaboración era una posibilidad realista: los dos artistas debutaron en listas antes de t y cada uno publicó una pista que entró en listas en los tres años previos. La ventana de tres años excluye ceros poco plausibles.  No obstante usamos una ventana de cinco años y sin salida como análisis de sensibilidad.

El panel de estimación tiene 3.756.411 díadas-año, 1.064 eventos de formación y 2.256 artistas entre 2015 y 2024. El año 2025 queda fuera de la estimación porque, cuando recogimos los datos, las listas de finales de 2025 podían seguir acumulando apariciones.

Sobre este mismo diseño combinamos un modelo explicativo y una referencia predictiva flexible.

## 58. ¿Por qué no un ERGM?

<sub>`_parte3_investigacion.qmd:355` · encabezado de nivel 1 · 319 palabras</sub>

Usamos dos herramientas con roles distintos. El logit es el modelo explicativo: modeliza la probabilidad de formación condicionada a la red del año anterior y a las características retardadas del par, con un índice lineal y efectos fijos de año, y permite hacer inferencia sobre una forma que se declara explícitamente. 

XGBoost, un conjunto de árboles potenciados, nos sirve de referencia predictiva: captura interacciones y no linealidades sin necesidad de especificarlas y nos permite cuantificar la señal predictiva para bloque de variables  de factores cuando no imponemos forma funcional. Se trata de una referencia flexible.

En el caso del ejercicio predictivo los dos modelos se reestiman para el periodo 2015–2023 y se puntúan una sola vez en 2024. El logit no tiene ningún ajuste. En XGBoost los hiperparámetros se fijaron de antemano, y la única elección basada en datos, el número de rondas o árboles que se añaden al ensamble, que se decide con parada temprana entrenando hasta 2022 y validando en 2023.

La inferencia del logit usa los errores estándar diádicos de Aronow y Samii, que admiten dependencia arbitraria entre dos díadas que comparten un artista.

Un último apunte metodológico. A pesar de que los modelos exponenciales de grafos aleatorios podrían parecer una opción natural para modelizar datos relacionales, existen dos razones que justifican la elección de modelos de clasificación. 

La primera es de escala: con 2.256 actores y millones de díadas, la constante de normalización es intratable y la estimación tiende a degenerar. En la práctica la estimación no sería viable.

La segunda es el tipo de pregunta que responde: un ERGM modeliza la distribución conjunta de la red; el objetivo del trabajo que presento es modelizar la probabilidad condicional de cada díada dada la red previa.

Nuestra elección exige evaluar a posteriori si la hipótesis de independencia condicional entre las observaciones díadicas resulta razonable una vez considerados los predictores y el estado previo de la red.

## 59. Especificaciones: proximidades y modelos anidados

<sub>`_parte3_investigacion.qmd:392` · encabezado de nivel 2 · 243 palabras</sub>

La comparación entre modelos exige asignar cada variable a una dimensión sustantiva concreta.


Estadísticamente trabajamos con cuatro bloques y 32 variables, además de los efectos de año; la tabla los resume. 

1. El bloque de red tiene ocho términos: vecinos comunes, índices de Jaccard y Adamic–Adar, conexión preferente, alcanzabilidad, proximidad geodésica y grado (en media y en diferencia). 

2. El bloque estético incorpora la proximidad estética (sim del coseno) y su cuadrado; la posición respecto al centroide anual y la entropía de etiquetas, que describen tipicidad y la amplitud (artista tiene similitudes relevantes con muchos, entropía alta, o pocos artistas) de su identidad estética; y el tamaño del vocabulario y los indicadores de ausencia, que controlan la cobertura. 

3. El bloque de actividad tiene siete: pistas acumuladas en listas y longitud de carrera, en media y diferencia, más la duración de la elegibilidad conjunta en tramos, que controla el tiempo de exposición. 

4. Finalmente el bloque de otras proximidades y atributos tiene otros siete: escena lingüística, país registrado, tipo de artista, género cuando ambos son personas y tres medidas retardadas de historial común de sellos.

Observación: las variables de nodo entran como media del par, que mide nivel, y como diferencia absoluta, que mide asimetría, de modo que el resultado no dependa del orden arbitrario de los artistas dentro del par.

Estimamos tres modelos anidados:  Completo, con los cuatro bloques; Solo red, con la topología; y Sin red, con estética, actividad y atributos.

## 60. ¿Optimo interior?

<sub>`_parte3_investigacion.qmd:429` · encabezado de nivel 2 · 208 palabras</sub>

La especificación cuadrática, que es  habitual en la literatura y  usamos en nuestras estimaciones, impone un máximo por construcción. Pero encontrar un máximo no acredita que exista una relación de U-invertida como la postulada.

Para reforzar la evidencia recurrimos a tres estrategias: 
1. La primera, consiste en discretizar la métrica de similitud estética y analizar las tasas de formación observadas por tramo (e intervalos), sin ningún ajuste funcional. 
2. La segunda es ajustar un *spline* cúbico que da la curva flexible del perfil. 
3. La tercera es un test confirmatorio de reversión de signo, basado en el enfoque de dos líneas de Simonsohn, con dos submuestras: en una se localiza el punto de ruptura como máximo del *spline*; en la otra se estima la pendiente posterior, con datos que no se usaron para localizarlo. Solo confirma un óptimo interior si la pendiente cambia de positiva a negativa.

Evaluamos las propiedades de este último  por simulación, con paneles calibrados al número de eventos y a la distribución de similitud de nuestra muestra. Para 200 replicas, cuando el perfil verdadero crece y se aplana, el test confirma falsamente un óptimo interior en el 0,5% de los casos; frente a un óptimo interior lo detecta en el 79% de las simulaciones.

## 61. Resultado base: especificación cuadrática

<sub>`_parte3_investigacion.qmd:492` · encabezado de nivel 2 · 254 palabras</sub>

Comenzamos analizando los resultados de la estimación base.

[Zoom: bloque de red.] El bloque de red es conjuntamente informativo (contraste conjunto del bloque rechaza el modelo restringido) y proximidad y centralidad se asocian a la formación de 
colaboraciones. La proximidad geodésica muestra como los pares que ya estaban cerca en la red previa tienen una propensión mucho mayor a conectar directamente. El grado medio también es positivo, en línea con un mecanismo de visibilidad si bien la asimetría en la centralidad se asocia a una menor probabilidad de vínculo. 

[Zoom: estética y escena.] La forma cuadrática en la proximidad estética reproduce el patrón conocido: término lineal positivo y cuadrático negativo que sitúan un máximo en una similitud de 0.637. No obstante, por ubicación,  en el percentil 94.8 del soporte,  la región cuenta con pocos pares y eventos: la estimación apunta a una relación no lineal y cóncava, pero no es concluyente respecto a una caída. 

[Zoom: actividad, país y sellos.] Compartir la escena  presenta una asociación positiva y precisa, y una actividad media mayor en listas se asocia positivamente con la formación y una mayor diferencia de actividad, negativamente, de modo que pares activos con niveles de actividad similares se asocian a una mayor propensión a colaborar. El solapamiento de carreras en listas (las variables elegibilidad conjunta) muestran coeficientes negativos y crecientes: los pares que llevan años coexistiendo sin colaborar tienen cada vez menos probabilidad de hacerlo.


Importante recordar que son asociaciones condicionales y las escalas de los coeficientes no son comparables entre variables.

## 62. Lectura crítica del óptimo interior

<sub>`_parte3_investigacion.qmd:529` · encabezado de nivel 2 · 169 palabras</sub>

Revisamos la supervivencia del óptimo interior a modificaciones de la muestra utilizada en su estimación. La pregunta que nos hacemos es si ese máximo es una rasgo del comportamiento de los agentes a la hora de formar vínculos o un artefacto de la especificación. 

Para responderla cruzamos dos decisiones del diseño: 
1. La definición de la respuesta, todos los pares o solo pares artista principal–artista invitado
2. El conjunto de riesgo: consideramos una ventana de tres años para determinar si un artista está activo (deforma que si no produce un hit en esos tres años, sale del conjunto de riesgo) o sin salida (una vez se alcanzan llega a listas, se permanece en el conjunto de riesgo).

La reestimación del modelo bajo estos cuatro supuestos proporciona un resultado: **la forma cuadrática sobrevive a los cambios de muestra**. El máximo implícito se queda entre 0,63 y 0,70 en las cuatro celdas, con cualquier conjunto de riesgo y cualquier proyección, aunque siempre en la cola alta de la distribución de similitud.

## 63. La asociación estética crece y se aplana dentro del soporte

<sub>`_parte3_investigacion.qmd:572` · encabezado de nivel 2 · 235 palabras</sub>

Ya que la ubicación del óptimo interior en la cola superior de la distribución es compatible no solo con una reversión del efecto en la proximidad estética, sino con una saturación del mismo analizamos la relación postulada con especificaciones flexibles (que no presuponen una forma determinada). 

La figura siguiente muestra directamente la forma que sí respaldan los datos. La curva es el *spline* prespecificado sobre el modelo Completo y los puntos son las tasas de colaboración observadas para la discretización de la variable similitud del coseno. Ambas apuntan en la misma dirección: la tasa de formación sube con fuerza desde similitudes bajas hasta aproximadamente 0,3 o 0,4 para aplanarse después. Ningún tramo dentro del soporte tiene una tasa inferior a los anteriores, el *spline* no se gira hacia abajo en ningún punto del rango respaldado y los dos tramos más altos, con pocas observaciones de comparación, quedan por encima de las tasas intermedias, no por debajo.

Además, un test confirmatorio utiliza la mitad de la muestra para detectar un punto de ruptura (un máximo para la tasa de colaboración) en la distribución de la variable de similitud y ajusta dos rectas, antes y después de éste con el otro 50% de la muestra. El test confirma la subida anterior está confirmada pero no una caída posterior. El remuestreo muestra valores positivos con intervalos que incluyen cerolo que apoya un crecimiento y aplanamiento, sin reversión confirmada.

## 64. Lectura · **[reserva: slide en `.content-hidden`]**

<sub>`_parte3_investigacion.qmd:606` · encabezado de nivel 2 · 185 palabras</sub>

¿Cambia la curvatura según el tipo de par? Lo examinamos de forma exploratoria con dos moderadores, tomados de cuatro estratos prespecificados, interactuando los términos cuadráticos con cada uno. La interacción con país registrado común alcanza significación convencional, chi cuadrado de 8,88 con dos grados de libertad y p de 0,012; la interacción con el nivel de actividad del par no, p de 0,63.

Conviene leer bien lo que significa. No convierte al país en un efecto simple: su coeficiente medio en el modelo Completo es impreciso. Lo que cambia descriptivamente es la curvatura del resumen cuadrático. La concavidad se concentra entre los pares sin país común, donde el máximo implícito está en 0,557; entre los pares con país común el perfil es prácticamente creciente hasta el borde del soporte, 0,83. Es un resultado exploratorio: no observamos distancia, residencia, públicos ni idioma individual, así que no identificamos un mecanismo cultural, geográfico ni de expansión de audiencias, y el ejercicio no se corrige por multiplicidad.

Pasamos ahora de la asociación dentro de muestra a cuánto ordenan los bloques en un año que el modelo no ha visto.

## 65. Capacidad predictiva por bloques

<sub>`_parte3_investigacion.qmd:636` · encabezado de nivel 2 · 282 palabras</sub>

El ejercicio predictivo utiliza un protocolo estricto. Los dos modelos (logit y xgbm) se reestiman con datos 2015–2023 y se puntúan una sola vez en 2024, de modo que el modelo evaluado nunca ha visto el año de evaluación; XGBoost elige su número de árboles entrenando hasta 2022 y validando en 2023. En 2024 hay 64 eventos de formación de 490.000 (logit) o 526.000 díadas (xgbm) puntuadas según el modelo, una tasa base de 0,12 a 0,13 por mil. La diferencia es que el logit se entrena para el conjunto de casos completos y XGBoost para todos los pares, gracias al tratamiento nativo de los valores ausentes.

El AUC-PR del mejor modelo multiplica la tasa base por unas 18 veces en el logit y unas 14 en XGBoost. El *lift* en los 500 primeros mira el extremo del ranking y es inestable con tan pocos positivos, por eso añadimos las métricas a 10.000 primeros, donde el Completo recupera el 42% de los eventos con logit y el 31% con XGBoost. Conviene no comparar el  *lift* entre modelos por la  diferencia en la muestra de entrenamiento.

Un análisis de la capacidad explicativa dentro de la muestra de entrenamiento para los diferentes grupos de variables (test de wald sobre para modelo restringido en la especificación logit) es concluyente y apoya el modelo no restringindo. Fuera de muestra sin embargo la aportación del bloque de predictores de red es limitada. Por el contrario, quitar el bloque no-red tiene mayor coste, lo que sugiere que los bloques estética, actividad, cultura, instituciones y demás atributos contienen la mayor parte de la señal predictiva observable; la red es informativa dentro de muestra, pero al horizonte anual añade poco.

## 66. Constraste no paramétrico de la forma funcional

<sub>`_parte3_investigacion.qmd:677` · encabezado de nivel 2 · 137 palabras</sub>

Una utilidad adicional de XGBoost es que nos permite comprobar la forma del perfil estético sin imponer ninguna forma funcional.

Para ello recurrimos a la atribución de las predicciones locales a los distintos predictores del modelo que porprociona los valores de shapley. El gráfico de dependencia muestra para cada par-año cuánto aporta la similitud estética a la puntuación (contribuciones al *score*, en escala de log-odds, no probabilidades parciales). Los valores se muestran para la el conjunto de dartos de prueba (2024).

El patrón reafirma el hallazgo del ejercicio de discretización y el *spline*: la contribución sube con fuerza por debajo de una similitud de 0,3, se aplana desde aproximadamente 0,4 y no muestra un declive claro en la parte alta. 

Es importante señalar que este resultado se obtiene de un modelo que no impone ninguna forma funcional.

## 67. Comprobaciones de los resultados

<sub>`_parte3_investigacion.qmd:706` · encabezado de nivel 2 · 245 palabras</sub>

Esta tabla resume muestra distintas  comprobaciones. Todas son análisis descriptivos o de sensibilidad. Las presento brevemente.

La primera familia es la inferencia. El *bootstrap* de nodos, que remuestrea artistas y arrastra también la composición del conjunto de riesgo, es más conservador: aumenta los errores estándar con una ratio mediana de 1,60. Bajo ese criterio los términos estéticos, la geodésica, el grado, la escena y el tipo se mantienen; el historial común de sello deja de distinguirse de cero, y por eso lo leemos como positivo pero impreciso. 

La segunda es la definición del resultado. Restringir los eventos a pistas de exactamente dos artistas (elección bilateral), deja 609 eventos y un perfil esencialmente igual; ponderar por tamaño de equipo o devolver los pares invitado–invitado como clase negativa tampoco lo cambia, y los bloques de red, actividad y atributos se mueven como máximo 0,37, 0,13 y 0,05 en cada variante. 

La tercera es la ventana del conjunto de riesgo: con cero, tres y cinco años los máximos implícitos son 0,635, 0,637 y 0,630.

La cuarta es la medición de etiquetas: solo MusicBrainz, vectores binarios, vocabularios mínimos de tres y de cinco etiquetas, submuestra bien medida y terciles de cobertura. El perfil sobrevive en todas, los demás bloques se mueven como máximo 0,26 y las interacciones con la cobertura no son conjuntamente significativas, p de 0,082.

La corrección de Firth, el enlace cloglog y la inclusión de efectos de artista con un logit condicional se discuten a continuación.

## 68. Corrección de sesgo de Firth

<sub>`_parte3_investigacion.qmd:770` · encabezado de nivel 2 · 188 palabras</sub>

Dada la baja frecuencia del evento analizado, estimamos dos modelos alternativos. En primer lugar, empleamos la corrección de Firth, basada en una verosimilitud penalizada, para reducir el sesgo de las estimaciones y mitigar posibles problemas de separación. En segundo lugar, estimamos un modelo con enlace log-log complementario (cloglog), cuya forma asimétrica resulta apropiada cuando la respuesta registra la ocurrencia de un evento generado por un proceso en tiempo continuo.

[Zoom: columna Δ Firth–logit.] Los dos términos focales de similitud cambian como máximo 0,014. El mayor desplazamiento de toda la tabla es 0,176, en el Jaccard de vecindarios, que equivale a aproximadamente 0,23 de su error estándar. Los coeficientes culturales e institucionales son igual de estables. El cloglog conserva el mismo patrón de signos, aunque está en otra escala de enlace y sus magnitudes no se comparan directamente con las del logit. Tampoco hay señales de separación: la estimación converge y ninguna observación tiene una probabilidad ajustada superior a un medio.

El alcance es el que es: una auditoría de coeficientes. Queda pendiente recalcular errores estándar  así que el ejercicio  muestra que las estimaciones puntuales no dependen del estimador.

## 69. Logit condicional

<sub>`_parte3_investigacion.qmd:829` · encabezado de nivel 2 · 252 palabras</sub>

Los modelos anteriores solo controlan las diferencias entre artistas mediante variables observadas. Para absorber las características no observables de los artistas principales, aplicamos un diseño de elección emparejada: para cada artista principal con al menos una colaboración en un año, comparamos los colaboradores elegidos con todos los candidatos elegibles. El estrato artista-año absorbe toda característica constante del artista ese año, como su calidad latente, visibilidad o actividad.

El análisis comprende 641 estratos, 545.149 pares-año y 1.064 eventos. Las variables de red no se incluyen porque la posición del artista principal es fija dentro de cada estrato. Aunque es el control más fuerte frente a la heterogeneidad no observada, solo incluye artistas con alguna colaboración; por ello, los coeficientes se interpretan por su dirección, no por su magnitud respecto a los modelos anteriores.

[Zoom: similitud, escena, país y sello.] La dirección y la curvatura estéticas se mantienen cerca de los valores base. Las proximidades cultural e institucional aparecen incluso mayores. Parte de esa diferencia tiene explicación: dentro del conjunto de oportunidades de un principal, el país y el sello ya no compiten con la posición del propio principal en la red, que en el modelo base absorbía parte de la asociación geográfica.

Lo que este ejercicio nos dice es que los resultados de proximidad no son un artefacto de la heterogeneidad no observada de artistas principales: dentro de cada principal, los socios más cercanos estética, cultural e institucionalmente son elegidos con más frecuencia.

Con la evidencia principal y sus comprobaciones, sintetizo qué aprendemos.

## 70. La formación es multidimensional

<sub>`_parte3_investigacion.qmd:862` · encabezado de nivel 2 · 290 palabras</sub>

Cuatro resultados. El primero es la hipótesis focal: dentro del soporte común, la proximidad estética tiene una asociación positiva que se aplana. Es importante señalar que la partición prespecificada localiza el cambio alrededor de 0.68, la subida está confirmada y la caída no: no hay evidencia de declive en ningún punto del soporte observado. Eso es coherente con un umbral de compatibilidad: la poca similitud es una barrera para trabajar juntos pero los datos no respaldan una penalización por compatibilidad excesiva entre los pares que observamos.

El segundo son la relevancia de otras medidas de proximidad. La cultural importa, pero en forma de escena compartida más que de país. La institucional, el historial común de sello, es positiva pero menos robusta. Y en actividad, los pares más activos y más equilibrados colaboran más, mientras que la proximidad de carrera no da un resultado claro.

El tercero es la topología. El bloque de red es claramente informativo dentro de muestra, pero en el ejercicio predictivo (para el año de prueba) añade poca mejora marginal a las características no-red, con intervalos que incluyen cero. Este hallazgo sugiere que los estadísticos son el resultado de un proceso de preferencias y oportunidades que las características observables ya capturan y no variables explicativas originales.

El cuarto es metodológico: en este diseño, el máximo interior aparece al imponer una cuadrática y no se reproduce con las formas flexibles. Formación y éxito son preguntas distintas, y la forma debe contrastarse sin imponerla.

En conjunto, la colaboración emerge de varias proximidades y oportunidades que operan juntas: la estética funciona como condición de compatibilidad dentro del soporte observado; cultura, instituciones, actividad y red estructuran qué emparejamientos llegan a materializarse. 

Este balance exige declarar también dónde no alcanza la evidencia.

## 71. Limitaciones y extensiones

<sub>`_parte3_investigacion.qmd:894` · encabezado de nivel 2 · 309 palabras</sub>

Las limitaciones son de diferentes tipos. Primera, las estimaciones son asociaciones condicionales a la red retardada, no efectos causales. Segunda, las medidas son parciales: las etiquetas o la escena incorporan ruido en su construcción y el historial de sellos no agota los canales institucionales. Tercera, la cola alta está poco poblada: hay ocho eventos por encima de una similitud de 0,90, así que no es posible descartar una penalización por falta de coplementariedad para la similitud extrema. Cuarta, población y resultado están condicionados: estudiamos artistas activos en listas globales con metadatos, no se modeliza el llegar las listas no se modela y la colaboración fuera de listas se incorpora parcialmente. 

En lo que respecta a extensiones existe un diagnóstico de adecuación para evaluar la adecuación de la hipótesis de independencia condicional de los pares.  Para ello se construyen simulaciones de la red a partir del modelo estimado. El objeto es determinar si la simulaciones reproducen la topografía de la red (particularmente volumen de nuevos vínculos y concentración de los mismos). Las simulaciones muestran limitaciones para capturar la concentración de vínculos en determinados nodos lo que revela dependencia residual no capturada. No demuestra sesgo en los coeficientes, ni señala un mecanismo concreto, ni dice que otro modelo de red la resolvería. Pero sí marca la dirección: la primera extensión consiste en refinar esa estrategia de simulación para evaluar la incertidumbre que rodea al modelo y la adecuación del supuesto de independencia condicional entre díadas.

Las demás extensiones siguen de los resultados obtenidos. En concreto señalo dos: poblar la cola de alta similitud, con horizontes más largos, o mejorar las etiquetas con vocabularios más densos. La infraestructura construida, listas, etiquetas fechadas y panel diádico versionados y documentados, permite desarrollar esas extensiones dentro de la línea de industrias creativas del grupo de investigación CREAMARKT.

Muchas gracias. Quedo a disposición de la comisión.

## 72. Tres líneas extienden el programa de investigación · **[reserva: slide en `.content-hidden`]**

<sub>`_parte3_investigacion.qmd:928` · encabezado de nivel 2 · 101 palabras</sub>

La formación combina proximidades y oportunidades. Dentro de ese entorno, la asociación estética crece y se aplana sin caída respaldada en el soporte observado. La lección transportable es metodológica: formación y éxito son preguntas distintas y la forma debe contrastarse sin imponerla. El programa amplía la cola de similitud, une formación y rendimiento y estudia quién recluta a quién. La infraestructura versionada permite desarrollar estas extensiones en CREAMARKT. Gracias; quedo a disposición de la comisión.

[Sources] paper §Conclusions (further research); paquete de réplica: 2026_jcr/output/empirical_walkthrough_v2/; líneas del grupo CREAMARKT: web UV (grups-investigacio/creamarkt), línea "big data aplicado a las industrias creativas" verificada 2026-08-15.

## 73. Reserva · Calibración de los modelos predictivos · **[reserva: slide en `.content-hidden`]**

<sub>`_parte3_investigacion.qmd:960` · encabezado de nivel 2 · 30 palabras</sub>

Las puntuaciones se emplean para ordenar, no como probabilidades. Los diagramas muestran desviaciones descriptivas de calibración y no modifican la lectura predictiva principal.

[Sources] output/fig_calibration_logit.pdf y fig_calibration_xgb.pdf (códigos 25_logit_predict.R, 20_fit_xgboost.py).

## 74. Reserva · Aciertos en el top-k (2024) · **[reserva: slide en `.content-hidden`]**

<sub>`_parte3_investigacion.qmd:973` · encabezado de nivel 2 · 33 palabras</sub>

Con eventos tan raros, un AUC alto no garantiza una lista corta operativamente útil: el top-500 contiene entre cero y dos eventos según el modelo.

[Sources] output/pred_topk_ci.csv; denominadores output/tbl_pred_comparison.csv (489.912 logit; 526.319 XGBoost).

## 75. Reserva · Estabilidad temporal del perfil · **[reserva: slide en `.content-hidden`]**

<sub>`_parte3_investigacion.qmd:987` · encabezado de nivel 2 · 33 palabras</sub>

Restringir el inicio a 2017 apenas cambia los términos estéticos; es una comprobación descriptiva de estabilidad temporal de la cuadrática, no del punto flexible.

[Sources] output/fig_coef_evolution_fullscale.pdf (código 43_coef_evolution.R); cifras 2017+: paper §Results (fig-evolution).

## 76. Reserva · Detalle del test de forma · **[reserva: slide en `.content-hidden`]**

<sub>`_parte3_investigacion.qmd:1001` · encabezado de nivel 2 · 34 palabras</sub>

La semilla está fijada, pero la asignación depende del orden de las filas. El punto y las pendientes se reproducen en distribución y el veredicto permanece invariante.

[Sources] output/shape_hinge_bootstrap_summary.csv; DECISIONS.md D024; paper §sec-shapetest (nota).

## 77. Reserva · Cobertura de etiquetas por año · **[reserva: slide en `.content-hidden`]**

<sub>`_parte3_investigacion.qmd:1015` · encabezado de nivel 2 · 34 palabras</sub>

La cobertura cae al entrar artistas nuevos sin suficientes lanzamientos etiquetados previos; por eso la medición se audita por separado y el *spline* excluye los pares sin coseno observado.

[Sources] output/fig_coverage_per_year.pdf; output/tbl_panel_composition.csv (columna coverage).

## 78. Reserva · Importancia de variables (SHAP) · **[reserva: slide en `.content-hidden`]**

<sub>`_parte3_investigacion.qmd:1029` · encabezado de nivel 2 · 35 palabras</sub>

El beeswarm sitúa estética, actividad y proximidad geodésica entre las variables con mayor contribución al *score*; no permite comparar efectos causales ni sustituye los contrastes por bloques.

[Sources] output/fig_shap_beeswarm_m1.pdf (código 20_fit_xgboost.py); lectura: paper §Results (fig-shap-bees).

