# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos. Quando a cliente fizer um saque, diminuiremos o saldo 
# da conta corrente. Quando ela fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda mensal, ou seja, elas podem sacar valores que 
# deixam a sua conta com valor negativo até -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".

import colorama
colorama.init()

class Pessoa:
    def __init__(self, nome, telefone, renda, sexo):
        self.__nome = nome
        self.__telefone = telefone
        self.__renda = renda
        self.__sexo = sexo

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone

    @property
    def renda(self):
        return self.__renda
    
    @renda.setter
    def renda(self, nova_renda):
        self.__renda = nova_renda
        self.ativar_cheque_especial()

    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self, novo_sexo):
        self.__sexo = novo_sexo
        self.ativar_cheque_especial()

class Cliente(Pessoa):
    def __init__(self, nome, telefone, renda, sexo, conta_corrente):
        super().__init__(nome, telefone, renda, sexo)
        self.cheque_especial = False
        self.saldo = 0
        self.conta_corrente = conta_corrente
        self.ativar_cheque_especial()

    def ativar_cheque_especial(self):
        if self.sexo == 'F' and self.renda > 0:
            self.cheque_especial = True
        else:
            self.cheque_especial = False

    def sacar(self, valor):
        if self.cheque_especial or self.saldo >= valor:
            self.saldo -= valor
            self.conta_corrente.registrar_operacao("Saque", valor)
            print('Saque realizado com sucesso!')
        else:
            print('Não há saldo disponível para sacar o valor indicado!')

    def depositar(self, valor):
        self.saldo += valor
        self.conta_corrente.registrar_operacao("Depósito", valor)
        print('Depósito realizado com sucesso!')

    def __str__(self) -> str:
        return(f'Cliente: {self.nome}\n' +
               f'Telefone: {self.telefone}\n' +
               f'Renda: {self.renda}\n' +
               f'Sexo: {self.sexo}\n' +
               f'Saldo: {self.saldo}\n')

class Conta_corrente:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.lista_operacoes = []

    def registrar_operacao(self, operacao, valor):
        self.lista_operacoes.append((operacao, valor))

    def mostrar_operacoes(self):
        for operacao in self.lista_operacoes:
            print(operacao)

# Criando uma instância de Cliente
cliente1 = Cliente('Flavia', '1234555', 4657.90, 'F', None)

# Criando uma instância de Conta_corrente passando o cliente
conta_corrente1 = Conta_corrente(cliente1, 1000)
cliente1.conta_corrente = conta_corrente1

# Executando algumas operações
cliente1.depositar(500)
cliente1.sacar(200)

# Consultando as operações
conta_corrente1.mostrar_operacoes()

# Imprimindo os dados do cliente
print(cliente1)

# Realizando outro saque
cliente1.sacar(1000)

# Consultando o saldo do cliente
saldo_cliente = cliente1.saldo
print(f"Saldo do cliente: {saldo_cliente}")