# Maestr-a-UNI-jne-neutralidad-finetuning

\# Fine-tuning de modelo de lenguaje para neutralidad electoral



\## Descripción



Este repositorio contiene la estructura inicial del proyecto de tesis orientado al ajuste fino de un modelo de lenguaje natural para apoyar la evaluación automatizada y asistida de proyectos de resolución en materia de neutralidad electoral en el Perú.



\## Objetivo general



Diseñar, ajustar y validar un modelo de lenguaje natural mediante fine-tuning, utilizando resoluciones y documentos normativos electorales, para apoyar la evaluación automatizada de proyectos de resolución en materia de neutralidad electoral.



\## Componentes del proyecto



\- Ingesta reproducible de documentos oficiales.

\- Construcción de dataset jurídico-electoral.

\- Preprocesamiento y estructuración de datos.

\- Fine-tuning del modelo de lenguaje.

\- Recuperación documental complementaria para trazabilidad normativa.

\- Evaluación automática y evaluación experta.



\## Estructura del repositorio



\- `config/`: configuración de fuentes documentales.

\- `data/raw/`: documentos originales descargados.

\- `data/processed/`: documentos procesados y segmentados.

\- `data/training/`: dataset preparado para fine-tuning.

\- `scripts/`: scripts reproducibles.

\- `src/`: módulos principales del sistema.

\- `notebooks/`: exploración y pruebas iniciales.

\- `docs/`: documentación técnica y metodológica.

\- `outputs/`: logs, modelos y reportes.

\- `tests/`: pruebas básicas del sistema.



\## Ejecución inicial



Instalar dependencias:



```bash

pip install -r requirements.txt

