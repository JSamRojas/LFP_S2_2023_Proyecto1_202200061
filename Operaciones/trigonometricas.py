from Abstract.abstract import Expression
from math import *
class Trigonometrica(Expression):
    
    def __init__(self, izquierda, tipo, fila, columna):
        
        self.izquierda = izquierda
        self.tipo = tipo
        
        super().__init__(fila, columna)
    
    def operar(self, arbol):
        
        ValorIzq = ''
        
        if self.izquierda != None:
            
            ValorIzq = self.izquierda.operar(arbol)
    
        if self.tipo.operar(arbol) == ("seno" or "Seno"):
            return sin(ValorIzq)
        elif self.tipo.operar(arbol) == ('coseno' or 'Coseno'):
            return cos(ValorIzq)
        elif self.tipo.operar(arbol) == ('tangente' or 'Tangente'):
            return tan(ValorIzq)
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()