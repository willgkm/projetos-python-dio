import textwrap


def menu():
    menu = """\n
    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrato
    [CC]\tCriar conta
    [CU]\tCriar usuário
    [q]\tSair
    [t]\tTestes
    => """
    return input(textwrap.dedent(menu))


def executa_deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso! ")
    else:
        print("\n Erro ao realizar deposito")
    return saldo, extrato


def executa_saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\n Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\n Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\nO valor informado é inválido.")

    return saldo, extrato


def executa_extrato(saldo, /, *, extrato):
    print("\n EXTRATO ")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    usuario = usuarios_filtrados[0] if usuarios_filtrados else None

    if usuario:
        print("\n Já existe usuário com esse CPF! ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    usuario = usuarios_filtrados[0] if usuarios_filtrados else None

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("valor do depósito: "))

            saldo, extrato = executa_deposito(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("valor do saque: "))

            saldo, extrato = executa_saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            executa_extrato(saldo, extrato=extrato)

        elif opcao == "cu":
            criar_usuario(usuarios)

        elif opcao == "cc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "q":
            break


main()