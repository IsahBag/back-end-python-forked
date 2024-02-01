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

from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone        

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

 

class Cliente(Pessoa):
    def __init__(self, nome, telefone, renda, sexo):
        super().__init__(nome, telefone)
        self.__sexo = sexo
        self.__renda = renda         
        self.saldo = 0      
        if self.__sexo == 'F':
             self.saldo_min = -renda 
        else:
            self.saldo_min = 0

    @property
    def renda(self):
        return self.__renda
    
    @renda.setter
    def renda(self, nova_renda):
        self.__renda = nova_renda

    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self, novo_sexo):
        self.__sexo = novo_sexo     
    
    def sacar(self, valor):
        if self.__sexo == 'M' and self.saldo - valor < 0:
            print(colorama.Fore.RED + "Operação excede o limite do cheque especial para o cliente masculino.")
            return False
        elif self.__sexo == 'F' and self.saldo - valor < - self.__renda:
            print(colorama.Fore.RED + "Operação excede o limite do cheque especial para a cliente feminina.")
            return False
        else:        
            self.saldo -= valor
            return True

    def depositar(self, valor):
        self.saldo += valor

    def __str__(self):
        return(f'Cliente: {self.nome}\n' +
               f'Telefone: {self.telefone}\n' +
               f'Renda Mensal: {self.__renda}\n' +
               f'Sexo: {self.__sexo}\n' +
               f'Saldo: {self.saldo}')


class Conta_corrente:
    def __init__(self, clientes):
        self.saldo = 0
        self.clientes = clientes

    def sacar(self, valor):
        for cliente in self.clientes:
            if not cliente.sacar(valor):
                return False
        self.saldo -= valor
        return True

    def depositar(self, valor):
        for cliente in self.clientes:
            cliente.depositar(valor)
        self.saldo += valor

    def __str__(self):
        clientes_str = '\n\n'.join(str(cliente) for cliente in self.clientes)
        return f"Saldo da Conta Corrente: {self.saldo}\n\nDetalhes dos Clientes:\n{clientes_str}"


# Exemplo de uso do programa
cliente1 = Cliente("Maria", "123456789", 3000, "F")
cliente2 = Cliente("João", "987654321", 2500, "M")

conta = Conta_corrente([cliente1])

print(cliente1)

conta.depositar(1000)
print("Saldo após depósito:")
print(conta)

conta.sacar(200)
print("Saldo após saque:")
print(conta)