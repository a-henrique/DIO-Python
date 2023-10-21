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