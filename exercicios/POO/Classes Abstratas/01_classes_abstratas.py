from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        return super().marca
        
class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando a TV')
    
    def desligar(self):
        print("Desligando a TV")

    @property
    def marca(self):
        return "LG"
    
class ControleArcondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar")

    def desligar(self):
        print("Desligando o Ar")

    @property
    def marca(self):
        return "Samsung"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controleAr = ControleArcondicionado()
print(controleAr.marca)