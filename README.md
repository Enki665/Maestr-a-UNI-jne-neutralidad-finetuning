# Maestría-UNI-jne-neutralidad-finetuning

# Fine-tuning de modelo de lenguaje para neutralidad electoral

## Descripción

Este repositorio contiene la estructura inicial del proyecto de tesis orientado al ajuste fino de un modelo de lenguaje natural para apoyar la evaluación automatizada y asistida de proyectos de resolución en materia de neutralidad electoral en el Perú.

El proyecto se desarrolla en el marco de una investigación aplicada en inteligencia artificial, con énfasis en procesamiento de lenguaje natural, fine-tuning de modelos de lenguaje, construcción de dataset jurídico-electoral y recuperación documental complementaria para trazabilidad normativa.

---

## Objetivo general

Diseñar, ajustar y validar un modelo de lenguaje natural mediante fine-tuning, utilizando resoluciones y documentos normativos electorales, para apoyar la evaluación automatizada y asistida de proyectos de resolución en materia de neutralidad electoral en el Perú.

---

## Enfoque del proyecto

El proyecto tendrá dos componentes principales:

1. **Fine-tuning del modelo de lenguaje**

   El modelo será ajustado con un dataset especializado construido a partir de documentos normativos, guías oficiales, reglamentos y resoluciones públicas relacionadas con neutralidad electoral.

2. **Recuperación documental complementaria**

   Se implementará un componente de recuperación de información para identificar normas, fragmentos y precedentes relevantes que permitan sustentar las respuestas generadas por el modelo.

---

## Fuentes iniciales del dataset

El dataset estará compuesto inicialmente por:

- Decreto Supremo N.° 054-2025-PCM.
- Guía de Neutralidad Electoral de la Presidencia del Consejo de Ministros.
- Reglamento sobre propaganda electoral, publicidad estatal y neutralidad en periodo electoral del Jurado Nacional de Elecciones.
- Resoluciones públicas del Jurado Nacional de Elecciones vinculadas a neutralidad electoral.

---

## Estructura del repositorio

```text
Maestr-a-UNI-jne-neutralidad-finetuning/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── config/
│   └── sources.yaml
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── training/
│   └── metadata/
│
├── scripts/
│   ├── ingest_v0.py
│   ├── preprocess_v0.py
│   └── build_dataset_v0.py
│
├── src/
│   ├── ingestion/
│   ├── preprocessing/
│   ├── finetuning/
│   ├── retrieval/
│   └── evaluation/
│
├── notebooks/
│   └── 01_exploracion_dataset.ipynb
│
├── docs/
│   ├── plan_recuperacion.md
│   ├── criterios_dataset.md
│   └── decisiones_tecnicas.md
│
├── tests/
│   └── test_ingestion.py
│
└── outputs/
    ├── logs/
    ├── models/
    └── reports/
