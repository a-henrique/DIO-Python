class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_de_nascimento(cls, ano, mes, dia, nome):
        idade = 2023 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
# p = Pessoa("Audrin", 23)
# print(p.nome, p.idade)

p = Pessoa.criar_de_nascimento(1999, 12, 26, "Audrin")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(p.idade))
print(Pessoa.e_maior_idade(12))
