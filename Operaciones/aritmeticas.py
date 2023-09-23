from Abstract.abstract import Expression
from Graficas.Arbol import *

class Aritmetica(Expression):
    
    def __init__(self, izquierda, derecha, tipo, fila, columna):
        self.izquierda = izquierda
        self.derecha = derecha
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
    
    def operar(self):
        global grafo
        
        ValorIzq = self.izquierda
        ValorDer = self.derecha
        resultado = None
        
        nodoIzq = None
        nodoDer = None
        
        if isinstance(self.izquierda, Expression):
            
            ValorIzq = self.izquierda.operar()
            nodoIzq = grafo.obtenerUltimoNodo()
        
        else:
            
            ValorIzq = self.izquierda
            nodoIzq = grafo.agregarNodo(str(ValorIzq))
        
        if isinstance(self.derecha, Expression):
            
            ValorDer = self.derecha.operar()
            nodoDer = grafo.obtenerUltimoNodo()
        
        else:
            
            ValorDer = self.derecha
            nodoDer = grafo.agregarNodo(str(ValorDer))
            
        if self.tipo == ('suma' or 'Suma'):
            resultado = ValorIzq + ValorDer
        elif self.tipo == ('resta' or 'Resta'):
            resultado = ValorIzq - ValorDer
        elif self.tipo == ('multiplicacion' or 'Multiplicacion'):
            resultado =  ValorIzq * ValorDer
        elif self.tipo == ('division' or 'Division'):
            resultado = ValorIzq / ValorDer
        elif self.tipo == ('modulo' or 'Modulo'):
            resultado = ValorIzq % ValorDer
        elif self.tipo == ('potencia' or 'Potencia'):
            resultado = ValorIzq ** ValorDer
        elif self.tipo == ('raiz' or 'Raiz'):
            resultado = ValorIzq ** (1/ValorDer)
        elif self.tipo == ('inverso' or 'Inverso'):
            resultado = 1/ValorIzq
        else:
            return None
        
        raiz = grafo.agregarNodo(f"{self.tipo}\\n{str(round(resultado,2))}")
        grafo.agregarArista(raiz,nodoIzq)
        
        if self.derecha != None:
            
            grafo.agregarArista(raiz,nodoDer)
        
        return round(resultado,2)
    
    def __str__(self) -> str:
        return (
            super().__str__()
            + " tipo: "
            + self.tipo
            + " valor1: "
            + str(self.izquierda)
            + " valor2: "
            + str(self.derecha)
        )
        