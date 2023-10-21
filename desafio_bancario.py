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
            extrato += f"Valor depositado: {valor_depositado:.2f}\n"
        else:
            print("digite um valor válido")

    elif opcao == 1:
        print("Saque")


    
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