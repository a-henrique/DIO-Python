from time import sleep


menu = """
===================
Menu de opções
===================
[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair 

==> Opção:"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = int(input(menu))

    if opcao == 0:
        print("Depósito")
        valor_depositado = float(input("Digite o valor a ser depositado: "))
        if valor_depositado <= 0:
           print("Valor Inválido")
           sleep(1)
        
        elif valor_depositado > 0:
            print("Processando...")
            sleep(1)
            print(f"Operação encerrada com Sucesso!")
            saldo += valor_depositado
            extrato += f"Valor depositado: R${valor_depositado:.2f}\n"
        else:
            print("digite um valor válido")

    elif opcao == 1:
        print("Saque")
        valor_a_sacar = float(input("Quanto você deseja sacar?"))
        
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

    
    elif opcao == 2:
        print("=================== Extrato ====================")
        print(extrato)
        print(f"Saldo Total:R${saldo:.2f}")
        print("================== FIM Extrato ===================")

    elif opcao == 3:
        print("Saindo... Até a próxima!")
        break

    else:
        print("OPÇÃO INVÁLIDA")