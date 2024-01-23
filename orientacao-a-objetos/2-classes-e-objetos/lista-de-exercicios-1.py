# Criando uma classe que modele o objeto "carro".
class Carro:

# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
    def __init__(self):
        self.ligado = False
        self.cor = 'vermelho'
        self.modelo = 'Troller'
        self.velocidade = 0
        self.velocidade_max = 220
        self.velocidade_min = 0

# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelerar(self):
        if not self.ligado:
            return
        if self.velocidade < self.velocidade_max:
            self.velocidade += 5

    def desacelerar(self):
        if not self.ligado:
            return
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 5

    def __str__(self) -> str:
        return f'Carro - cor {self.cor} - modelo {self.modelo} - ligado {self.ligado} - velocidade {self.velocidade}'

# Crie uma instância da classe carro.
carro = Carro()

# Faça o carro "andar" utilizando os métodos da sua classe.
carro.ligar()
for _ in range (12):
    carro.acelerar()

print(f"O carro está ligado? {carro.ligado}")
print(f"Em que velocidade o carro está? {carro.velocidade} km/h")

# Faça o carro "parar" utilizando os métodos da sua classe.
while carro.velocidade != 0:
    carro.desacelerar()
carro.desligar()

print(f"O carro está ligado? {carro.ligado}")
print(f"Em que velocidade o carro está? {carro.velocidade} km/h")