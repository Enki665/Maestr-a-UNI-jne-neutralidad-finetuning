\# Criterios del dataset



\## Objetivo del dataset



El dataset tiene como finalidad reunir documentos normativos, guías oficiales, reglamentos y resoluciones públicas vinculadas a la neutralidad electoral en el Perú, con el propósito de preparar información para el fine-tuning de un modelo de lenguaje y para la recuperación documental complementaria.



\## Criterios de inclusión



Se incluirán documentos que cumplan uno o más de los siguientes criterios:



1\. Normas oficiales vinculadas al deber de neutralidad electoral.

2\. Guías emitidas por instituciones públicas sobre neutralidad electoral.

3\. Reglamentos del Jurado Nacional de Elecciones relacionados con propaganda electoral, publicidad estatal o neutralidad.

4\. Resoluciones públicas del JNE que desarrollen criterios sobre neutralidad electoral.

5\. Documentos disponibles en fuentes oficiales o repositorios públicos verificables.



\## Criterios de exclusión



Se excluirán:



1\. Documentos sin fuente verificable.

2\. Documentos duplicados.

3\. Noticias, opiniones, notas de prensa o comentarios no oficiales.

4\. Documentos incompletos o ilegibles.

5\. Documentos que contengan datos sensibles que no puedan ser anonimizados.



\## Formato esperado para fine-tuning



Cada ejemplo del dataset de entrenamiento podrá tener la siguiente estructura:



```json

{

&#x20; "instruction": "Evalúa el siguiente caso en materia de neutralidad electoral.",

&#x20; "input": "Texto del caso, proyecto de resolución o resumen de hechos.",

&#x20; "output": "Análisis esperado, posible infracción, fundamento normativo y recomendación."

}

