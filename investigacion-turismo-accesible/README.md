# Análisis de sentimiento en redes sociales para el turismo accesible de personas con discapacidad

Proyecto de investigación del semillero de la Universidad Libre – Seccional Barranquilla (2023).

## Introducción

El análisis de sentimiento en redes sociales sirve para entender las opiniones y actitudes de los usuarios sobre un tema. Este proyecto lo aplica al **turismo accesible**, cuyo objetivo es que las personas con discapacidad puedan viajar sin barreras y con igualdad de oportunidades. En redes sociales los usuarios cuentan sus experiencias de viaje, y entre ellas están las relacionadas con la accesibilidad.

Esta técnica tiene límites: no todos los usuarios expresan sus opiniones con claridad y los comentarios recopilados pueden tener sesgos. Aun así, bien aplicada puede aportar información útil para promover un turismo más inclusivo.

## Objetivos

- **Barreras:** identificar los principales desafíos y barreras que enfrentan las personas con discapacidad al acceder a destinos turísticos. Esto incluye deficiencias de infraestructura, transporte, información y comunicación, y también las actitudes y el nivel de conciencia de los proveedores de servicios turísticos.
- **Buenas prácticas:** detectar los aspectos positivos de la experiencia de las personas con discapacidad en destinos turísticos accesibles, y reconocer los destinos o servicios que se destacan en accesibilidad.
- **Recomendaciones:** analizar las opiniones y sugerencias de las personas con discapacidad sobre cómo mejorar la accesibilidad en el turismo, para encontrar áreas de mejora y proponer estrategias de turismo inclusivo.

## Metodología

```
API de X/Twitter ──► Extracción por palabras clave ──► CSV
                                                        │
        ┌───────────────────────────────────────────────┘
        ▼
Normalización: minúsculas, URLs, @menciones, #hashtags, puntuación, emojis, stop words (es)
        │
        ▼
Exploración: frecuencia de palabras ─► bigramas ─► red de co-ocurrencia ─► nube de palabras
        │
        ▼
Traducción es → en (googletrans) ─► Polaridad con VADER (NLTK): Positivo / Negativo / Neutral
```

## Contenido

| Archivo | Descripción |
|---|---|
| [`notebooks/01-extraccion-tweets-tweepy.ipynb`](notebooks/01-extraccion-tweets-tweepy.ipynb) | Autenticación con la API de X/Twitter (`tweepy.Client` y `tweepy.API`), búsqueda de usuarios, conversión a DataFrame y filtrado de tweets por palabras clave. Se desarrolló en Google Colab. |
| [`../capacitacion-nlp/04-modelos/04-prototipo-sentimiento-twitter.ipynb`](../capacitacion-nlp/04-modelos/04-prototipo-sentimiento-twitter.ipynb) | Pipeline completo de análisis (limpieza → bigramas → red → nube de palabras → VADER), construido en la capacitación |

## Avances

- Se construyó en Jupyter/Colab un programa que extrae tweets con credenciales de Twitter Developer, usando palabras clave definidas de antemano, con o sin límite de resultados. Los datos se guardan en CSV.
- La normalización elimina stop words, espacios, caracteres especiales y emojis. El resultado es un conjunto de palabras con contenido útil para el modelo.
- Se identifican palabras que aparecen juntas (bigramas) y sus relaciones. Con eso se arma una red y una nube de palabras que muestran los términos más relevantes según su frecuencia de co-ocurrencia.
- Como las consultas están en español, los textos se traducen al inglés y luego se calcula su polaridad (positivo, negativo o neutral) con el módulo VADER de NLTK.

## Resultados preliminares

Tras extraer los tweets se analizó la frecuencia de palabras. En la primera pasada dominaban conectores como "la", "en" y "de". Al quitarlos quedaron las palabras que dan contexto al contenido de los tweets, que son la base de la etapa de análisis de sentimiento.

## Ejecución

1. Copia `.env.example` (en la raíz del repo) a `.env` y completa las credenciales de X Developer.
2. Exporta las variables (`set -a; source .env; set +a`) y abre los notebooks.

> **Limitación actual:** desde 2023 la API de X no permite buscar tweets en el plan gratuito. Para reproducir la extracción se necesita un plan de pago o un dataset ya descargado. La parte de análisis sí se puede ejecutar con cualquier CSV de textos.

## Referencias

- X/Twitter API: https://developer.twitter.com/en
- Tweepy: https://docs.tweepy.org/en/stable/
- VADER (NLTK): https://www.nltk.org/howto/sentiment.html
- MinCIT – documento de referencia sobre turismo accesible en Colombia: https://www.mincit.gov.co/CMSPages/GetFile.aspx?guid=f29fa89a-ed14-4c7f-b803-176b86074fbc
