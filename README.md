# Ejercicio Visión computacional

## Descripción
Realizar un algoritmo que clasifique la imagen de un documento en alguna de las siguientes categorías

* INE
* Pasaporte
* Id Colombiana
* Id Chile
* Id Perú

Además detectar los siguientes elementos dentro de la credencial ine mexicana

* **Escudo Nacional**

![imagen escudo nacional](/detector/templates/escudo_aguila.PNG)

* **Franja naranja lateral**

![imagen escudo nacional](/detector/templates/franja_anaranjada.PNG)

* **Mapa de la república mexicana**

![imagen escudo nacional](/detector/templates/mapa_republica_mexicana.PNG)


## Enfoque de la solución

Para detectar los elementos se utiliza opencv para preprocesar las imágenes y detectar bordes que nos permitan ubicar las credenciales dentro de una imagen, la limitación de este enfoque es la calidad de la imagen.

Para buscar los elementos dentro de la INE se utiliza una función de template matching que encuentre la ubicación de estos elementos.

Uno de los requerimientos del ejercicio es utilizar tensorflow para crear una red neuronal que permita clasificar las imágenes en alguna de las categorías antes mencionadas, sin embargo, no existe un dataset adecuado para entrenar una red convolucional, otro enfoque podría ser extraer características como HOG, SIFT o SURF para entrenar un modelo de machine learning, en específico una SVM que permita separar en el espacio de características las de cada uno de los documentos, puesto que en cada credencial varían los datos de las personas y las fotos, lo adecuado sería tener un dataset con mayor volumen y variabilidad de documentos. 