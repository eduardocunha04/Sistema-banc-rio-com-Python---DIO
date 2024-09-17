#Sistema bancário - Projeto DIO - by: Eduardo Gaeta

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação não concluída! Valor informado é inválido.")
            
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação não concluída! Você não possui saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação não concluída! O valor do saque excede seu limite disponível.")
        
        elif excedeu_saques:
            print("Operação não concluída! Número de saques excedidos.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Operação não foi concluída! O valor informado é inválido.")
            
    elif opcao == "e":
        print("\=================== EXTRATO ===================")
        print("Não foram realizadas movimentações nesta conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================================")
        
    elif opcao == "q":
        break
    
    else:
        print("Operação não foi concluída, por favor, selecione uma opção a ser realizada.!")
