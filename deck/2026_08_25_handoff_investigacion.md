# Handoff → agente de `2026_jcr` · notas y slides de la propuesta investigadora

**Fecha:** 25-08-2026 · **Origen:** proyecto `catedra` (`0_ACTIVOS_2025/catedra`) · **Destino:** `0_ACTIVOS_2025/investigacion/Spoti_API/2026_jcr/presentation`

Este documento traslada dos cosas que **solo puede aplicar el proyecto `2026_jcr`**, porque su deck fuente `propuesta_investigacion.qmd` es la única fuente editable de la Parte 3 del ejercicio de cátedra:

1. **24 notas de orador reescritas** por Juan (§2). Su texto íntegro está aquí y **en ningún otro sitio**.
2. **Las correcciones de slides** de la propuesta investigadora (§3), verbatim del documento del autor.

## 0. Por qué llega por handoff y no como un commit

En `catedra`, la Parte 3 del deck unificado vive en `_parte3_investigacion.qmd`, que es una **copia generada** por `scripts/sync_partes.py` desde
`external/jcr_presentation/propuesta_investigacion.qmd` — un **enlace simbólico de solo lectura** a este proyecto. `catedra` no escribe ahí por regla explícita de su `AGENTS.md`.

Juan revisó las notas sobre el volcado de auditoría de `catedra` (`0_ejercicio/deck/presentacion_ejercicio_esquema.md`), que reúne las tres partes. Ese volcado **se regenera** desde los `.qmd`, así que su copia editada de la Parte 3 se pierde en cuanto se vuelve a generar. Por eso el texto se extrae aquí **antes** de regenerar nada.

## 1. Antes de inyectar: un bloque que el parser se salta

En `propuesta_investigacion_esquema.md`, **línea 34**, el encabezado `#### Versión editada` de la slide «¿Se ha convertido la música en un deporte de equipo?» **no lleva línea en blanco detrás**:

```
34| #### Versión editada
35| A comienzos de los setenta, menos del 3% de las entradas anuales del Billboard Hot 100…
```

`leer_esquema()` de `inyectar_notas.py` busca `#### Versión editada\n\n(.*)\Z`, con **dos** saltos. Sin la línea en blanco, ese bloque se descarta en silencio: el script lee **24** notas para **25** slides visibles y aborta con
`ERROR: 25 slides visibles en el deck y 24 notas en el esquema`.

**Arreglo:** insertar una línea en blanco entre la 34 y la 35. Con eso el esquema parsea 25/25. (Verificado desde `catedra` con un parser tolerante: 25 bloques, y 22 de ellos idénticos carácter a carácter al texto que hoy tiene el deck; los otros 3 difieren solo en espacios en blanco. Es decir, esquema y deck están en sinc.)

## 2. Notas de orador reescritas

24 de las 25 notas visibles de la Parte 3 tienen texto nuevo. En conjunto la parte pasa de **7438** a **5797** palabras (≈53.1 → ≈41.4 min a 140 palabras/min).

**Cómo aplicarlas.** Cada nota va identificada por su **posición** en `propuesta_investigacion_esquema.md` (orden de los bloques `##` que tienen «Versión editada», de 1 a 25). El emparejamiento por posición está verificado; **no lo hagas por título**: el volcado de `catedra` rotula algunas notas con el título de un *callout* en vez del de la slide, así que ambos títulos aparecen abajo y en 8 casos no coinciden. Sustituye el cuerpo del `#### Versión editada` correspondiente y luego:

```bash
# desde la raíz de 2026_jcr/presentation (ajusta la ruta a inyectar_notas.py)
python <ruta>/inyectar_notas.py propuesta_investigacion_esquema.md propuesta_investigacion.qmd --dry-run
```

Debe decir **25 slides visibles · 25 notas sustituidas · 0 creadas**. Sin `--dry-run` para escribir.

La nota de la posición 18 (`Heterogeneidad en la complementariedad estética`) es **la única que Juan no reescribió**, coherentemente con la corrección de §3 que manda ocultar esa slide. Se incluye abajo marcada como *sin cambios* para que el recuento cuadre.

### Posición 1 · Esquema

<sub>bloque `## Esquema` de `propuesta_investigacion_esquema.md` · nota #47 del volcado · 200 → 177 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Presento la propuesta de investigación *Creative Collaborations*, un trabajo conjunto con Manuel Cuadrado-García y María Luisa Palma-Martos que estudia la formación de colaboraciones entre artistas en la música grabada. La pregunta que organiza toda la exposición es fácil de formular: entre todas las parejas de artistas que podrían colaborar, ¿por qué unas llegan a hacerlo y otras no?

La exposición sigue seis bloques. Empiezo por la motivación, la pregunta, el marco conceptual y la contribución de este trabajo. Después presento los datos y, en particular, cómo medimos la proximidad estética entre dos artistas y cómo describimos la red de colaboraciones previa. El tercer bloque es el núcleo empírico: el diseño del conjunto de riesgo, la estrategia de estimación y el resultado sobre la forma de la relación entre similitud estética y colaboración. El cuarto pasa de la asociación dentro de muestra a la capacidad de ordenar colaboraciones en un año que el modelo no ha visto. El quinto resume las comprobaciones para calibrar la sensibilidad de los hallazgos y el último recoge resultados, límites y líneas futuras.
~~~~~

### Posición 2 · ¿Se ha convertido la música en un deporte de equipo?

<sub>bloque `## ¿Se ha convertido la música en un deporte de equipo?` de `propuesta_investigacion_esquema.md` · nota #48 del volcado · 219 → 222 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
A comienzos de los setenta, menos del 3% de las entradas anuales del Billboard Hot 100 correspondían a colaboraciones. Entre 2016 y 2020 esa misma tasa asciende al 40%: casi dos de cada cinco. La colaboración pasa de ser una anomalía entre los grandes éxitos a una práctica habitual en la producción cultural. Lo que se observa es un cambio de régimen que emerge en paralelo a la digitalización de la música y que se asienta en un nuevo equilibrio (elevada tasa de colaboración presente en los éxitos) con la implantación de un modelo de negocio en la industria basado en el acceso, no en la propiedad (el streaming).

El interés económico del fenómeno va más allá de la suma de créditos en una producción cultural: supone investigar los incentivos que llevan a combinar temporalmente competencias o recursos físico y simbólicos (identidades estéticas), reputación y acceso a públicos. Por limitaciones de tiempo, soslayaré el sustrato teórico que subyace al ejercicio 
empírico de esta propuesta.


No obstante introduzco un apunte: en la creación de equipos creativos, orientados a la producción cultural o en la academia (equipos científicos) existe una tensión entre similitud entre los participantes (que puede facilitar coordinación o compatibilidad) y la distancia (que puede aportar novedad y complementariedad). Y este es uno de los aspectos centrales que estudiamos en esta propuesta.
~~~~~

### Posición 3 · Colaboraciones: un emparejamiento multidimensional

<sub>bloque `## Colaboraciones: un emparejamiento multidimensional` de `propuesta_investigacion_esquema.md` · en el volcado de `catedra` aparece como «Proximidad estética: un aspecto recurrente en la literatura» (rótulo de callout) · nota #49 del volcado · 313 → 334 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
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
~~~~~

### Posición 4 · Marco conceptual

<sub>bloque `## Marco conceptual` de `propuesta_investigacion_esquema.md` · nota #50 del volcado · 388 → 343 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Aquí convergen dos literaturas. La primera estudia las consecuencias de colaborar, y en música la evidencia es clara: los *featurings* elevan la demanda de *streaming*, resultado central de McKenzie y coautores, y los duetos sobreviven más tiempo en las listas, como documentan Kaimann y coautores. 

La segunda estudia la formación del vínculo. Rivera, Soderstrom y Uzzi ordenan los mecanismos de formación de díadas en tres familias: asortativos, basados en la similitud; relacionales, basados en lazos previos, socios comunes y posición en la red; y de proximidad geográfica e institucional. Gulati y Gargiulo añaden que las redes se reproducen a sí mismas, porque los lazos previos generan la información y la confianza que hacen más probables los nuevos. Nuestros bloques de predictores son la traducción de esas tres familias.

La tensión entre parecidos y complementarios tiene también una larga tradición. Mitsuhashi y Greve distinguen compatibilidad (rasgos similares que facilitan el trabajo conjunto) de complementariedad (recursos distintos que crean valor al combinarse). La resolución habitual es un óptimo interior: Nooteboom y coautores lo formalizan como distancia cognitiva óptima; Uzzi y coautores muestran que la ciencia de mayor impacto combina una base convencional con elementos atípicos; y Smith y coautores lo estiman en la formación de equipos científicos, con una U invertida en el solapamiento temático.

En música, en cambio, la evidencia sobre distancia óptima es sobre resultados. Askin y Mauskapf muestran que la diferenciación óptima de una canción predice su éxito en listas, y Ordanini, Nunes y Nanni, que emparejar artistas de géneros distintos amplía la audiencia. Eso habla de qué funciona una vez existe la colaboración, no de qué parejas se seleccionan. Los pocos trabajos que estudian la formación en música se ciñen a una escena o un género, sin medida explícita de similitud y no estiman sobre la población completa de pares en riesgo. Esa es la brecha que cubre este trabajo: contrastar la forma de la relación estética sin presuponerla, integrada con las demás dimensiones de proximidad y con la topología de la red.
La contribución consiste en hacer esa integración operativa.
~~~~~

### Posición 5 · Afinidad estética y emparejamiento multidimensional

<sub>bloque `## Afinidad estética y emparejamiento multidimensional` de `propuesta_investigacion_esquema.md` · nota #51 del volcado · 258 → 220 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
La contribución se apoya en cuatro elementos. El primero es la integración: un único modelo combina la homofilia estética, cultural, territorial, institucional y por actividad y la estructura de la red previa, de modo que la forma de la relación estética se estima manteniendo constantes las demás proximidades y oportunidades.

El segundo es la medición. Representamos a cada artista con un vector de etiquetas generadas por los usuarios de dos redes sociales en música. Las etiquetas en $t$ se refieren a lanzamientos de un artista previos a $t$ lo que impide que la colaboración que queremos predecir entre mecánicamente como predictor a través de las etiquetas que ella misma genera. 

El tercero es el contraste para medir la proximidad estética. Combinamos especificaciones alternativas: además de la cuadrática se implementa un test de forma prespecificado, con *spline* y reversión de signo, que pregunta si el máximo interior que aparece en este diseño procede de los datos o de la función impuesta. 

El cuarto es el diseño y la validación: el evento es la primera colaboración principal–invitado, estimamos sobre el conjunto de riesgo completo sin muestrear negativos, la inferencia admite dependencia entre díadas que comparten artista y descomponemos la aportación de cada bloque dentro y fuera de muestra.

Para ello necesitamos combinar fuentes que midan tres cosas distintas: resultados, percepciones y relaciones.
~~~~~

### Posición 6 · Fuentes de datos

<sub>bloque `## Fuentes de datos` de `propuesta_investigacion_esquema.md` · en el volcado de `catedra` aparece como «Por qué etiquetas y no géneros de plataforma» (rótulo de callout) · nota #52 del volcado · 239 → 246 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Combinamos tres fuentes. La primera son las listas globales semanales de Spotify, de septiembre de 2013 a diciembre de 2025, con los metadatos de pista, álbum y artista del API Web de Spotify. Las listas nos dan el registro de colaboraciones con el detalle de créditos que necesitamos: quién es el artista principal (lead) y quién el invitado (feature) en cada pista. Tras limpiar y deduplicar nos quedamos con 12.688 combinaciones pista–artista y 2.878 artistas en el ámbito del estudio.

La segunda son las etiquetas que los usuarios asignan en Last.fm y MusicBrainz, fechadas por lanzamiento: 794.309 filas de etiquetas para 2.402 artistas, que cubre el 83,5% del ámbito. Aquí conviene justificar una elección. Spotify tiene su propia clasificación de géneros, pero solo cubre 981 de los 2.878 artistas, aproximadamente un tercio, y refleja categorías seleccionadas por la plataforma. Las etiquetas cubren más del doble y, sobre todo, recogen cómo describe la audiencia a cada artista: géneros y subgéneros, pero también estilos, estados de ánimo y otras percepciones. Para medir la posición estética desde el punto de vista del público es la fuente adecuada.

La tercera son los metadatos de MusicBrainz: tipo de entidad, país, género cuando el artista es una persona y año del primer lanzamiento. A ellos se añade el historial de sellos, construido con los créditos de álbum observados en las listas hasta el año anterior.

La cuestión decisiva es cómo convertir esas etiquetas en una medida de proximidad coherente en el tiempo.
~~~~~

### Posición 7 · Proximidad estética

<sub>bloque `## Proximidad estética` de `propuesta_investigacion_esquema.md` · nota #53 del volcado · 262 → 205 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Cada artista es un vector en el espacio de etiquetas. Su perfil en el año t acumula las etiquetas de todos sus lanzamientos fechados estrictamente antes de t, de modo que el perfil es acumulativo y está retardado por construcción. La proximidad de un par es la similitud coseno entre los dos vectores retardados: el ángulo entre los dos artistas en el espacio estético que define la audiencia.

La figura muerstra una proyección ilustrativa a dos dimensiones, si bien las medidas de similaridad son reales. Bad Bunny y J Balvin comparten buena parte del vocabulario con que se les describe y su coseno es 0,82; Bad Bunny y Ed Sheeran apenas comparten etiquetas y el coseno es 0,07.

Una observación sobre la cobertura: la proporción de pares con similitud observada cae del 93% en 2015 al 67% en 2024, porque los artistas que van entrando en las listas llegan con historiales de etiquetas más delgados. A este respecto, cuando un par carece de medida de proximidad estética  permanece en el modelo con un indicador de ausencia y el tramo cero.

Junto a esta proximidad sustantiva hay otra distinta, que no se mide en etiquetas sino en la red: la cercanía heredada de las colaboraciones anteriores.
~~~~~

### Posición 8 · La red previa amplía las oportunidades relacionales

<sub>bloque `## La red previa amplía las oportunidades relacionales` de `propuesta_investigacion_esquema.md` · nota #54 del volcado · 243 → 189 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
La red de colaboraciones cumulativa se densifica a lo largo de la década. Los artistas activos pasan de 327 en 2015 a 1.033 en 2024, el grado medio sube de 1,63 a 6,22 y la proporción de artistas sin ningún lazo previo cae del 33,3% al 16,1%. Las cifras describen la red de cada año; la figura muestra la red acumulada, sin aislados, con la misma disposición de nodos en los dos años para que se aprecie la consolidación.

El estado de la red en el año anterior no es solo un descriptivo: es el objeto sobre el que condicionamos. Para cada par de artistas en riesgo de colaborar en t calculamos, para la red acumulada hasta t-1, medidas de centralidad y posición en el grafo como número de socios comunes, si están conectados por algún camino, a qué distancia y qué posición ocupa cada artista. 

Con estas variables podemos preguntar si la historia estructural aporta información propia una vez observamos estética, cultura, instituciones y actividad. En este caso hablamos de oportunidad relacional observada, esto es, de que dos artistas cercanos en la red tienen mayor propensión a colaborar.
~~~~~

### Posición 9 · Composición de la red

<sub>bloque `## Composición de la red` de `propuesta_investigacion_esquema.md` · nota #55 del volcado · 212 → 137 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
La composición visual de esa red ayuda a entender por qué cultura y topología deben medirse por separado.

Esta figura cumple una función ilustrativa. Es el subgrafo de mayor grado de la red acumulada hasta 2024, para el 5% superior de la distribución de la centralidad. Lo que se ve es que el núcleo denso lo ocupan dos escenas, la latina y la anglófona, con un número reducido de artistas puente entre ambas.

La imagen sugiere que la estructura relacional tiene una segmentación cultural, lo que justifica una decisión de medición. En concreto la existencia de conexiones parece emerger tanto por proximidad (estéticam cultural o geográfica) como por la ubicación en el grafo, p.e. el caso de conexiones que se cierran por vecinos compartidos o la existencia de intermediarios (o brokers) que actúan de puente entre escenas.
~~~~~

### Posición 10 · El modelo de formación

<sub>bloque `## El modelo de formación` de `propuesta_investigacion_esquema.md` · en el volcado de `catedra` aparece como «Definición de la respuesta a modelizar» (rótulo de callout) · nota #56 del volcado · 308 → 207 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Decidir qué cuenta como colaboración implica definir el estimando, una decisión que no es inocua. En nuestro caso tratamos de evitar mezclar dos cosas distintas: la formación de una conexión nueva y la repetición de un vínculo que ya existía. Modelizarlas juntas es modelizar procesos distintos como si fueran uno.

Además, en las colaboraciones de más de dos artistas, evitamos contabilizar como vínculos la asociación de aquellos que son invitados (featuring), aunque tampoco los contamos como negativos.

Nuestra defición de riesgo es sensible al rol: la respuesta es positiva si el par colabora en el año t cuando uno es el principal (lead) y el otro el invitado (featuring) en una pista que entra en listas. Si el evento es de formación se exige además que no hubiera ningún lazo previo entre ambos, de ningún tipo. Las repeticiones se estudian aparte. 

El resultado agregado, que suma primeras y repetidas, tiene 1.811 eventos frente a los 1.064 de formación.

Añadir que en cualquier caso estamos ante  un evento muy raro: en el caso de formación encontramos 26,9 por cada 100.000 pares-año, con intervalo del 95% entre 25,3 y 28,5. Esa rareza condiciona el diseño y la inferencia.

Con el evento definido, construimos el conjunto completo de oportunidades plausibles.
~~~~~

### Posición 11 · Diseño: conjunto de riesgo y resultado

<sub>bloque `## Diseño: conjunto de riesgo y resultado` de `propuesta_investigacion_esquema.md` · nota #57 del volcado · 290 → 201 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Estimamos sobre el conjunto de riesgo completo: todos los pares no ordenados en riesgo en cada año, sin muestrear negativos. La ventaja es interpretativa: los coeficientes describen cómo se distinguen las colaboraciones realizadas de la población de pares que podían haber colaborado y no lo hicieron, sin las correcciones que exige un diseño caso–control (selección de una muestra de casos y otra de controles en proporciones que no necesariamente representan su frecuencia real en la población).

Lo decisivo es quién está en riesgo. Un par pertenece al conjunto de riesgo en t si la colaboración era una posibilidad realista: los dos artistas debutaron en listas antes de t y cada uno publicó una pista que entró en listas en los tres años previos. La ventana de tres años excluye ceros poco plausibles.  No obstante usamos una ventana de cinco años y sin salida como análisis de sensibilidad.

El panel de estimación tiene 3.756.411 díadas-año, 1.064 eventos de formación y 2.256 artistas entre 2015 y 2024. El año 2025 queda fuera de la estimación porque, cuando recogimos los datos, las listas de finales de 2025 podían seguir acumulando apariciones.

Sobre este mismo diseño combinamos un modelo explicativo y una referencia predictiva flexible.
~~~~~

### Posición 12 · Estimación

<sub>bloque `## Estimación` de `propuesta_investigacion_esquema.md` · en el volcado de `catedra` aparece como «¿Por qué no un ERGM?» (rótulo de callout) · nota #58 del volcado · 337 → 319 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Usamos dos herramientas con roles distintos. El logit es el modelo explicativo: modeliza la probabilidad de formación condicionada a la red del año anterior y a las características retardadas del par, con un índice lineal y efectos fijos de año, y permite hacer inferencia sobre una forma que se declara explícitamente. 

XGBoost, un conjunto de árboles potenciados, nos sirve de referencia predictiva: captura interacciones y no linealidades sin necesidad de especificarlas y nos permite cuantificar la señal predictiva para bloque de variables  de factores cuando no imponemos forma funcional. Se trata de una referencia flexible.

En el caso del ejercicio predictivo los dos modelos se reestiman para el periodo 2015–2023 y se puntúan una sola vez en 2024. El logit no tiene ningún ajuste. En XGBoost los hiperparámetros se fijaron de antemano, y la única elección basada en datos, el número de rondas o árboles que se añaden al ensamble, que se decide con parada temprana entrenando hasta 2022 y validando en 2023.

La inferencia del logit usa los errores estándar diádicos de Aronow y Samii, que admiten dependencia arbitraria entre dos díadas que comparten un artista.

Un último apunte metodológico. A pesar de que los modelos exponenciales de grafos aleatorios podrían parecer una opción natural para modelizar datos relacionales, existen dos razones que justifican la elección de modelos de clasificación. 

La primera es de escala: con 2.256 actores y millones de díadas, la constante de normalización es intratable y la estimación tiende a degenerar. En la práctica la estimación no sería viable.

La segunda es el tipo de pregunta que responde: un ERGM modeliza la distribución conjunta de la red; el objetivo del trabajo que presento es modelizar la probabilidad condicional de cada díada dada la red previa.

Nuestra elección exige evaluar a posteriori si la hipótesis de independencia condicional entre las observaciones díadicas resulta razonable una vez considerados los predictores y el estado previo de la red.
~~~~~

### Posición 13 · Especificaciones: proximidades y modelos anidados

<sub>bloque `## Especificaciones: proximidades y modelos anidados` de `propuesta_investigacion_esquema.md` · nota #59 del volcado · 294 → 243 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
La comparación entre modelos exige asignar cada variable a una dimensión sustantiva concreta.


Estadísticamente trabajamos con cuatro bloques y 32 variables, además de los efectos de año; la tabla los resume. 

1. El bloque de red tiene ocho términos: vecinos comunes, índices de Jaccard y Adamic–Adar, conexión preferente, alcanzabilidad, proximidad geodésica y grado (en media y en diferencia). 

2. El bloque estético incorpora la proximidad estética (sim del coseno) y su cuadrado; la posición respecto al centroide anual y la entropía de etiquetas, que describen tipicidad y la amplitud (artista tiene similitudes relevantes con muchos, entropía alta, o pocos artistas) de su identidad estética; y el tamaño del vocabulario y los indicadores de ausencia, que controlan la cobertura. 

3. El bloque de actividad tiene siete: pistas acumuladas en listas y longitud de carrera, en media y diferencia, más la duración de la elegibilidad conjunta en tramos, que controla el tiempo de exposición. 

4. Finalmente el bloque de otras proximidades y atributos tiene otros siete: escena lingüística, país registrado, tipo de artista, género cuando ambos son personas y tres medidas retardadas de historial común de sellos.

Observación: las variables de nodo entran como media del par, que mide nivel, y como diferencia absoluta, que mide asimetría, de modo que el resultado no dependa del orden arbitrario de los artistas dentro del par.

Estimamos tres modelos anidados:  Completo, con los cuatro bloques; Solo red, con la topología; y Sin red, con estética, actividad y atributos.
~~~~~

### Posición 14 · Versiones de la proximidad estética

<sub>bloque `## Versiones de la proximidad estética` de `propuesta_investigacion_esquema.md` · en el volcado de `catedra` aparece como «¿Optimo interior?» (rótulo de callout) · nota #60 del volcado · 338 → 208 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
La especificación cuadrática, que es  habitual en la literatura y  usamos en nuestras estimaciones, impone un máximo por construcción. Pero encontrar un máximo no acredita que exista una relación de U-invertida como la postulada.

Para reforzar la evidencia recurrimos a tres estrategias: 
1. La primera, consiste en discretizar la métrica de similitud estética y analizar las tasas de formación observadas por tramo (e intervalos), sin ningún ajuste funcional. 
2. La segunda es ajustar un *spline* cúbico que da la curva flexible del perfil. 
3. La tercera es un test confirmatorio de reversión de signo, basado en el enfoque de dos líneas de Simonsohn, con dos submuestras: en una se localiza el punto de ruptura como máximo del *spline*; en la otra se estima la pendiente posterior, con datos que no se usaron para localizarlo. Solo confirma un óptimo interior si la pendiente cambia de positiva a negativa.

Evaluamos las propiedades de este último  por simulación, con paneles calibrados al número de eventos y a la distribución de similitud de nuestra muestra. Para 200 replicas, cuando el perfil verdadero crece y se aplana, el test confirma falsamente un óptimo interior en el 0,5% de los casos; frente a un óptimo interior lo detecta en el 79% de las simulaciones.
~~~~~

### Posición 15 · Resultado base: especificación cuadrática

<sub>bloque `## Resultado base: especificación cuadrática` de `propuesta_investigacion_esquema.md` · nota #61 del volcado · 367 → 254 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Comenzamos analizando los resultados de la estimación base.

[Zoom: bloque de red.] El bloque de red es conjuntamente informativo (contraste conjunto del bloque rechaza el modelo restringido) y proximidad y centralidad se asocian a la formación de 
colaboraciones. La proximidad geodésica muestra como los pares que ya estaban cerca en la red previa tienen una propensión mucho mayor a conectar directamente. El grado medio también es positivo, en línea con un mecanismo de visibilidad si bien la asimetría en la centralidad se asocia a una menor probabilidad de vínculo. 

[Zoom: estética y escena.] La forma cuadrática en la proximidad estética reproduce el patrón conocido: término lineal positivo y cuadrático negativo que sitúan un máximo en una similitud de 0.637. No obstante, por ubicación,  en el percentil 94.8 del soporte,  la región cuenta con pocos pares y eventos: la estimación apunta a una relación no lineal y cóncava, pero no es concluyente respecto a una caída. 

[Zoom: actividad, país y sellos.] Compartir la escena  presenta una asociación positiva y precisa, y una actividad media mayor en listas se asocia positivamente con la formación y una mayor diferencia de actividad, negativamente, de modo que pares activos con niveles de actividad similares se asocian a una mayor propensión a colaborar. El solapamiento de carreras en listas (las variables elegibilidad conjunta) muestran coeficientes negativos y crecientes: los pares que llevan años coexistiendo sin colaborar tienen cada vez menos probabilidad de hacerlo.


Importante recordar que son asociaciones condicionales y las escalas de los coeficientes no son comparables entre variables.
~~~~~

### Posición 16 · Lectura crítica del óptimo interior

<sub>bloque `## Lectura crítica del óptimo interior` de `propuesta_investigacion_esquema.md` · nota #62 del volcado · 254 → 169 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Revisamos la supervivencia del óptimo interior a modificaciones de la muestra utilizada en su estimación. La pregunta que nos hacemos es si ese máximo es una rasgo del comportamiento de los agentes a la hora de formar vínculos o un artefacto de la especificación. 

Para responderla cruzamos dos decisiones del diseño: 
1. La definición de la respuesta, todos los pares o solo pares artista principal–artista invitado
2. El conjunto de riesgo: consideramos una ventana de tres años para determinar si un artista está activo (deforma que si no produce un hit en esos tres años, sale del conjunto de riesgo) o sin salida (una vez se alcanzan llega a listas, se permanece en el conjunto de riesgo).

La reestimación del modelo bajo estos cuatro supuestos proporciona un resultado: **la forma cuadrática sobrevive a los cambios de muestra**. El máximo implícito se queda entre 0,63 y 0,70 en las cuatro celdas, con cualquier conjunto de riesgo y cualquier proyección, aunque siempre en la cola alta de la distribución de similitud.
~~~~~

### Posición 17 · La asociación estética crece y se aplana dentro del soporte

<sub>bloque `## La asociación estética crece y se aplana dentro del soporte` de `propuesta_investigacion_esquema.md` · nota #63 del volcado · 305 → 235 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Ya que la ubicación del óptimo interior en la cola superior de la distribución es compatible no solo con una reversión del efecto en la proximidad estética, sino con una saturación del mismo analizamos la relación postulada con especificaciones flexibles (que no presuponen una forma determinada). 

La figura siguiente muestra directamente la forma que sí respaldan los datos. La curva es el *spline* prespecificado sobre el modelo Completo y los puntos son las tasas de colaboración observadas para la discretización de la variable similitud del coseno. Ambas apuntan en la misma dirección: la tasa de formación sube con fuerza desde similitudes bajas hasta aproximadamente 0,3 o 0,4 para aplanarse después. Ningún tramo dentro del soporte tiene una tasa inferior a los anteriores, el *spline* no se gira hacia abajo en ningún punto del rango respaldado y los dos tramos más altos, con pocas observaciones de comparación, quedan por encima de las tasas intermedias, no por debajo.

Además, un test confirmatorio utiliza la mitad de la muestra para detectar un punto de ruptura (un máximo para la tasa de colaboración) en la distribución de la variable de similitud y ajusta dos rectas, antes y después de éste con el otro 50% de la muestra. El test confirma la subida anterior está confirmada pero no una caída posterior. El remuestreo muestra valores positivos con intervalos que incluyen cerolo que apoya un crecimiento y aplanamiento, sin reversión confirmada.
~~~~~

### Posición 18 · Heterogeneidad en la complementariedad estética

<sub>bloque `## Heterogeneidad en la complementariedad estética` de `propuesta_investigacion_esquema.md` · en el volcado de `catedra` aparece como «Lectura» (rótulo de callout) · nota #64 del volcado · 185 → 185 palabras</sub>

**SIN CAMBIOS.** Dejar la «Versión editada» tal como está.

### Posición 19 · Capacidad predictiva por bloques

<sub>bloque `## Capacidad predictiva por bloques` de `propuesta_investigacion_esquema.md` · nota #65 del volcado · 459 → 282 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
El ejercicio predictivo utiliza un protocolo estricto. Los dos modelos (logit y xgbm) se reestiman con datos 2015–2023 y se puntúan una sola vez en 2024, de modo que el modelo evaluado nunca ha visto el año de evaluación; XGBoost elige su número de árboles entrenando hasta 2022 y validando en 2023. En 2024 hay 64 eventos de formación de 490.000 (logit) o 526.000 díadas (xgbm) puntuadas según el modelo, una tasa base de 0,12 a 0,13 por mil. La diferencia es que el logit se entrena para el conjunto de casos completos y XGBoost para todos los pares, gracias al tratamiento nativo de los valores ausentes.

El AUC-PR del mejor modelo multiplica la tasa base por unas 18 veces en el logit y unas 14 en XGBoost. El *lift* en los 500 primeros mira el extremo del ranking y es inestable con tan pocos positivos, por eso añadimos las métricas a 10.000 primeros, donde el Completo recupera el 42% de los eventos con logit y el 31% con XGBoost. Conviene no comparar el  *lift* entre modelos por la  diferencia en la muestra de entrenamiento.

Un análisis de la capacidad explicativa dentro de la muestra de entrenamiento para los diferentes grupos de variables (test de wald sobre para modelo restringido en la especificación logit) es concluyente y apoya el modelo no restringindo. Fuera de muestra sin embargo la aportación del bloque de predictores de red es limitada. Por el contrario, quitar el bloque no-red tiene mayor coste, lo que sugiere que los bloques estética, actividad, cultura, instituciones y demás atributos contienen la mayor parte de la señal predictiva observable; la red es informativa dentro de muestra, pero al horizonte anual añade poco.
~~~~~

### Posición 20 · Constraste no paramétrico de la forma funcional

<sub>bloque `## Constraste no paramétrico de la forma funcional` de `propuesta_investigacion_esquema.md` · nota #66 del volcado · 216 → 137 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Una utilidad adicional de XGBoost es que nos permite comprobar la forma del perfil estético sin imponer ninguna forma funcional.

Para ello recurrimos a la atribución de las predicciones locales a los distintos predictores del modelo que porprociona los valores de shapley. El gráfico de dependencia muestra para cada par-año cuánto aporta la similitud estética a la puntuación (contribuciones al *score*, en escala de log-odds, no probabilidades parciales). Los valores se muestran para la el conjunto de dartos de prueba (2024).

El patrón reafirma el hallazgo del ejercicio de discretización y el *spline*: la contribución sube con fuerza por debajo de una similitud de 0,3, se aplana desde aproximadamente 0,4 y no muestra un declive claro en la parte alta. 

Es importante señalar que este resultado se obtiene de un modelo que no impone ninguna forma funcional.
~~~~~

### Posición 21 · Comprobaciones de los resultados

<sub>bloque `## Comprobaciones de los resultados` de `propuesta_investigacion_esquema.md` · nota #67 del volcado · 449 → 245 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Esta tabla resume muestra distintas  comprobaciones. Todas son análisis descriptivos o de sensibilidad. Las presento brevemente.

La primera familia es la inferencia. El *bootstrap* de nodos, que remuestrea artistas y arrastra también la composición del conjunto de riesgo, es más conservador: aumenta los errores estándar con una ratio mediana de 1,60. Bajo ese criterio los términos estéticos, la geodésica, el grado, la escena y el tipo se mantienen; el historial común de sello deja de distinguirse de cero, y por eso lo leemos como positivo pero impreciso. 

La segunda es la definición del resultado. Restringir los eventos a pistas de exactamente dos artistas (elección bilateral), deja 609 eventos y un perfil esencialmente igual; ponderar por tamaño de equipo o devolver los pares invitado–invitado como clase negativa tampoco lo cambia, y los bloques de red, actividad y atributos se mueven como máximo 0,37, 0,13 y 0,05 en cada variante. 

La tercera es la ventana del conjunto de riesgo: con cero, tres y cinco años los máximos implícitos son 0,635, 0,637 y 0,630.

La cuarta es la medición de etiquetas: solo MusicBrainz, vectores binarios, vocabularios mínimos de tres y de cinco etiquetas, submuestra bien medida y terciles de cobertura. El perfil sobrevive en todas, los demás bloques se mueven como máximo 0,26 y las interacciones con la cobertura no son conjuntamente significativas, p de 0,082.

La corrección de Firth, el enlace cloglog y la inclusión de efectos de artista con un logit condicional se discuten a continuación.
~~~~~

### Posición 22 · Corrección de sesgo de Firth

<sub>bloque `## Corrección de sesgo de Firth` de `propuesta_investigacion_esquema.md` · nota #68 del volcado · 236 → 188 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Dada la baja frecuencia del evento analizado, estimamos dos modelos alternativos. En primer lugar, empleamos la corrección de Firth, basada en una verosimilitud penalizada, para reducir el sesgo de las estimaciones y mitigar posibles problemas de separación. En segundo lugar, estimamos un modelo con enlace log-log complementario (cloglog), cuya forma asimétrica resulta apropiada cuando la respuesta registra la ocurrencia de un evento generado por un proceso en tiempo continuo.

[Zoom: columna Δ Firth–logit.] Los dos términos focales de similitud cambian como máximo 0,014. El mayor desplazamiento de toda la tabla es 0,176, en el Jaccard de vecindarios, que equivale a aproximadamente 0,23 de su error estándar. Los coeficientes culturales e institucionales son igual de estables. El cloglog conserva el mismo patrón de signos, aunque está en otra escala de enlace y sus magnitudes no se comparan directamente con las del logit. Tampoco hay señales de separación: la estimación converge y ninguna observación tiene una probabilidad ajustada superior a un medio.

El alcance es el que es: una auditoría de coeficientes. Queda pendiente recalcular errores estándar  así que el ejercicio  muestra que las estimaciones puntuales no dependen del estimador.
~~~~~

### Posición 23 · Logit condicional

<sub>bloque `## Logit condicional` de `propuesta_investigacion_esquema.md` · nota #69 del volcado · 305 → 252 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Los modelos anteriores solo controlan las diferencias entre artistas mediante variables observadas. Para absorber las características no observables de los artistas principales, aplicamos un diseño de elección emparejada: para cada artista principal con al menos una colaboración en un año, comparamos los colaboradores elegidos con todos los candidatos elegibles. El estrato artista-año absorbe toda característica constante del artista ese año, como su calidad latente, visibilidad o actividad.

El análisis comprende 641 estratos, 545.149 pares-año y 1.064 eventos. Las variables de red no se incluyen porque la posición del artista principal es fija dentro de cada estrato. Aunque es el control más fuerte frente a la heterogeneidad no observada, solo incluye artistas con alguna colaboración; por ello, los coeficientes se interpretan por su dirección, no por su magnitud respecto a los modelos anteriores.

[Zoom: similitud, escena, país y sello.] La dirección y la curvatura estéticas se mantienen cerca de los valores base. Las proximidades cultural e institucional aparecen incluso mayores. Parte de esa diferencia tiene explicación: dentro del conjunto de oportunidades de un principal, el país y el sello ya no compiten con la posición del propio principal en la red, que en el modelo base absorbía parte de la asociación geográfica.

Lo que este ejercicio nos dice es que los resultados de proximidad no son un artefacto de la heterogeneidad no observada de artistas principales: dentro de cada principal, los socios más cercanos estética, cultural e institucionalmente son elegidos con más frecuencia.

Con la evidencia principal y sus comprobaciones, sintetizo qué aprendemos.
~~~~~

### Posición 24 · La formación es multidimensional

<sub>bloque `## La formación es multidimensional` de `propuesta_investigacion_esquema.md` · nota #70 del volcado · 346 → 290 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Cuatro resultados. El primero es la hipótesis focal: dentro del soporte común, la proximidad estética tiene una asociación positiva que se aplana. Es importante señalar que la partición prespecificada localiza el cambio alrededor de 0.68, la subida está confirmada y la caída no: no hay evidencia de declive en ningún punto del soporte observado. Eso es coherente con un umbral de compatibilidad: la poca similitud es una barrera para trabajar juntos pero los datos no respaldan una penalización por compatibilidad excesiva entre los pares que observamos.

El segundo son la relevancia de otras medidas de proximidad. La cultural importa, pero en forma de escena compartida más que de país. La institucional, el historial común de sello, es positiva pero menos robusta. Y en actividad, los pares más activos y más equilibrados colaboran más, mientras que la proximidad de carrera no da un resultado claro.

El tercero es la topología. El bloque de red es claramente informativo dentro de muestra, pero en el ejercicio predictivo (para el año de prueba) añade poca mejora marginal a las características no-red, con intervalos que incluyen cero. Este hallazgo sugiere que los estadísticos son el resultado de un proceso de preferencias y oportunidades que las características observables ya capturan y no variables explicativas originales.

El cuarto es metodológico: en este diseño, el máximo interior aparece al imponer una cuadrática y no se reproduce con las formas flexibles. Formación y éxito son preguntas distintas, y la forma debe contrastarse sin imponerla.

En conjunto, la colaboración emerge de varias proximidades y oportunidades que operan juntas: la estética funciona como condición de compatibilidad dentro del soporte observado; cultura, instituciones, actividad y red estructuran qué emparejamientos llegan a materializarse. 

Este balance exige declarar también dónde no alcanza la evidencia.
~~~~~

### Posición 25 · Limitaciones y extensiones

<sub>bloque `## Limitaciones y extensiones` de `propuesta_investigacion_esquema.md` · nota #71 del volcado · 415 → 309 palabras</sub>

Texto nuevo (sustituye íntegro el cuerpo de «Versión editada»). Copiar tal cual lo que va entre los delimitadores, sin incluirlos:

~~~~~text
Las limitaciones son de diferentes tipos. Primera, las estimaciones son asociaciones condicionales a la red retardada, no efectos causales. Segunda, las medidas son parciales: las etiquetas o la escena incorporan ruido en su construcción y el historial de sellos no agota los canales institucionales. Tercera, la cola alta está poco poblada: hay ocho eventos por encima de una similitud de 0,90, así que no es posible descartar una penalización por falta de coplementariedad para la similitud extrema. Cuarta, población y resultado están condicionados: estudiamos artistas activos en listas globales con metadatos, no se modeliza el llegar las listas no se modela y la colaboración fuera de listas se incorpora parcialmente. 

En lo que respecta a extensiones existe un diagnóstico de adecuación para evaluar la adecuación de la hipótesis de independencia condicional de los pares.  Para ello se construyen simulaciones de la red a partir del modelo estimado. El objeto es determinar si la simulaciones reproducen la topografía de la red (particularmente volumen de nuevos vínculos y concentración de los mismos). Las simulaciones muestran limitaciones para capturar la concentración de vínculos en determinados nodos lo que revela dependencia residual no capturada. No demuestra sesgo en los coeficientes, ni señala un mecanismo concreto, ni dice que otro modelo de red la resolvería. Pero sí marca la dirección: la primera extensión consiste en refinar esa estrategia de simulación para evaluar la incertidumbre que rodea al modelo y la adecuación del supuesto de independencia condicional entre díadas.

Las demás extensiones siguen de los resultados obtenidos. En concreto señalo dos: poblar la cola de alta similitud, con horizontes más largos, o mejorar las etiquetas con vocabularios más densos. La infraestructura construida, listas, etiquetas fechadas y panel diádico versionados y documentados, permite desarrollar esas extensiones dentro de la línea de industrias creativas del grupo de investigación CREAMARKT.

Muchas gracias. Quedo a disposición de la comisión.
~~~~~

## 3. Correcciones de slides (verbatim del autor)

Copiado sin alterar de `catedra/0_ejercicio/deck/2026_08_24_correcciones.md`, sección «Propuesta investigadora». Las decisiones de contenido son del autor; `catedra` no las interpreta.

---

## Slide `Afinidad estética y emparejamiento multidimensional`
- NO ES heterofilia por actividad. En realidad el término diff_hits_charts es negativo (pequeño), aunque el nivel de actividad medio es positivo: habría que interpretarlo correctamente, porque implica la existencia de homofilía. EN concreto, de la interpretación en `codex`, 
> El **coeficiente positivo de la media** indica que las díadas con mayor actividad acumulada conjunta presentan mayores odds de formar una primera colaboración. Una unidad adicional en la media se asocia con aproximadamente un 3,4% más de odds.
**El coeficiente negativo de la diferencia** indica que, para un mismo nivel medio de actividad, una mayor desigualdad entre los miembros reduce las odds: alrededor de un 1,4% por cada pista adicional de brecha.
La lectura conjunta es: importan tanto el nivel de actividad como su equilibrio dentro de la díada. Algebraicamente, una pista adicional del miembro menos activo está asociada con un aumento mucho mayor que una pista adicional del miembro ya más activo. Es compatible con matching por nivel de actividad o con un “cuello de botella” en el miembro menos activo, pero no identifica ese mecanismo causalmente.

## Slide `Fuentes de datos`

- Eliminar un `$$` en el 34% del .callout.

## Slide `Composición de la red`

- UTILIZAR el grafo de AIMAC: la versión que muestra no es la misma!!!! (y hay errores como asignar a becky g a anglófono)

## Slide `El modelo de formación`

- MUY DENSO Y EXTENSO. Simplificar

## Slide `Especificaciones: proximidades y modelos anidados`

- Arreglar la nota en el .callout. Visualización bizarra 

## Slide `Versiones de la proximidad estética`

Modificar el texto en el callout así: `La especificación cuadrática para la proximidad estética impone un máximo por construcción. Pero, ¿alcanza la propensión a colaborar un máximo interior de similitud estética, o crece y se satura?`

## Slide `Resultado base: especificación cuadrática`

- Sustituir en tabla (y en cualquiera posterior) el nombre de la variable `Misma escena lingüística` por `Misma escena`

- DUPLICAR LA SLIDE PERO EN LUGAR DE TABLA UTILIZAR UN GRAFICO DE DOT-AND-WHISKER PLOTS DE ALGUNOS COEFICIENTES (P.E. LOS QUE SE COMENTAN EN EL ENTORNO `{.notes}`) PARA VISUALIZAR RDOS EN LUGAR DE TENER QUE LEER

## Slide `Lectura crítica del óptimo interior`

En esta slide se incorporan resultados para los que no hemos mostrado ninguna evidencia. En concreto, estamos viendo cmo el óptimo interior sobrevive. NO ESTAMOS VIENDO QUE ESPECIFICACIONES ALTERNATIVAS LO HAGAN POCO PLAUSIBLE, PORQUE ESAS ESPECIFICACIONES ALTERNATIVAS VIENEN EN LA TRASPARENCIA POSTERIOR.

Por tanto hay que modificar: 

1. eliminar todo el texto de la slide Y DEJAR SOLO la tabla
2. Incluir en la tabla el percentil de la distribución en el que se sitúa el óptimo interior

## Slide `Heterogeneidad en la complementariedad estética`

RESERVA: Ocultar esta slide (Presentación excesivamente  larga -- necesitamos aligerar). 

## Slide `Comprobaciones de los resultados`

- Eliminar de la tabla la fila `Colaboración fuera de listas`. Mucho contenido

- Eliminar además mención a Firth, cloglog y clogit ya que reservamos dos slides para ellas

## Slide `Corrección de sesgo de Firth`

DUPLICAR SLIDE PARA MOSTRAR GRAFICO COMO EN SLIDE DEL MODELO BASE PERO EN LUGAR DE ESTIMACION PUNTUAL + INTERVALO PRODUCIR
ESTIMACION CON FIRTH-ESTIMACION LOGIT (VER LA DISTANCIA ENTRE ESTIMACIONES PUNTUALES)

IGUAL CON CLOGLOG

USAR MISMOS COEFICIENTES QUE EN MODELO BASE 

## Slide `Logit condicional`

MISMA ESTRATEGIA QUE SLIDE DE FIRTH: DUPLICAR PARA MOSTRAR GRÁFICO EN LA SEGUNDA. MISMOS COEFS QUE MODELO BASE.

## Slide `Limitaciones y extensiones`

Corregir la slide utilizando la narrativa del esquema `presentacion_ejercicio_esquema.md` del proyecto catedra.

---

Una precisión sobre el último punto («Limitaciones y extensiones → usar la narrativa del esquema `presentacion_ejercicio_esquema.md`»): esa narrativa es exactamente la nota de la **posición 25** de §2. No hace falta abrir el fichero de `catedra`.

## 4. Paso de vuelta hacia `catedra`

Cuando el deck fuente esté actualizado y renderizado, avisar a `catedra` para que ejecute:

```bash
cd 0_ejercicio/deck
python scripts/sync_partes.py            # recopia _parte3_investigacion.qmd y sus figuras
quarto render presentacion_ejercicio.qmd # RevealJS + Beamer del deck unificado
python scripts/extraer_notas.py          # regenera el volcado de auditoría
```

Hasta entonces, el volcado de `catedra` seguirá mostrando el texto **antiguo** de la Parte 3. Es lo esperado, no un error.

Si al ocultar la slide «Heterogeneidad…» (o al duplicar slides para los dot-and-whisker) cambia el número de slides visibles, cambiarán también los contadores de control de `catedra`: hoy **61** `<aside class="notes">` en el HTML unificado y **77** páginas en el PDF Beamer.

## 5. Ajuste de tiempo (pendiente, informativo)

La Parte 3 tiene **20 min** asignados en el ejercicio (15 CV + 15 docente + 20 investigación = 50 min). Con las notas nuevas queda en **≈41.4 min** a 140 palabras/min, frente a ≈53.1 antes.

La cota es mecánica (leer íntegra cada nota, sin pausas), pero la desviación es grande y sigue siendo la mayor de las tres partes: el CV queda en ≈21,4 min para 15 y la propuesta docente en ≈18,5 para 15. Ocultar la slide de heterogeneidad (§3) ayuda; probablemente no baste.
