import MensagemPadrao

class Extrato(MensagemPadrao):
    
    def __init__(self,menu):
        
        self._mensagem = ""
        self.menu = menu

    @property
    def mensagem(self):
        return self._mensagem
    
    def mostrarMensagem(self):
        return self.mensagem