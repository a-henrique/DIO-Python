class Estudante:

    # VARIÁVEL DE CLASSE //  ATRIBUTO DA CLASSE
    escola = "DIO"

    def __init__(self, nome, matricula):
    # VARIÁVEL DE INSTÂNCIA // ATRIBUTO DE INSTANCIA
        self.nome = nome
        self.matricula = matricula

    
    def __str__(self):
        return f"{self.nome} -> {self.matricula} -> {self.escola}"
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Audrin", 1)
aluno_2 = Estudante('Mayra', 2)
mostrar_valores(aluno_1, aluno_2)

print('----------------------')

Estudante.escola = 'Python'
mostrar_valores(aluno_1, aluno_2)