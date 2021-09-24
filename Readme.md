# Proceso de obtención del corpus:
Scraping de la coleccion digital del [Museo de Museo de Arte Latinoamericano
de Buenos Aires](https://coleccion.malba.org.ar/)

Al momento de realizar este práctico la colección cuenta con 569 obras, de las cuales 277 tienen alguna clase de texto que las describe


En scrapping_malba.py se encuentra el código utilizado para el scraping.

# Limpieza de los textos

En una primera instancia exploratoria vamos a convertir todas las palabras a minúscula, eliminando signos de puntuación.

Además de eso, vamos a separar los documentos en oraciones. 

Para vectorizar el texto con TFIDF vamoa a realizar el siguiente preproceso:

1. Lowercase a todo el texto
2. Tokenizamos las palabras, y luego lemmatizamos.
3. Nos deshacemos de stopwords definidas en NLTK.
4. Calculamos la matriz tfidf deshaciendonos de palabras que aparecen solamente 1 vez
5. Clustering! (Ya vemos cual, alguno para alta dimensionalidad capaz)

Vamos a probar 2 formas de vectorizar, cada cual con su limpieza distinta:



1. TFIDF: para hacer estos vectores vamos a preprocesar el texto normalizando 