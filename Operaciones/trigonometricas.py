from Abstract.abstract import Expression
from math import *
from Graficas.Arbol import *

class Trigonometrica(Expression):
    
    def __init__(self, izquierda, tipo, fila, columna):
        
        self.izquierda = izquierda
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
    
    def operar(self):
        
        ValorIzq = self.izquierda
        
        nodo = None
        resultado = None
        
        if isinstance(self.izquierda, Expression):
            
            ValorIzq = self.izquierda.operar()
            nodo = grafo.obtenerUltimoNodo()
        
        else:
            
            ValorIzq = self.izquierda
            nodo = grafo.agregarNodo(str(ValorIzq))
            
    
        if self.tipo == ("seno" or "Seno"):
            
            resultado = sin(ValorIzq)
            
        elif self.tipo == ('coseno' or 'Coseno'):
            
            resultado = cos(ValorIzq)
            
        elif self.tipo == ('tangente' or 'Tangente'):
            
            resultado = tan(ValorIzq)
        
        raiz = grafo.agregarNodo(f"{self.tipo}\\n{str(round(resultado,2))}")
        grafo.agregarArista(raiz, nodo)
        
        return round(resultado,2)