import Padrao

class MensagemPadrao(Padrao):

    def __init__(self,menu):
        
        self._mensagem = """
        Deseja voltar a tela principal?
        - [1] Sim
        - [0] Não
        """
        self.menu = menu

    @property
    def mensagem(self):
        return self._mensagem
    
    def mostrarMensagem(self):
        return self.mensagem

    def voltar(self, menu):
        menu.mostrar()

    def sair(self):
        pass