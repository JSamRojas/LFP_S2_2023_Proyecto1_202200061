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

### Menú Principal

Una vez iniciada la aplicacion, lo primero que encontraremos sera esta ventana, en donde podemos visualizar 4 botones y un listado de opciones, los primeros tres botones estan relacionados al analizador lexico directamente, mientras que el el listado de opciones y el boton de color azul, nos sirven para todo lo relacionado con el archivo .json que vamos a analizar. Cada uno de los botones negros, realizan sus funciones una vez sean oprimidos, pero el listado de opciones (es donde podemos ver la opcion de **Abrir**) funciona con el boton azul de al lado, una vez seleccionado que queremos realizar, deberemos oprimir el boton azul y seguido de esto, la opcion elegida se empezara a ejecutar.

![Manual Técnico](https://i.ibb.co/XXD6mJD/Interfaz-Principal.jpg)

### Listado de opciones
Dentro de las opciones encontramos las siguientes:
*Abrir: esta opcion nos servira para seleccionar el archivo .json que se usara para el analisis, una vez seleccionado el archivo dentro del explorador de archivos, este se cargara en el area de texto que se ubica en el centro de la ventana y una vez se despliegue el archivo .json, entonces podremos editarlo.

*Guardar: si seleccionamos esta opcion, entonces se guardara el archivo que hayamos editado dentro del area de texto, con el mismo nombre que tenia cuando se cargo, cabe resaltar que si no hemos cargado un archivo, entonces nos mostrara un mensaje de error.

*Guardar como: a diferencia de la opcion de **Guardar**, esta opcion nos permite guardar el archivo editado dentro del texto de area con otro nombre y para ingresar el nombre, se nos desplegara el explorador de archivos donde seleccionaremos donde guardar el archivo y el nuevo nombre que le daremos al mismo, al igual que con la anterior opcion, si no hemos cargado el archivo, entonces nos mostrara un mensaje de error.

*Salir: si el usuario selecciona esta opcion, la ventana se cerrara y el programa terminara la ejecucion.

![Manual Técnico](https://i.ibb.co/zXwVQT2/Listado-de-Opciones.jpg)


### Opcion de Analizar

La opcion de **Analizar** la utilizaremos una vez hayamos cargado el archivo y aparezca dentro del area de texto, cabe resaltar que si no hemos cargado el archivo, entonces nos mostrara un mensaje de error el programa. Como su nombre lo indica, este boton nos servira para analizar el archivo .json y una vez se haya terminado de analizar el archivo, entonces nos mostrara un mensaje donde nos indicara que se analizo el archivo con exito.

![Manual Técnico](https://i.ibb.co/f4yhNxQ/Boton-Analizar.jpg)

### Opcion de Errores

La opcion de **Errores** unicamente se utilizara cuando hayamos analizado el archivo .json, si intentamos usarla antes de haber usado la opcion de analizar, entonces nos mostrara un mensaje de error. Esta opcion sirve para generar el archivo .json donde se desplegaran los errores lexicos encontrados durante el analisis del archivo.

![Manual Técnico](https://i.ibb.co/s5fgPDg/Boton-Errores.jpg)

### Opcion de Reporte

La opcion de **Reporte** unicamente se utilizara cuando hayamos analizado el archivo .json, si intentamos usarla antes de haber usado la opcion de analizar, entonces nos mostrara un mensaje de error. Esta opcion sirve para generar la imagen donde iran los diagramas de las operaciones analizadas anteriormente, una vez generada la imagen, se nos desplegara en pantalla para que podamos verla.

![Manual Técnico](https://i.ibb.co/Pj6d2Kh/Boton-Reporte.jpg)

---

