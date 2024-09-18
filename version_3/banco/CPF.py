from version_3.banco.Dados import Dados

class CPF(Dados):

    def __init__(self):
        super().__init__()
        self._mensagem = super().mensagem() + 'o CPF que deseja adicionar:'

    def mensagem(self):

        return self._mensagem
    
    def mostrarErro(self, erro):
        return super().mostrarErro(erro)
    
class CpfEntrada(Dados):

    def __init__(self):
        super().__init__()
        self._mensagem = super().mensagem() + 'o CPF cadastrado:'

    def mensagem(self):
        return self._mensagem