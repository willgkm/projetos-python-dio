menu = """
  [D] Depositar
  [S] Sacar 
  [E] Extrato
  [Q] SAIR 

==> """

menu_deposito = """
        MENU DEPOSITO 

Qual valor deseja depositar: """


menu_saque = """
        MENU SAQUE 

Qual valor deseja Sacar: """



saldo_atual = 0
limite = 500
extrato = ""
numero_saque = 0 
LIMITE_SAQUE = 3

def executa_deposito():
    global saldo_atual
    deposito = input(menu_deposito)
    saldo_atual += float(deposito)

def executa_saque():
    global numero_saque
    global saldo_atual
    global limite
    
    if( numero_saque >= LIMITE_SAQUE):
        print("Limite de saques diarios atingidos !!!")
        return  

    valor_saque = float(input(menu_saque))

    if(valor_saque >= saldo_atual):
        print("Saldo insuficiente !!!")
        return
    elif(valor_saque > limite):
        print("O valor maximo para saque é de R$500.00")
        return 
    else:
        saldo_atual -= valor_saque
        numero_saque += 1


while True: 

    opcao =  input(menu)

    if(opcao) == "d":
        executa_deposito()
    
    if(opcao) == "s":
        executa_saque()

    if(opcao) == "e":
        print("""MENU SALDO 
              
SALDO ATUAL : R$""",saldo_atual  )

    if(opcao) == "q":
        break