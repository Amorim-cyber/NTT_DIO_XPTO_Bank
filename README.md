# Criando um Sistema Bancário com python | pyscript | github pages

<a href="https://amorim-cyber.github.io/NTT_DIO_XPTO_Bank/">CLIQUE AQUI PARA INTERAGIR COM O PROJETO VERSÃO 2</a>

<a href="https://amorim-cyber.github.io/NTT_DIO_XPTO_Bank/">CLIQUE AQUI PARA INTERAGIR COM O PROJETO VERSÃO 1</a>

### Introdução:

Esta é uma solução para um dos desafios de projeto propostos pela Digital Inovation One (DIO). 

A ideia é criar um sistema bancário simples contendo as seguintes operações:
- Visualizar Extrato
- Efetuar Saque
- Efetuar Deposito
- Listar Usuários Cadastrados
- Cadastrar Usuário
- Cadastrar Conta

Conforme foi proposto, a aplicação foi desenvolvida utilizando a linguagem `Python`. Contudo resolvi adicionar os recursos do `pyscript` e do `github pages` para uma melhor experiência.

### Sobre pyscript e github pages:

O pyscript permite que seja possível executar scripts python dentro de um browser.

Já o github pages fornece hospedagem sem custo para projetos web de baixo porte.

A motivação de usar essas duas ferramentas é trazer para mais perto o produto final para o usuário, sinalizar que o que foi desenvolvido está funcionando sem problemas.

Logo uma aplicação que normalmente só poderia ser executada localmente, agora pode ser compartilhada a todos com a união desses dois recursos.

Caso você achou legal a ideia e deseja incluir em seu projeto, <a href="https://m.youtube.com/watch?v=dmIWFcJ2UTI">este vídeo</a> ensina de forma rápida e simples como implementar. 

### Sobre o sistema bancário:

#### - Menu -

Ao clicar no <a href="https://amorim-cyber.github.io/NTT_DIO_XPTO_Bank/">link</a> do projeto, aparecerá na tela o seguinte menu:

<div align="center">
<img src="./imgs/menu.png" width="400" height="400">
</div>
<br>
O usuário terá a opção de ver seu extrato, sacar uma quantia, depositar uma quantia e sair do programa. Por simplicidade, estamos supondo que o banco XPTO tem apenas uma conta.

Temos uma caixa de texto aonde irá acontecer a interação. É importante mencionar que o programa somente vai aceitar apenas o que está indicado em [ ], qualquer caracter diferente disso vai trazer a seguinte mensagem abaixo:

<div align="center">
<img src="./imgs/erro.png" width="400" height="400">
</div>

#### - Extrato -

Se incluimos o valor "1" na caixa de texto e clicar em Ok iremos para a tela de extrato. Estamos colocando uma condição que inicialmente o usuário sempre tem R$ 1200.00 em conta, e conforme vai acontecendo a interação, o saldo final vai ser modificado. 

Abaixo temos a situação onde ainda não ocorreu saques ou depositos. 

<div align="center">
<img src="./imgs/extrato1.png" width="400" height="400">
</div>

#### - Saque -

Voltando para o menu principal, ao digitar a opção "2", vamos para a operação de saque, o programa ira pedir o valor da quantia a ser sacada conforme pode ser observado logo abaixo:

<div align="center">
<img src="./imgs/digitar_valor.png" width="400" height="400">
</div>
<br>
Em relação a operação de saque, foi solicitado que incluissemos as seguintes regras:
<ol>
<li> O usuário pode fazer até 3 saques diários, acima desse número há é mais possível efetuar saques.</li>
<li> Os saques não podem superar valores acima de R$ 500.00</li>
</ol>

Após declarar o montante que deseja sacar, o valor será descontado do saldo inicial e atividade adicionada ao extrato.

Vale comentar que o programa só vai aceitar valores inteiros positivos no momento do saque, qualquer valor diferente disso vai retornar um erro.

Ocorrerá também um erro caso o usuário queira sacar um valor superior ao saldo que ele tem no momento.

#### - Deposito - 

A opção "3" dentro do menu principal leva para a operação de deposito, o procedimento é parecido com do saque, a diferença é que teremos um acrescimo de valor e sua movimentação adicionada ao extrato. Não há limite de quantidade e nem de quantia para depositos, contudo a regras de input continua a mesma: Não é permitido colocar valores que não sejam numero inteiros positivos.

Como disse acima, movimentamentações tanto de saque quanto de depósito modificam o saldo da conta. Após algumas operações realizadas, se formos consultar o extrato, haverá uma listagem das movimentações junto com os valores de saldo inicial e final conforme pode ser visualizado abaixo:

<div align="center">
<img src="./imgs/extrato2.png" width="400" height="400">
</div>

#### - Sair -

Por fim temos a opção de sair se digitarmos "0", uma vez selecionado o programa é encerrado e toda informação inserida deletada.

<div align="center">
<img src="./imgs/saida.png" width="600" height="400">
</div>

### Encerramento:

Se você você chegou até aqui e curtiu o projeto não deixe de dar uma estrela :star:

Obrigado! :smile: