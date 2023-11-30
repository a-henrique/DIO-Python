class Veiculo():
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor 
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Caminhao(Veiculo):
    
    def __init__(self, cor, placa, numero_rodas, carregado): # Sobrescreve o construtor da classe principal
        super().__init__(cor, placa, numero_rodas) # Herda todos os atributos da classe principal
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

class Carro(Veiculo):
    pass

class Motocicleta(Veiculo):
    pass

car1 = Carro("branco", "abc-1234", 4)

truck1 = Caminhao("azul", "dfc-4567", 8, True)

moto1 = Motocicleta("preta", "tyu-7856", 2)

print(car1)
print(truck1)
print(moto1)