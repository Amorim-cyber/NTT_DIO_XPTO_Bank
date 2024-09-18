from abc import ABC, abstractmethod

class Padrao(ABC):

    @property
    @abstractmethod
    def mensagem(self):
        pass

    @abstractmethod
    def mostrarMensagem(self):
        pass

    @abstractmethod
    def voltar(self):
        pass

    @abstractmethod
    def sair(self):
        pass