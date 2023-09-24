# Lenguajes Formales y de Programacion
## Proyecto No.1
### Segundo Semestre
```js
Universidad San Carlos de Guatemala
Programador: Jonatan Samuel Rojas Maeda
Carne: 202200061
Correo: jonas23450947@gmail.com
```
---
## Objetivos
* Objetivos Generales
    *Que el estudiante cree una herramienta la cual sea capaz de reconocer un lenguaje, dado por medio de un analizador léxico el cual cumple con las reglas establecidas, manejando la lectura y escritura de archivos para el manejo de la información. A través de un entorno gráfico.

* Objetivos Especificos
    *Implementar por medio de estados un analizador léxico.
    *Programar un Scanner para el análisis léxico.
    *Construir un scanner basándose en un autómata finito determinístico.
    *Crear una herramienta para interactuar de forma visual con el usuario con Tkinter.
    *Crear diagramas con la librería Graphviz.
---
## Descripción del Proyecto

### Librerias Utilizadas
* from tkinter import Text
* from tkinter import ttk
* from tkinter import Tk, messagebox, filedialog
* import tkinter as tk
* from fileinput import filename
* from tkinter.filedialog import askopenfilename
* import os
* import json
* from collections import namedtuple
* from math import *
* from abc import ABC, abstractmethod

### Menú Principal

Para la ventana principal, se hizo uso de la libreria de **Tkinter**, la cual ofrece una amplia cantidad de objetos visuales que son muy interactivos con el usuario, como los botones, las listas de opciones (Combobox) y tambien las etiquetas o labels. Para empezar siempre se declara una ventana o Frame principal que sera el que se utilizara para colocar cada uno de nuestros objetos, una vez declarada nuestra ventana principal, se utilizo las herramientas proporcionadas por Tkinter para generar cada uno de los elementos que conforman la interfaz grafica.

![Manual Técnico](https://i.ibb.co/jvtMX0q/Ventana-Principal-tkinter.jpg)

### Listado de Opciones

Para que el listado de opciones funcione, utilizamos un boton el cual cada vez que se presione, ejecutara la funcion seleccionada dentro del combobox, entonces de esta forma evitamos complicaciones a la hora de realizar la funcion seleccionada por el usuario. Para saber cual fue la opcion seleccionada, se utilizo un metodo que trae el combobox llamado **.get()** el cual nos regresa el valor de la opcion seleccionada, entonces dentro de la funcion **Opciones()** solamente comparamos cada una de las opciones para saber cual fue la que selecciono y dependiendo de eso, entonces el programa ejecutara la parte del codigo correspondiente.

![Manual Técnico](https://i.ibb.co/HtCqrm3/Programacion-de-Combobox.jpg)

### Instrucciones

Dentro de la funcion **Instrucion()** es donde formaremos todos nuestros lexemas, esta funcion recibe por parametro un string, el cual sera el archivo .json que habra cargado el usuario con anterioridad. Para armar todos los lexemas, primero necesitamos hacer unas comparaciones para poder saber que tipo de lexema sera el que armaremos, si es una palabra, primero validaremos si el char que lee el programa es igual a las comillas dobles, ya que todas las palabras estan encerradas en comillas, por lo que sera enviado a la funcion de **Crear_lexema()**, mas adelante explicaremos que se hace en esa funcion a detalle. Ahora si lo que armaremos es un numero, entonces primero validamos con la funcion nativa de python si el char es un digito, si lo es, entonces sera enviado a la funcion **Crear_numero()**. Ambas funciones, recibiran como parametro un string, el cual tambien sera el archivo .json, pero para poder asegurarnos de que se leera la palabra y el numero que toca, entonces usaremos una contadora, la cual ira aumentando con cada caracter que leamos y cuando sea el momento de enviar el string a la funcion, acortaremos el string usando la contadora anterior. 
Dentro de esta misma funcion, validaremos si lo que leemos es algun parentesis, una llave o un corchete, al igual que si es una coma o puntos dobles, pero si no es ninguno de los anteriores, entonces sera tomado como error lexico y agregaremos el caracter como error al diccionario, el cual despues sera convertido a archivo json.

![Manual Técnico](https://i.ibb.co/9vMC2DV/funcion-Instruccion.jpg)

### Crear lexema

la funcion **Crear_lexema()** recibe por parametro un string, el cual sera el archivo json acortado hasta despues de la primera comilla con la que se encuentre, ya que esta funcion nos ayudara a armar la palabra que esta encerrada en esas comillas, por lo que mientras el caracter que esta leyendo no sea otra comilla, entonces la funcion seguira armando la palabra, caracter a caracter, tambien dentro de esta funcion validaremos que el caracter que se lea, sea un numero o una letra, ya que si es otro tipo de caracter, este debe ser considerado un error lexico. Una vez encuentre la siguiente comilla, entonces regresara la palabra ya armada y tambien el string del archivo json, acortado hasta la siguiente comilla, el cual se estara llevando un control con una contadora.

![Manual Técnico](https://i.ibb.co/sCRY5Dm/funcion-crear-lexema.jpg)

### Crear Numero

En la funcion **Crear_numero()** recibe por parametro un string, el cual es el archivo .json, como en la anterior funcion, esta tambien esta acortada hasta el primer digito, por lo que mientras el caracter no sea un salto de linea o una coma, entonces el numero se seguira creando. Tambien validaremos si el caracter no es un punto, para saber si el numero que estamos formando es un numero decimal o un numero entero, y una vez hayamos creado el numero, regresamos el numero formado y archivo acortado hasta la coma o el salto de linea.

![Manual Técnico](https://i.ibb.co/qFx1X67/funcion-crear-numero.jpg)

### Operaciones

Dentro de la funcion **operar()** es donde realizaremos todas las operaciones matematicas que hayamos creado en la funcion de **Instrucciones()**, en la cual, ademas de crear los lexemas, los agregamos a una tupla la cual nos ayudara a crear la estructura de los tokens y esta estructura sera almacenada en una lista, la cual sera la que recorreremos elemento a elemento para averiguar que tipo de dato es el que estamos leyendo, si es una instruccion, un numero o algun signo. Si el valor del elemento es igual a la palabra "Operacion" entonces lo que haremos sera utilizar la funcion de .pop() para sacar el siguiente valor, que es los dos puntos y asi no tener ningun error, y luego almacenaremos el siguiente valor, el cual ya debe ser el nombre de la operacion a realizar. Si no es igual a esa palabra, entonces validaremos si no es igual a "valor1" o "valor2", si es igual a alguna de estas dos, entonces realizaremos un .pop() de nuevo para sacar el doble punto de nuevo y lo siguiente sera guardar en una variable el valor siguiente, que debe ser o un numero o un corchete de apertura, si es un numero, entonces continuaremos el flujo, pero si es un corchete de apertura, quiere decir que uno de los valores es otra operacion, por lo que el valor de la variable sera la misma funcion **operar()**, asi que se tomara de manera recursiva. Al final se realiza una comparacion para saber si hay dos valores y una operacion, si estan, entonces enviaremos a otra funcion llamada **Aritmetica()**, la cual nos regresara el resultado de la operacion enviada. Si esta operacion es una trigonometrica (seno, coseno o tangente), entonces lo enviaremos a la funcion **Trigonometrica()** la cual nos devolvera, igual que la anterior, el resultado de dicha operacion. Asi mismo, en esta funcion, guardaremos las instrucciones para lo que es el archivo de reportes.

![Manual Técnico](https://i.ibb.co/XDg5CL4/funcion-operar.jpg)

### Archivo de Errores

La funcion **JSONErrores()** es donde generaremos el archivo .json de los errores lexicos, para generar el archivo de manera sencilla, todos los errores lexicos se guardaran en un Diccionario, al cual solamente tendremos que aplicarle la funcion .dump de la libreria json y automaticamente convertira el Diccionario, en un archivo json. Cabe resaltar que se valida si el archivo ya fue analizado, ya que si no es analizado, entonces se mostrara un messagebox en el cual mosrtaremos un mensaje de error.

![Manual Técnico](https://i.ibb.co/6JbD9DP/funcion-JSONErrores.jpg)

### Generar Reporte

La funcion de **Crear_Grafo()** simplemente invocara a la funcion **generarGrafo()**, la cual nos creara el archivo .dot para que graphviz pueda generar el archivo pdf con el reporte de las operaciones matematicas. Al igual que con la funcion de los errores, esta tambien valida si el archivo ya fue analizado, si es asi, entonces podra generar el reporte, de lo contrario, se mostrara el messagebox de error en el cual informara que primero se debe analizar el archivo.

![Manual Técnico](https://i.ibb.co/LnH7f3p/funcion-generar-grafo.jpg)

### Clase Abstracta

Para trabajar con lo que es tener un grafo binario, entonces usaremos una clase abstracta, la cual nos ayudara con una plantilla y luego heredaremos de esta misma a otras clases, en las cuales realizaremos las operaciones aritmeticas correspondientes. En este caso tenemos la funcion **operar()** como un metodo abstracto, la cual sera una base para utilizarla en las demas clases.

![Manual Técnico](https://i.ibb.co/0y7Vw7H/clase-abstracta.jpg)

### Clase aritmeticas

Dentro de esta clase, que hereda de la clase **Expression()**, es donde realizaremos las operaciones matematicas normales, las cuales son las compuestas por dos valores, un valor izquierdo y un valor derecho, el tipo de operacion y un valor de fila y columna. Entonces primero tenemos la funcion **operar()** donde validaremos que tanto el valor derecho, como el izquierdo, no sean una funcion, ya que si son una funcion, entonces volveremos a llamar a la misma funcion, para que opere los dos valores que tiene dentro de si mismo, ya que es otra operacion y si no son operaciones ninguno de los dos, entonces procederemos a operar ambos y usaremos la funcion **agregarNodo()** para agregar ambos valores como nodos en el grafo de reporte. Una vez realizada la operacion, entonces agregaremos crearemos una raiz la cual constara del nombre de la operacion y el resultado y agregaremos esa raiz, acompañado del nodo izquierdo y si el derecho es distinto de None, lo agregaremos tambien. Por ultimo regresaremos el resultado de la operacion para que sea guardado en su respectiva lista, redondeado a 2 decimales.

![Manual Técnico](https://i.ibb.co/6tYmqhJ/clase-aritmeticas-1.jpg)
![Manual Técnico](https://i.ibb.co/HqV3Kvv/clase-aritmeticas-2.jpg)

### Clase trigonometricas

Dentro de esta clase, que hereda de la clase **Expression()**, es donde realizaremos las operaciones trigonometricas solicitadas, las cuales son seno, coseno y tangente. Al igual que con la anterior clase, esta recibe por parametro lo mismo, solo que esta recibe solamente un valor, ya que estas operaciones se hacen con un solo valor.Entonces primero tenemos la funcion **operar()** donde verificamos que el valor enviado no sea una funcion, si lo es, entonces volveremos a llamar a la misma funcion para que opere los dos valores que tiene dentro el valor, de lo contrario, agregaremos el nodo al grafo y procederemos a operar el valor. Una vez con el resultado crearemos una raiz, con el resultado y el valor que se le aplico la funcion trigonometrica y tambien regresaremos el resultado de la funcion redondeado a 2 decimales.

![Manual Técnico](https://i.ibb.co/jkQG6fr/funcion-trigonometricas.jpg)

### Clase Arbol

Dentro de esta clase, es donde generaremos el reporte en forma de grafo utilizando la libreria de graphviz. Iniciando con la funcion **Configurar()**, la cual nos servira para almacenar los valores de las configuraciones que vienen en el archivo .json, luego tenemos la funcion **agregarNodo()** la cual recibe por parametro el valor del nodo y generara el nodo con el nombre que le corresponde segun la contadora y el valor sera el que recibimos por parametro. Luego esta la funcion **agregarArista()** que recibe dos nodos por parametro, y esta creara una arista entre dos nodos, los cuales por lo general seran el nodo raiz y el nodo hijo. Luego esta la funcion **generarGrafo()**, la cual sera invocada cuando la persona desee generar el reporte y lo que hara sera crear el archivo .dot y seguido, el .pdf donde ya veremos al anterior archivo interpretado por graphviz. Por ultimo, tenemos la funcion **ObtenerUltimoNodo()** la cual creara un nodo con el nombre anterior y es asi, ya que se invoca cuando dentro de uno de los dos valores, tenemos una funcion, por lo que creamos ese nodo para poder enlazar ambos numeros despues.

![Manual Técnico](https://i.ibb.co/s1bf6sm/clase-arbol.jpg)

---