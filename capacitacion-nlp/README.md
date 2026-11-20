# Capacitación en NLP – Semillero Unilibre Barranquilla

Curso de Procesamiento de Lenguaje Natural con Python, dictado en el semillero de investigación de la Universidad Libre – Seccional Barranquilla entre **marzo y mayo de 2023**, en cuatro encuentros. Cada encuentro tiene notebooks teóricos y un taller. Algunos talleres incluyen su solución.

> Los notebooks se guardaron con sus salidas, así que puedes leerlos en GitHub sin ejecutarlos.

## Encuentro 1 – Fundamentos de Python para texto · [`01-fundamentos/`](01-fundamentos/)

| Notebook | Contenido |
|---|---|
| [`00-demo-twitter-api`](01-fundamentos/00-demo-twitter-api.ipynb) | Demo inicial: conexión a la API de Twitter con `tweepy` y términos de búsqueda |
| [`00-fundamentos-bases`](01-fundamentos/00-fundamentos-bases.ipynb) | f-strings, alineación y relleno, formato de fechas |
| [`01-archivos-de-texto`](01-fundamentos/01-archivos-de-texto.ipynb) | Crear, leer (`read`, `seek`, `readlines`), escribir y agregar a archivos; context managers |
| [`02-archivos-pdf`](01-fundamentos/02-archivos-pdf.ipynb) | Lectura y extracción de texto de PDFs con `PyPDF2` |
| [`03-expresiones-regulares`](01-fundamentos/03-expresiones-regulares.ipynb) | Patrones, identificadores, cuantificadores, grupos, comodines, exclusión |
| [`04-taller`](01-fundamentos/04-taller.ipynb) · [`solución`](01-fundamentos/04-taller-solucion.ipynb) | f-strings, archivo de tweets del proyecto, `contacts.txt`, PDF `Business_Proposal.pdf`, regex |

## Encuentro 2 – Normalización de texto · [`02-normalizacion/`](02-normalizacion/)

| Notebook | Contenido |
|---|---|
| [`00-spacy-basics`](02-normalizacion/00-spacy-basics.ipynb) | Instalación de spaCy, objetos `Doc`/`Token`/`Span`, pipeline, POS, dependencias |
| [`01-tokenizacion`](02-normalizacion/01-tokenizacion.ipynb) | Prefijos, sufijos, infijos, excepciones, entidades nombradas, noun chunks, `displacy` |
| [`02-stemming`](02-normalizacion/02-stemming.ipynb) | Porter y Snowball (NLTK) |
| [`03-lematizacion`](02-normalizacion/03-lematizacion.ipynb) | Lemas con spaCy |
| [`04-stop-words`](02-normalizacion/04-stop-words.ipynb) | Consultar, agregar y quitar stop words |
| [`05-vocabulario-y-matching`](02-normalizacion/05-vocabulario-y-matching.ipynb) | `Matcher` por reglas, cuantificadores, `PhraseMatcher` sobre `reaganomics.txt` |
| [`06-taller`](02-normalizacion/06-taller.ipynb) · [`solución`](02-normalizacion/07-taller-solucion.ipynb) | Taller de conceptos básicos de NLP sobre `owlcreek.txt` |

## Encuentro 3 – Vectorización y clasificación · [`03-vectorizacion/`](03-vectorizacion/)

Diapositivas: [`presentaciones/encuentro-3-vectorizacion.pptx`](presentaciones/encuentro-3-vectorizacion.pptx)

| Notebook | Contenido |
|---|---|
| [`00-scikit-learn-primer`](03-vectorizacion/00-scikit-learn-primer.ipynb) | Introducción a scikit-learn con el corpus SMS Spam: train/test split, regresión logística, Naive Bayes, SVM |
| [`01-extraccion-de-features`](03-vectorizacion/01-extraccion-de-features.ipynb) | Vocabulario desde cero, bolsa de palabras, TF-IDF, `Pipeline` |
| [`02-proyecto-clasificacion-de-texto`](03-vectorizacion/02-proyecto-clasificacion-de-texto.ipynb) | Clasificación de reseñas de películas: limpieza de NaN y vacíos, pipelines, métricas |
| [`03-taller`](03-vectorizacion/03-taller.ipynb) | Evaluación: clasificar `moviereviews2.tsv` con `LinearSVC` |

## Encuentro 4 – Modelos · [`04-modelos/`](04-modelos/)

Diapositivas: [`presentaciones/encuentro-4-modelos.pptx`](presentaciones/encuentro-4-modelos.pptx)

| Notebook | Contenido |
|---|---|
| [`00-latent-dirichlet-allocation`](04-modelos/00-latent-dirichlet-allocation.ipynb) | Modelado de temas con LDA sobre artículos de NPR |
| [`01-factorizacion-matrices-no-negativas`](04-modelos/01-factorizacion-matrices-no-negativas.ipynb) | Modelado de temas con NMF |
| [`02-semantica-y-vectores-de-palabras`](04-modelos/02-semantica-y-vectores-de-palabras.ipynb) | Word vectors de spaCy, similitud, norma y aritmética vectorial |
| [`03-analisis-de-sentimiento`](04-modelos/03-analisis-de-sentimiento.ipynb) | VADER (NLTK) sobre reseñas de Amazon y medición de su precisión |
| [`04-prototipo-sentimiento-twitter`](04-modelos/04-prototipo-sentimiento-twitter.ipynb) | **Prototipo del proyecto**: tweets ("servicios hoteleros") → limpieza → stop words en español → bigramas y red → nube de palabras → traducción → VADER |

## Datos

Los datasets están en [`datos/`](datos/) y los notebooks los leen con rutas relativas (`../datos/...`). Ahí mismo se explica cuáles vienen incluidos y cuáles hay que descargar aparte.

## Entorno

- Para ejecutar los notebooks hoy, usa el [`requirements.txt`](../requirements.txt) de la raíz.
- [`entorno-original-curso.yml`](entorno-original-curso.yml) es el entorno conda que se usó en 2023 (Python 3.6/3.7, spaCy 2.0). Se deja como referencia histórica.

### Notas de compatibilidad

- `00-spacy-basics` usa `spacy.load('en')`, que es sintaxis de spaCy 2. En spaCy 3 hay que cambiarlo por `spacy.load('en_core_web_sm')`.
- `PyPDF2` ahora se llama `pypdf`. La API de `PdfReader` es casi igual.
- `DataFrame.append` (usado en algunos notebooks) se eliminó en pandas 2. Hay que reemplazarlo por `pd.concat`.
- Desde 2023 la API de X/Twitter cobra por la búsqueda de tweets, así que los notebooks que la usan necesitan un plan de pago o datos ya descargados.
