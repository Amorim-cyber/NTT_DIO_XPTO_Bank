from version_3.banco.Digito import Digito

class Dados(Digito):

    def __init__(self):
        self._mensagem = 'Digite '

    def mensagem(self):
        return self._mensagem
    
    def mostrarErro(self, erro):
        return super().mostrarErro(erro)