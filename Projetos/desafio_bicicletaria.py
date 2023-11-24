class Bicicleta:
    
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1

    def buzinar(self):
        print("Plim Plim")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta Parada")
    
    def correr(self): # Todo método deve ter um param explicito, geralmente é o self
        print("vruuummmm...")

    # def __str__(self):
    #     return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def trocar_marcha(self, nro_marcha):
        print("Trocando Marcha")
       
        def _trocar_marcha():
            if nro_marcha > self.marcha:
                print("Marcha Trocada...")
            else:
                print("Não foi possível trocar de marcha")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)


b2 = Bicicleta("verde", "monark", 2000, 189)
b2.buzinar() # Bicicleta.buzinar(b2)
print(b2)