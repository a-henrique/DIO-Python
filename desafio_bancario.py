from time import sleep


def menu():
    menu = """
    ===================
    Menu de opções
    ===================
    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Cadastrar Usuario
    [4] Criar Conta
    [5] Listar Contas
    [6] Sair 

    ==> Opção:"""

    return int(input(menu))

def depositar(saldo, valor_depositado, extrato, /):
    if valor_depositado <= 0:
        print("Valor Inválido")
        sleep(1)
    
    elif valor_depositado > 0:
        print("Processando...")
        sleep(1)
        print(f"Depósito realizado!")
        saldo += valor_depositado
        extrato += f"Valor depositado: R${valor_depositado:.2f}\n"
    else:
        print("OPERAÇÃO FALHOU")
    
    return saldo, extrato
    
def sacar(*, saldo, valor_a_sacar, extrato,  limite, numero_saques, LIMITE_SAQUES):
   
    if numero_saques >= LIMITE_SAQUES:
        print("Você excedeu o limite de saques diários!!")
    elif valor_a_sacar > limite:
        print(f"Você não pode sacar valores acima de R${limite:.2f}")
    elif valor_a_sacar > saldo:
        print("Saldo insuficiente")
    elif valor_a_sacar < 0:
        print("Operacao não permitida")
    else:
        numero_saques += 1
        saldo -= valor_a_sacar
        print("Processando...")
        sleep(1)
        extrato += f"Valor Saque: -R${valor_a_sacar:.2f}!\n"
        print(f"Operação encerrada com Sucesso!")
    return saldo, extrato

def exibir_extrato(saldo,/, *, extrato):
    print("=================== Extrato ====================")
    print(extrato)
    print(f"Saldo Total:R${saldo:.2f}")
    print("================== FIM Extrato ===================") 

def criar_usuario(usuarios):
    cpf = input("Informe o CPF do usuário (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=================================")
        print("Já existe um usuário com esse CPF")
        print("=================================")
        return
    
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a dad de nascimento {dd-mm-aaaa}: ")
    endereco = input("Informe o endereco (logradouro, rua - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco":endereco})

    print("usuario cadastrado")

def filtrar_usuario(cpf, usuarios):
    filtrado = []
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            filtrado = usuario["cpf"]
        else:
            filtrado = None
    return filtrado

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não foi encontrado, fim da criação")

def listar_contas(contas):
    total = 0
    for conta in contas:
        print(f"Agencia: {conta['agencia']}, Conta: {conta['numero_conta']}, Usuario: {conta['usuario']}")
        total += 1
    print("=========================")
    print(f"Total de Contas: {total}")
    print("=========================")

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        
        opcao = menu()
        
        if opcao == 0:
            valor_a_depositar = float(input("Informe quanto deseja depositar: "))
            saldo, extrato = depositar(saldo, valor_a_depositar, extrato)

        elif opcao == 1:
            valor_a_sacar = float(input("Informe quanto deseja sacar: "))
            saldo, extrato = sacar(saldo=saldo, valor_a_sacar=valor_a_sacar, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
        
        elif opcao == 2:
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 3:
            criar_usuario(usuarios)

        elif opcao == 4:
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == 5:
            listar_contas(contas)

        elif opcao == 6:
            print("bye")
            break
        else:
            print("OPÇÃO INVÁLIDA")

main()