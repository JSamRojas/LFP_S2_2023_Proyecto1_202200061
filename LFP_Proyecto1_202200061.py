from tkinter import Text
from tkinter import ttk
from tkinter import Tk, messagebox, filedialog
import tkinter as tk
from fileinput import filename
from tkinter.filedialog import askopenfilename
import os

ebg = '#000000'
fg = '#FFFFFF'
global nombre_archivo
global opciones
global abrio
nombre_archivo = ""
abrio = False
global TxtArchivo
ventana = tk.Tk()

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
    
    BtnAnalizar = tk.Button(ventana, text = "Analizar", bg = "black", fg = "white")
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
           
Vista()
