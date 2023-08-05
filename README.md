# DataEmoSci
Análisis de Sentimiento en Redes Sociales para Turismo Accesible de Personas con Discapacidad

## Introducción

El análisis de sentimiento en las redes sociales se ha convertido en una herramienta valiosa para comprender las opiniones y actitudes de los usuarios sobre diversos temas. Un área en la que se ha aplicado este análisis es el turismo accesible para personas con discapacidad. El turismo accesible tiene como objetivo garantizar que las personas con discapacidad puedan disfrutar de experiencias de viaje sin barreras y con igualdad de oportunidades. Las plataformas de redes sociales se han convertido en espacios donde los usuarios comparten sus experiencias de viaje, incluidas aquellas relacionadas con el turismo accesible.

Es importante tener en cuenta las limitaciones del análisis de sentimiento en las redes sociales. No todos los usuarios expresan sus opiniones de manera clara, y puede haber sesgos en los comentarios recopilados. Sin embargo, cuando se ejecuta correctamente, esta técnica puede proporcionar información valiosa y contribuir a promover un turismo más inclusivo y accesible para las personas con discapacidad.

## Objetivos

- Identificar los principales desafíos y barreras que enfrentan las personas con discapacidad al acceder a destinos turísticos. Esto incluye identificar deficiencias en infraestructuras, transporte, información y comunicación, así como comprender las actitudes y la conciencia de los proveedores de servicios turísticos.
- Detectar aspectos positivos y destacados de la experiencia de las personas con discapacidad en destinos turísticos accesibles. Esto puede implicar reconocer destinos o servicios turísticos que se destacan en accesibilidad.
- Analizar las opiniones y recomendaciones de las personas con discapacidad sobre cómo mejorar la accesibilidad en el turismo. Esto implica recopilar y analizar los comentarios y sugerencias de las personas con discapacidad para identificar áreas de mejora y desarrollar estrategias para promover un turismo más inclusivo.

## Progreso

Hemos desarrollado un programa utilizando Jupyter Notebook, que incluye funciones para extraer datos de Twitter utilizando credenciales de autenticación de Twitter Developer. Predefinimos palabras clave para la extracción de datos y realizamos la extracción con o sin un límite de tweets. Los datos extraídos se almacenan en un archivo CSV. El proceso de normalización posterior implica eliminar stopwords, espacios, caracteres especiales y emojis. Este proceso resulta en un conjunto de datos que contiene palabras valiosas, que se utilizarán para el entrenamiento del modelo.

El código también identifica palabras coocurrentes (bigramas) y sus relaciones, lo que nos permite crear una nube de palabras para visualizar la relevancia de las palabras en función de su frecuencia de coocurrencia. Dado que las consultas o criterios están en español, traducimos los resultados y procedemos con el preentrenamiento del modelo. Después de esto, determinamos la polaridad de los datos extraídos (Positivo, Negativo, Neutral) utilizando el módulo VADER de NLTK.

## Análisis

### Análisis de Sentimiento en Redes Sociales para Turismo Accesible de Personas con Discapacidad

## Resultados

Después de extraer los tweets, analizamos la frecuencia de las palabras como se muestra en la siguiente tabla. Identificamos conectores como "la", "en", "de", etc., que se eliminarán para centrarse en las palabras que brindan contexto al contenido del tweet, como se muestra en la segunda tabla.
