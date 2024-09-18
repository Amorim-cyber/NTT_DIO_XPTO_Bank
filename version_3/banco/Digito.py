from abc import ABC, abstractmethod

class Digito(ABC):

    @property
    @abstractmethod
    def mensagem(self):
        pass

    @abstractmethod
    def mostrarErro(self,erro):
        pass