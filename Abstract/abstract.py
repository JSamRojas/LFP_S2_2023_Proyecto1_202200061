from abc import ABC, abstractmethod

class Expression(ABC):
    
    @abstractmethod
    def operar(self, arbol):
        pass
    