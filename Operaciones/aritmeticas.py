from Abstract.abstract import Expression

class Aritmetica(Expression):
    
    def __init__(self, izquierda, derecha, tipo, fila, columna):
        self.izquierda = izquierda
        self.derecha = derecha
        self.tipo = tipo
        super().__init__(fila, columna)
    
    def operar(self, arbol):
        
        ValorIzq = ''
        ValorDer = ''
        
        if self.izquierda != None:
            
            ValorIzq = self.izquierda.operar(arbol)
        
        if self.derecha != None:
            
            ValorDer = self.derecha.operar(arbol)
    
        if self.tipo.operar(arbol) == ('suma' or 'Suma'):
            return ValorIzq + ValorDer
        elif self.tipo.operar(arbol) == ('resta' or 'Resta'):
            return ValorIzq - ValorDer
        elif self.tipo.operar(arbol) == ('multiplicacion' or 'Multiplicacion'):
            return ValorIzq * ValorDer
        elif self.tipo.operar(arbol) == ('division' or 'Division'):
            return ValorIzq / ValorDer
        elif self.tipo.operar(arbol) == ('modulo' or 'Modulo'):
            return ValorIzq % ValorDer
        elif self.tipo.operar(arbol) == ('potencia' or 'Potencia'):
            return ValorIzq ** ValorDer
        elif self.tipo.operar(arbol) == ('raiz' or 'Raiz'):
            return ValorIzq ** (1/ValorDer)
        elif self.tipo.operar(arbol) == ('inverso' or 'Inverso'):
            return 1/ValorIzq
        else:
            return None
    
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()
        