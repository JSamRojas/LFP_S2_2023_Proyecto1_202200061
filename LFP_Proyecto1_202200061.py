from tkinter import Text
from tkinter import ttk
from tkinter import Tk, messagebox, filedialog
import tkinter as tk
from fileinput import filename
from tkinter.filedialog import askopenfilename
import os

from Operaciones import *
from Abstract.lexema import *
from Abstract.numeros import *

DicErrores = {
    "errores":[]   
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
ventana = tk.Tk()

numero_Lin = 1
numero_Col = 1
Lista_Lexemas = []
Instruc = []

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
    
    BtnErrores = tk.Button(ventana, text = "Errores", bg = "black", fg = "white")
    BtnErrores.place(x = 160, y = 10, width = 100, height = 30)
    
    BtnReporte = tk.Button(ventana, text = "Reporte", bg = "black", fg = "white")
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
        abrio == True
    
    if opciones.get() == "Guardar":
        
       if abrio == True:
     
        f = open(nombre_archivo,"w")
        f.write(TxtArchivo.get(1.0,tk.END))
        f.close()
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
            messagebox.showinfo(message = "Archivo guardado con exito", title = "Analizador Lexico")
        
        else:
            
            messagebox.showerror(message = "Por favor, primero abra un archivo antes de guardarlo", title = "Analizador Lexico")
    
    if opciones.get() == "Salir":
        
        exit()

def Instruccion(archivo):
    
    global numero_Lin
    global numero_Col
    global Lista_Lexemas
    apuntador = 0
    lexema = ''
    
    while archivo:
        
        char = archivo[apuntador]
        apuntador += 1
        
        if char == '\"':
            
            lexema, archivo = Crear_lexema(archivo[apuntador:])
            
            if lexema and archivo:
                
                numero_Col += 1
                
                l = Lexema(lexema, numero_Lin, numero_Col)
                
                Lista_Lexemas.append(l)
                numero_Col += len(lexema) + 1
                apuntador = 0
         
        elif char.isdigit():
            
            token, archivo = Crear_numero(archivo)
            
            if token and archivo:
                numero_Col += 1
                
                n = Numero(token, numero_Lin, numero_Col)
                
                Lista_Lexemas.append(n)
                numero_Col += len(str(token)) + 1
                apuntador = 0
        
        elif char == '[' or char == ']':
            
            c = Lexema(char, numero_Lin,numero_Col)
            
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
        else:
            archivo = archivo[1:]
            apuntador = 0
            numero_Col += 1
    
    for lexema in Lista_Lexemas:
        print(lexema)

def Crear_lexema(archivo):
    
    global numero_Lin
    global numero_Col
    global Lista_Lexemas
    apuntador = ''
    lexema = ''
    
    for char in archivo:
        
        apuntador += char
        
        if char == '\"':
            return lexema, archivo[len(apuntador):]
        
        else:
            
            lexema += char 
    
    return None, None     
        
def ejecutar():
    global linea
    
    Instruccion(linea)
    Realizar_OperR()

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
    hacer = ""
    valorn1 = ""
    valorn2 = ""
    tipooper = ""
    
    while Lista_Lexemas:
        
        lex = Lista_Lexemas.pop(0)
        
        hacer = lex.operar(None)
        
        if hacer == ('operacion' or 'Operacion'):
            
            operacion = Lista_Lexemas.pop(0)
            tipooper = operacion.operar(None)
        
        elif hacer == ('valor1' or 'Valor1'):
            
            n1 = Lista_Lexemas.pop(0)
            valorn1 = n1.operar(None)
            
            if valorn1 == '[':
                n1 = operar()
        
        elif hacer == ('valor2' or 'Valor2'):
            
            n2 = Lista_Lexemas.pop(0)
            valorn2 = n2.operar(None)
            
            if valorn2 == '[':
                n2 = operar()
        
        
        
        if operacion and n1 and n2:
            return aritmeticas.Aritmetica(n1, n2, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n2.getFila()}:{n2.getColumna()}')
        
        if operacion != '':
            
            if tipooper == 'Seno' or tipooper == 'seno' or tipooper == 'Coseno' or tipooper == 'coseno' or tipooper == 'Tangente' or tipooper == 'tangente':
            
                if n1 != '':
                
                    return trigonometricas.Trigonometrica(n1, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
    
    return None
            
def Realizar_OperR():
    
    global Instruc
    
    while True:
        
        operacion = operar()
        
        if operacion:
            
            Instruc.append(operacion)
            
            print("Realizo la operacion")
            
        else:
            break
    
    for instruccion in Instruc:
        print(instruccion.operar(None))
        
            
Vista()
