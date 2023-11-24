from time import sleep


def menu():
    menu = """
    ===================
    Menu de opções
    ===================
    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Sair 

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
            print("bye")
            break
        else:
            print("OPÇÃO INVÁLIDA")

main()