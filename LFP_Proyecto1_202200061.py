from tkinter import Text
from tkinter import ttk
from tkinter import Tk, messagebox, filedialog
import tkinter as tk
from fileinput import filename
from tkinter.filedialog import askopenfilename
import os
import json
from collections import namedtuple

from Operaciones import *
from Abstract import *
from Graficas.Arbol import *

Tokens = namedtuple("Token", ["valor","fila","columna"])

DicErrores = {
    "errores":[]   
}

configuracion = {
    
    "texto": None,
    "fondo": None,
    "fuente": None,
    "forma": None,
}

ebg = '#000000'
fg = '#FFFFFF'
global nombre_archivo
global opciones
global abrio
global linea
nombre_archivo = ""
abrio = False
global TxtArchivo
global numero_Lin
global numero_Col
global Instruc
global lista_Lexemas
global ContaErrores
global GenerarErrores
global GenerarGrafo
ventana = tk.Tk()

numero_Lin = 1
numero_Col = 1
Lista_Lexemas = []
Instruc = []
ContaErrores = 0
GenerarErrores = 0
GenerarGrafo = 0
linea = ""

def Vista():
    global TxtArchivo
    global opciones
    
    ventana.title("Analizador lexico")
    ventana.geometry("1200x700")
    
    label = tk.Label(ventana,bg = "green")
    label.place(x=0, y=0, width = 1200, height = 50)  
    
    style = ttk.Style()
    style.theme_use('alt')
    
    ventana.option_add('*TCombobox*Listbox*Background', ebg)
    ventana.option_add('*TCombobox*Listbox*Foreground', fg)
    ventana.option_add('*TCombobox*Listbox*selectBackground', fg)
    ventana.option_add('*TCombobox*Listbox*selectForeground', ebg)
    
    style.map('TCombobox', fieldbackground=[('readonly', ebg)])
    style.map('TCombobox', selectbackground=[('readonly', ebg)])
    style.map('TCombobox', selectforeground=[('readonly', fg)])
    style.map('TCombobox', background=[('readonly', ebg)])
    style.map('TCombobox', foreground=[('readonly', fg)]) 
    
    opciones = ttk.Combobox(state = "readonly", values = ["Abrir", "Guardar", "Guardar como", "Salir"])
    opciones.place(x = 420, y = 10, width = 100, height = 30)
    opciones.current(0)
    
    BtnAnalizar = tk.Button(ventana, text = "Analizar", bg = "black", fg = "white", command = ejecutar)
    BtnAnalizar.place(x = 30, y = 10, width = 100, height = 30)
    
    BtnErrores = tk.Button(ventana, text = "Errores", bg = "black", fg = "white", command = JSONErrores)
    BtnErrores.place(x = 160, y = 10, width = 100, height = 30)
    
    BtnReporte = tk.Button(ventana, text = "Reporte", bg = "black", fg = "white", command = Crear_Grafo)
    BtnReporte.place(x = 290, y = 10, width = 100, height = 30)
    
    BtnOpciones = tk.Button(ventana, text = "Seleccionar", bg = "blue", fg = "white", command = Opciones)
    BtnOpciones.place(x = 550, y = 10, width = 100, height = 30)
    
    TxtArchivo = Text(ventana)
    TxtArchivo.config(font = ("Consolas", 10), padx = 10, pady = 10)
    TxtArchivo.place(x = 200, y = 100, width = 800, height = 500)
    
    for i in range(1,41):
        
        TxtArchivo.insert(float(i),str(i)+"."+"\n")
    
    ventana.mainloop()

def Opciones():
    
    global opciones
    global TxtArchivo
    global nombre_archivo
    global abrio
    global linea
    global GenerarGrafo
    global GenerarErrores
    
    if opciones.get() == "Abrir":
        
        linea = ""
            
        Tk().withdraw()
        try:
                
            filename = askopenfilename(title="Seleccione el archivo", filetypes=[('Archivos', f'*.json')])
            partido = filename.split("/")
            nombre_archivo = partido.pop()
                
            with open(filename, encoding='utf-8') as infile:
                    linea = infile.read()
                        
        except:
                
            messagebox.showerror(message = "No selecciono ningun archivo", title = "Error")
            return
        
        TxtArchivo.delete(1.0,41.0)
        TxtArchivo.insert(1.0,linea)
        
        abrio = True
        GenerarGrafo = 0
        GenerarErrores = 0
        
    
    if opciones.get() == "Guardar":
        
       if abrio == True:
     
        f = open(nombre_archivo,"w")
        f.write(TxtArchivo.get(1.0,tk.END))
        f.close()
        linea = TxtArchivo.get(1.0,tk.END)
        messagebox.showinfo(message = "Archivo guardado con exito", title = "Analizador Lexico")
        
       else:
        
        messagebox.showerror(message = "Por favor, primero abra un archivo antes de guardarlo", title = "Analizador Lexico")
           
       
    if opciones.get() == "Guardar como":
        
        if abrio == True:
        
            ventana.archivoNombre = filedialog.asksaveasfilename(title = "Guardar como", initialdir = "LFP_S2_2023_Proyecto1_202200061", defaultextension = ".json", filetypes =[("Archivo json", "*.json")])
            
            print(ventana.archivoNombre)
            partidocomo = ventana.archivoNombre.split("/")
            nombreComo = partidocomo.pop()
            
            f = open(nombreComo,"w")
            f.write(TxtArchivo.get(1.0,tk.END))
            f.close()
            linea = TxtArchivo.get(1.0,tk.END)
            messagebox.showinfo(message = "Archivo guardado con exito", title = "Analizador Lexico")
        
        else:
            
            messagebox.showerror(message = "Por favor, primero abra un archivo antes de guardarlo", title = "Analizador Lexico")
    
    if opciones.get() == "Salir":
        
        exit()

def Instruccion(archivo):
    
    global numero_Lin
    global numero_Col
    global Lista_Lexemas
    global ContaErrores
    apuntador = 0
    lexema = ''
    
    numero_Col = 1
    numero_Lin = 1
    
    while archivo:
        
        char = archivo[apuntador]
        apuntador += 1
        
        if char == '\"':
            
            lexema, archivo = Crear_lexema(archivo[apuntador:])
            
            if lexema and archivo:
                
                numero_Col += 1
                
                l = Tokens(lexema, numero_Lin, numero_Col)
                
                Lista_Lexemas.append(l)
                numero_Col += len(lexema) + 1
                apuntador = 0
         
        elif char.isdigit():
            
            token, archivo = Crear_numero(archivo)
            
            if token and archivo:
                numero_Col += 1
                
                n = Tokens(token, numero_Lin, numero_Col)
                
                Lista_Lexemas.append(n)
                numero_Col += len(str(token)) + 1
                apuntador = 0
        
        elif char in ["{", "}", "[", "]", ",", ":"]:
            
            c = Tokens(char, numero_Lin,numero_Col)
            
            Lista_Lexemas.append(c)
            archivo = archivo[1:]
            apuntador = 0
            numero_Col += 1
        
        elif char == '\t':
            numero_Col +=4
            archivo = archivo[4:]
            apuntador = 0
        
        elif char == '\n':
            archivo = archivo[1:]
            apuntador = 0
            numero_Lin += 1
            numero_Col = 1
        
        elif char == " ":
            
            archivo = archivo[1:]
            numero_Col += 1
            apuntador = 0
            
        else:
            
            ContaErrores +=1
            
            DicErrores["errores"].append({
                
                "No.": ContaErrores,   
                "lexema": char,
                "tipo": "Error lexico",
                "columna": numero_Col,
                "fila": numero_Lin
            })
                        
            archivo = archivo[1:]
            apuntador = 0
            numero_Col += 1
        
   # for lexema in Lista_Lexemas:
    #    print(lexema)

def Crear_lexema(archivo):
    
    global numero_Lin
    global numero_Col
    global Lista_Lexemas
    global ContaErrores
    Columna_Temp = numero_Col
    apuntador = ''
    lexema = ''
    
    for char in archivo:
        
        apuntador += char
        
        if char == '\"':
            
            return lexema, archivo[len(apuntador):]
        
        else:
            
            if Errores_entre_Lexemas(char) == 0:
            
                lexema += char
                Columna_Temp += 1
            
            elif Errores_entre_Lexemas(char) == 1:
                
                Columna_Temp += 1
            
            elif Errores_entre_Lexemas(char) == 2:
                
                Columna_Temp += 1
                
                ContaErrores +=1
                
                DicErrores["errores"].append({
                        
                        "No.": ContaErrores,   
                        "lexema": char,
                        "tipo": "Error lexico",
                        "columna": Columna_Temp,
                        "fila": numero_Lin
                    })
                
    return None, None     
        
def ejecutar():
    
    global GenerarErrores
    global GenerarGrafo
    global Lista_Lexemas
    global Instruc
    
    global linea
    
    tokens = Tokens(None,None,None)
    Lista_Lexemas.clear()
    Instruc.clear()
    
    if linea == "":
    
        messagebox.showerror(message = "No puede analizar el archivo, sin haberlo cargado", title = "Error")
    
    else:
        Instruccion(linea)
        grafo.dot.clear()
        grafo.Configurar(configuracion)
        Realizar_OperR()
        
        GenerarGrafo = 1
        GenerarErrores = 1
        
        return grafo

def Crear_numero(archivo):
    
    numero =''
    apuntador = ''
    decimal = False
    
    for char in archivo:
        
        apuntador += char
        
        if char == '.':
            
            decimal = True
        
        if char == '\"' or char == ' ' or char == '\n' or char == '\t' or char == ",":
            
            if decimal:
                
                return float(numero), archivo[len(apuntador)-1:]
            
            else:
                
                return int(numero), archivo[len(apuntador)-1:]
        
        else:
            
            numero += char   
    
    return None, None

def operar():
    
    global Lista_Lexemas
    global Instruc
    operacion = ''
    n1 = ''
    n2 = ''
    
    while Lista_Lexemas:
        
        lex = Lista_Lexemas.pop(0)
        
        if lex.valor == ('operacion' or 'Operacion'):
            
            Lista_Lexemas.pop(0)
            operacion = Lista_Lexemas.pop(0).valor
        
        elif lex.valor == ('valor1' or 'Valor1'):
            
            Lista_Lexemas.pop(0)
            n1 = Lista_Lexemas.pop(0).valor
            
            if n1 == '[':
                n1 = operar()
        
        elif lex.valor == ('valor2' or 'Valor2'):
            
            Lista_Lexemas.pop(0)
            n2 = Lista_Lexemas.pop(0).valor
            
            if n2 == '[':
                n2 = operar()
        
        elif lex.valor in ["texto","fondo","fuente","forma"]:
            
            Lista_Lexemas.pop(0)
            configuracion[lex.valor] = Lista_Lexemas.pop(0).valor
        
        if operacion and n1 and n2:
            return aritmeticas.Aritmetica(n1, n2, operacion,0,0)
        
        if operacion != '':
            
            if operacion == 'Seno' or operacion == 'seno' or operacion == 'Coseno' or operacion == 'coseno' or operacion == 'Tangente' or operacion == 'tangente':
            
                if n1 != '':
                
                    return trigonometricas.Trigonometrica(n1, operacion,0,0)
    
    return None
            
def Realizar_OperR():
    
    global Instruc
    global grafo
    
    while True:
        
        operacion = operar()
        
        if operacion:
            
            Instruc.append(operacion)
            
        else:
            break
        
    grafo.Configurar(configuracion)
    
    for instruccion in Instruc:
        
        print(instruccion.operar())
        
def JSONErrores():
    
    global GenerarErrores
    
    if GenerarErrores == 1:
    
        with open("RESULTADOS_202200061.json", "w") as file:
        
            json.dump(DicErrores, file, indent = 4)
            messagebox.showinfo(message = "Archivo de errores generado con exito", title = "Generar Errores")
    
    else:
        
        messagebox.showerror(message = "No puede generar el archivo de errores, debe analizar el archivo .json primero", title = "Error")

def Crear_Grafo():
    
    global GenerarGrafo
    
    if GenerarGrafo == 1:
    
        grafo.generarGrafo()  
        messagebox.showinfo(message = "Reporte realizado con exito!", title = "Generar Reporte")
    
    else:
        
        messagebox.showerror(message = "No se puede generar el Reporte, primero debe analizar el archivo .json", title = "Error")

def Errores_entre_Lexemas(char):
    
    if (ord(char) >= 48 and ord(char) <= 57) or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
        
        return 0
    
    elif ord(char) == 58 or ord(char) == 44 or ord(char) == 91 or ord(char) == 93 or ord(char) == 123 or ord(char) == 125 or char == " ":
        
        return 1
    
    else:
        
        return 2
          
Vista()
