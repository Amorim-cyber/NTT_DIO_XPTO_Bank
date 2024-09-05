
SALDO_INICIAL = 1200
LIMITE_MAXIMO = 500
MENSAGEM_BOAS_VINDAS = """
Olá Usuário! Bem vindo ao banco XPTO!

O que deseja fazer?

- [1] Mostrar Extrato 
- [2] Realizar Saque 
- [3] Realizar Deposito
- [0] Sair
"""

loop = True 
saldo_final = SALDO_INICIAL
numero_de_saques_diarios = 0
numero_de_depositos_diarios = 0
movimentacoes = []

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

def digitar_valor():
    mensagem_digitar_valor = """
    Digite o valor desejado:
    """
    valor_texto = input(mensagem_digitar_valor)

    if valor_texto.isdigit():
        valor = abs(int(valor_texto))
        return valor
    else:
        mostrar_erro(tipo=2)
    return 0

def mostrar_extrato():
    global SALDO_INICIAL
    global saldo_final
    global movimentacoes

    if len(movimentacoes) != 0: 
        texto_movimentacoes = "\n    ".join([f"- {movimentacao['descricao']}: R$ {movimentacao['valor']}.00" for movimentacao in movimentacoes]) 
    else: 
        texto_movimentacoes = "- Sem movimentações no momento -"

    mensagem_mostrar_extrato = f"""EXTRATO DA CONTA
    Saldo Inicial: R$ {SALDO_INICIAL}.00
    {texto_movimentacoes}
    Saldo Final: R$ {saldo_final}.00""" 

    mostrar_mensagem_padrao(mensagem_mostrar_extrato)

def sacar_valor():
    global LIMITE_MAXIMO
    global saldo_final
    global numero_de_saques_diarios
    global movimentacoes
    valor = digitar_valor()

    if valor == 0:
        return
    
    if valor > LIMITE_MAXIMO:
        mostrar_erro(tipo=5)
        return

    if numero_de_saques_diarios == 3:
        mostrar_erro(tipo=4)
        return

    if saldo_final >= valor:
        saldo_final -= valor 
        numero_de_saques_diarios += 1
        movimentacoes.append({'descricao': f"Saque ({numero_de_saques_diarios}/3)",'valor': (-1)*valor})
        mostrar_mensagem_padrao(f'O valor R$ {valor}.00 foi retirado com sucesso! ({numero_de_saques_diarios}/3)')
    else:
        mostrar_erro(tipo=3)

def depositar_valor():
    global saldo_final
    global movimentacoes
    global numero_de_depositos_diarios
    valor = digitar_valor()

    if valor == 0:
        return

    
    saldo_final += valor
    numero_de_depositos_diarios+=1
    movimentacoes.append({'descricao': f"Deposito ({numero_de_depositos_diarios})",'valor': valor})
    mostrar_mensagem_padrao(f'O valor R$ {valor}.00 foi depositado com sucesso!')

def mostrar_erro(tipo = 1):
    if tipo == 1:
        mostrar_mensagem_padrao('Opção inválida! Por favor digitar as opções indicadas entre [ ].')
    elif tipo == 2:
        mostrar_mensagem_padrao('Valor inválido! Por favor digitar números inteiros positivos.')
    elif tipo == 3:
        mostrar_mensagem_padrao('Saldo insuficiente para o saque!')
    elif tipo == 4:
        mostrar_mensagem_padrao('Você excedeu o limite diário de 3 solicitações de saque.\n    Não é mais possivel realizar esta operação.')
    elif tipo == 5:
        mostrar_mensagem_padrao('Você somente pode realizar operações\n    de saque de no máximo R$ 500.00')
    elif tipo == 6:
        print("\n    Por favor atualize a página para reiniciar a aplicação")

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
            mostrar_extrato()
        elif opcao == "2":
            sacar_valor()
        elif opcao == "3":
            depositar_valor()
    else:
        mostrar_erro()


def iniciar():
    
    while loop:
        opcao = input(MENSAGEM_BOAS_VINDAS)
        executar_controle(opcao)


try:

    iniciar()

except:
    mostrar_erro(tipo = 6)