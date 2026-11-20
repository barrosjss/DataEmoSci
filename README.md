# DataEmoSci

**Análisis de sentimiento en redes sociales para el turismo accesible de personas con discapacidad.**

Repositorio del trabajo realizado con el **semillero de investigación de la Universidad Libre – Seccional Barranquilla** (2023). Reúne dos partes:

1. **La capacitación en Procesamiento de Lenguaje Natural (NLP)** que recibimos en el semillero: cuatro encuentros con notebooks, talleres, datasets y presentaciones.
2. **La investigación aplicada**: extracción de publicaciones de Twitter/X y análisis de sentimiento sobre turismo accesible.

La capacitación cierra con un prototipo (Twitter + limpieza de texto + bigramas + VADER). Ese prototipo es la base técnica de la investigación.

## Estructura

```
DataEmoSci/
├── capacitacion-nlp/                  # Curso de NLP del semillero (4 encuentros)
│   ├── 01-fundamentos/                # Python para texto, archivos, PDFs, regex
│   ├── 02-normalizacion/              # spaCy, tokenización, stemming, lemas, stop words
│   ├── 03-vectorizacion/              # scikit-learn, BoW, TF-IDF, clasificación
│   ├── 04-modelos/                    # LDA, NMF, word vectors, VADER, prototipo
│   ├── datos/                         # Datasets usados en los notebooks
│   ├── presentaciones/                # Diapositivas de los encuentros 3 y 4
│   ├── entorno-original-curso.yml     # Entorno conda original (2023, referencia)
│   └── README.md                      # Temario detallado
├── investigacion-turismo-accesible/   # Proyecto de investigación
│   ├── notebooks/
│   └── README.md                      # Objetivos, metodología y avances
├── .env.example                       # Plantilla de credenciales de la API de X
├── requirements.txt                   # Dependencias actualizadas
└── LICENSE                            # MIT
```

## Cómo empezar

```bash
# 1. Crear entorno
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2. Modelos de spaCy y recursos de NLTK
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
python -m spacy download es_core_news_md
python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('stopwords')"

# 3. Credenciales (solo para los notebooks que usan la API de X/Twitter)
cp .env.example .env                 # completar con tus llaves; .env no se sube a git

# 4. Abrir los notebooks
jupyter lab
```

Los notebooks leen las credenciales con `os.getenv(...)`. Para cargarlas desde `.env`, exporta las variables en la terminal antes de abrir Jupyter (`set -a; source .env; set +a`) o usa `python-dotenv`.

## Rutas de aprendizaje

| Si quieres...                               | Empieza por                                                                                      |
|---------------------------------------------|--------------------------------------------------------------------------------------------------|
| Repasar el curso desde cero                 | [`capacitacion-nlp/README.md`](capacitacion-nlp/README.md)                                       |
| Ver el análisis de sentimiento en acción    | [`04-modelos/03-analisis-de-sentimiento.ipynb`](capacitacion-nlp/04-modelos/03-analisis-de-sentimiento.ipynb) |
| Ver el prototipo con tweets                 | [`04-modelos/04-prototipo-sentimiento-twitter.ipynb`](capacitacion-nlp/04-modelos/04-prototipo-sentimiento-twitter.ipynb) |
| Conocer la investigación                    | [`investigacion-turismo-accesible/README.md`](investigacion-turismo-accesible/README.md)         |

## Créditos

- Semillero de investigación, Universidad Libre – Seccional Barranquilla.
- Gran parte del material de la capacitación es una adaptación al español de material de cursos públicos de NLP con Python (spaCy, NLTK, scikit-learn).
- Autor del repositorio: Jesús Barros.

## Licencia

[MIT](LICENSE). Los datasets de `capacitacion-nlp/datos/` conservan sus licencias originales (ver [`capacitacion-nlp/datos/README.md`](capacitacion-nlp/datos/README.md)).
