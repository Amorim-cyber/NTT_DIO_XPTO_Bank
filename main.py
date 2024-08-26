loop = True 

mensagem_boas_vindas = """
Olá Usuário! Bem vindo ao banco XPTO!

O que deseja fazer?

- [1] Ver Saldo disponível
- [2] Realizar Saque 
- [3] Realizar Deposito
- [0] Sair
"""

def mostrar_mensagem_padrao(mensagem):

    mensagem_padrao = f"""
    {mensagem}

    Deseja voltar a tela principal?
    - [1] Sim
    - [0] Não
    """
    opcao_mensagem = input(mensagem_padrao)

    if opcao_mensagem == "1":
        return
    elif opcao_mensagem == "0":
        sair()
    else:
        mostrar_erro()

def mostrar_saldo():
    mostrar_mensagem_padrao("Mostrando saldo...")
    
def sacar_valor():
    mostrar_mensagem_padrao('Sacando valor...')

def depositar_valor():
    mostrar_mensagem_padrao('Depositando valor...')

def mostrar_erro():
    mostrar_mensagem_padrao('Opção inválida! por favor digitar as opções indicadas entre [].')

def sair():
    global loop

    mensagem_saida = """
    Obrigado por usar nosso sistema! Tenha um bom dia!

    Caso deseje reiniciar a aplicação, basta atualizar a página.
    """

    print(mensagem_saida)
    loop = False


def executar_controle(opcao):

    opcoes_disponiveis = ["0","1","2","3"]

    if opcao in opcoes_disponiveis:
        if opcao == "0":
            sair()
        elif opcao == "1":
            mostrar_saldo()
        elif opcao == "2":
            sacar_valor()
        elif opcao == "3":
            depositar_valor()
    else:
        mostrar_erro()


def iniciar():
    
    while loop:
        opcao = input(mensagem_boas_vindas)
        executar_controle(opcao)

iniciar()
