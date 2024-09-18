from version_3.banco.Menu import Menu
from version_3.banco.CPF import CPF, CpfEntrada
from version_3.banco.Saida import Saida

class MenuInicial(Menu):

    def __init__(self):
        super().__init__()
        self._opcoes = """
        - [1] Entrar como cliente
        - [2] Cadastrar novo cliente
        - [0] Sair  
        """

    def mostrarMensagem(self):
        super().mostrarMensagem(apresentacao = "Bem vindo ao banco XPTO!")

    def executarOpcoes(self):

        caixa_texto = self.caixa_texto.value

        if caixa_texto == "1":
            self.cadastrarNovoDadoCliente(CpfEntrada())
        if caixa_texto == "2":
            self.cadastrarNovoDadoCliente(CPF())
        if caixa_texto == "0":
            Saida(self.caixa_mensagem)



    def cadastrarNovoDadoCliente(self,digito):

        caixa_mensagem = self.caixa_mensagem

        caixa_mensagem.write(digito.mensagem())