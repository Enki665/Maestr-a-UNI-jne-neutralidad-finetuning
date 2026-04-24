\# Plan de recuperación de información



\## Objetivo



Diseñar e implementar una primera versión del componente de recuperación documental para identificar normas, guías, reglamentos y resoluciones relevantes sobre neutralidad electoral.



Este componente complementará el fine-tuning del modelo de lenguaje, proporcionando evidencia verificable para sustentar las respuestas generadas.



\## Relación con el proyecto de tesis



El proyecto busca desarrollar un modelo de lenguaje ajustado mediante fine-tuning para apoyar la evaluación automatizada y asistida de proyectos de resolución en materia de neutralidad electoral.



La recuperación documental permitirá:



1\. Ubicar fragmentos normativos relevantes.

2\. Recuperar precedentes o criterios del JNE.

3\. Sustentar las respuestas del modelo.

4\. Reducir afirmaciones sin respaldo.

5\. Mejorar la trazabilidad jurídica.



\## Flujo de recuperación



```text

Documento original

&#x20;     ↓

Extracción de texto

&#x20;     ↓

Limpieza y normalización

&#x20;     ↓

Segmentación en fragmentos

&#x20;     ↓

Generación de embeddings

&#x20;     ↓

Indexación vectorial

&#x20;     ↓

Consulta del usuario

&#x20;     ↓

Recuperación top-k

&#x20;     ↓

Respuesta con evidencia

