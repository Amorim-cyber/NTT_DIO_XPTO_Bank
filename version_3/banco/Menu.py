from pyscript import Element

class Menu:

    def __init__(self):
        self._clientes = []
        self._cliente = None
        self._caixa_mensagem = Element("caixa_mensagem")
        self._caixa_texto = Element("caixa_texto")

        self._opcoes = """
        - [1] Mostrar Extrato 
        - [2] Realizar Saque 
        - [3] Realizar Deposito
        - [4] Cadastrar nova conta
        - [5] Mostrar dados
        - [0] Sair  
        """

    @property
    def caixa_texto(self):
        return self._caixa_texto
    
    @property
    def caixa_mensagem(self):
        return self._caixa_mensagem

    def mostrarMensagem(self,apresentacao):

        caixa_mensagem = self._caixa_mensagem

        mensagem = f"""{apresentacao}
                
                O que deseja fazer? 
                {self._opcoes}"""
        
        caixa_mensagem.write(mensagem)

        

    def mostrarExtrato():
        pass

    def realizarSaque():
        pass

    def realizarDeposito():
        pass

    def cadastrarNovaConta():
        pass

    def mostrarDados():
        pass

    def mostrarErro():
        pass

    def sair():
        pass
