# Escrever um programa que armazena as informações de três carros
# e aprensente-as na tela para o usuário

class Carro:
    def __init__(self, modelo, ano, placa, marca, cor): # método construtor
        self.modelo = modelo # declaração de um atributo e atribuição de um valor
        self.ano = ano # variáveis de instância
        self.placa = placa
        self.marca = marca
        self.cor = cor
        
    def __str__(self):
        return f'{self.modelo} da empresa {self.marca}, ano {self.ano}, cor {self.cor} e placa {self.placa} '

Jetta = Carro('-Jetta', 1997, 'ABC1234', 'Chervolet', 'Preto') # instanciamento de um objeto
Lancer = Carro('-Lancer', 2020, 'CBA4321', 'Mitsubishi', 'Branco') # instanciamento de um objeto
Fusca = Carro('-Fusca', 1995, 'GHF5291', 'Volkswagen', 'Azul') # instanciamento de um objeto
Civic = Carro('-Civic', 2017, 'KIO7129', 'Honda', 'Prata') # instanciamento de um objeto

print(Jetta)
print(Lancer)
print(Fusca)
print(Civic)

print(f'Cor do carro 2: {Lancer.cor}')
print(f'Marca do carro 3: {Fusca.marca}')