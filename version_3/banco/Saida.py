class Saida:

    def __init__(self,caixa_mensagem):
        
        mensagem = """
        Obrigado por usar nosso sistema! Tenha um bom dia!

        Caso deseje reiniciar a aplicação, basta atualizar a página.
        """
        
        caixa_mensagem.write(mensagem)

    