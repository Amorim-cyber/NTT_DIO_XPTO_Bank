from datetime import datetime
from pyweb import pydom

class banco_XPTO:

    def __init__(self):
        self.SALDO_INICIAL = 1200
        self.LIMITE_MAXIMO = 500
        self.MENSAGEM_BOAS_VINDAS = """
        Olá Usuário! Bem vindo ao banco XPTO!

        O que deseja fazer?

        - [1] Mostrar Extrato 
        - [2] Realizar Saque 
        - [3] Realizar Deposito
        - [0] Sair
        """

        self.loop = True 
        self.saldo_final = self.SALDO_INICIAL
        self.numero_de_saques_diarios = 0
        self.numero_de_depositos_diarios = 0
        self.movimentacoes = []

    def mostrar_mensagem_padrao(self,mensagem):

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
            self.sair()
        else:
            self.mostrar_erro()

    def digitar_valor(self):
        mensagem_digitar_valor = """
        Digite o valor desejado:
        """
        valor_texto = input(mensagem_digitar_valor)

        if valor_texto.isdigit():
            valor = abs(int(valor_texto))
            return valor
        else:
            self.mostrar_erro(tipo=2)
        return 0

    def mostrar_extrato(self):

        movimentacoes = self.movimentacoes

        if len(movimentacoes) != 0: 
            texto_movimentacoes = "\n    ".join([f"- [{movimentacao['descricao']} | {movimentacao['data']}] -> R$ {movimentacao['valor']}.00" for movimentacao in movimentacoes]) 
        else: 
            texto_movimentacoes = "- Sem movimentações no momento -"

        mensagem_mostrar_extrato = f"""EXTRATO DA CONTA
        Saldo Inicial: R$ {self.SALDO_INICIAL}.00
        {texto_movimentacoes}
        Saldo Final: R$ {self.saldo_final}.00""" 

        self.mostrar_mensagem_padrao(mensagem_mostrar_extrato)

    def sacar_valor(self):

        movimentacoes = self.movimentacoes
        valor = self.digitar_valor()
        data_registro = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        if valor == 0:
            return
        
        if len(movimentacoes) == 10:
            self.mostrar_erro(tipo=7)
            return
        
        if valor > self.LIMITE_MAXIMO:
            self.mostrar_erro(tipo=5)
            return

        if self.numero_de_saques_diarios == 3:
            self.mostrar_erro(tipo=4)
            return

        if self.saldo_final >= valor:
            self.saldo_final -= valor 
            self.numero_de_saques_diarios += 1
            movimentacoes.append({'data': f"{data_registro}",'descricao': f"Saque ({self.numero_de_saques_diarios}/3)",'valor': (-1)*valor})
            self.mostrar_mensagem_padrao(f'O valor R$ {valor}.00 foi retirado com sucesso! ({self.numero_de_saques_diarios}/3)')
        else:
            self.mostrar_erro(tipo=3)

    def depositar_valor(self):
        
        movimentacoes = self.movimentacoes

        valor = self.digitar_valor()
        data_registro = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        if valor == 0:
            return
        
        if len(movimentacoes) == 10:
            self.mostrar_erro(tipo=7)
            return

        
        self.saldo_final += valor
        self.numero_de_depositos_diarios+=1
        movimentacoes.append({'data': f"{data_registro}", 'descricao': f"Deposito ({self.numero_de_depositos_diarios})",'valor': valor})
        self.mostrar_mensagem_padrao(f'O valor R$ {valor}.00 foi depositado com sucesso!')

    def mostrar_erro(self,tipo = 1):
        if tipo == 1:
            self.mostrar_mensagem_padrao('Opção inválida! Por favor digitar as opções indicadas entre [ ].')
        elif tipo == 2:
            self.mostrar_mensagem_padrao('Valor inválido! Por favor digitar números inteiros positivos.')
        elif tipo == 3:
            self.mostrar_mensagem_padrao('Saldo insuficiente para o saque!')
        elif tipo == 4:
            self.mostrar_mensagem_padrao('Você excedeu o limite diário de 3 solicitações de saque.\n    Não é mais possivel realizar esta operação.')
        elif tipo == 5:
            self.mostrar_mensagem_padrao('Você somente pode realizar operações\n    de saque de no máximo R$ 500,00.')
        elif tipo == 6:
            print("\n    Por favor atualize a página para reiniciar a aplicação")
        elif tipo == 7:
            print("    Número de transações excedido!\n    O sistema permite somente realizar até 10 operações diárias.")

    def sair(self):

        mensagem_saida = """
        Obrigado por usar nosso sistema! Tenha um bom dia!

        Caso deseje reiniciar a aplicação, basta atualizar a página.
        """

        print(mensagem_saida)
        self.loop = False


    def executar_controle(self,opcao):

        opcoes_disponiveis = ["0","1","2","3"]

        if opcao in opcoes_disponiveis:
            if opcao == "0":
                self.sair()
            elif opcao == "1":
                self.mostrar_extrato()
            elif opcao == "2":
                self.sacar_valor()
            elif opcao == "3":
                self.depositar_valor()
        else:
            mostrar_erro()


    def iniciar(self):
        
        while self.loop:
            opcao = input(self.MENSAGEM_BOAS_VINDAS)
            self.executar_controle(opcao)

