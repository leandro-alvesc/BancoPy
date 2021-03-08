from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []
clientes: List[Cliente] = []


def main() -> None:
    menu()


def menu() -> None:
    print('=' * 50)
    print(' Caixa Eletrônico '.center(50, '*'))
    print(' Banco Central '.center(50, '*'))
    print('=' * 50)

    print(' MENU '.center(50, '*'))
    print('1- Criar conta')
    print('2- Efetuar Saque')
    print('3- Efetuar Depósito')
    print('4- Efetuar Transferência')
    print('5- Listar Contas')
    print('6- Sair')

    opcao: int = int(input('Selecione uma opção: '))

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(1.5)
        exit(0)
    else:
        print('Opção inválida.')
        sleep(1.5)
        menu()


def criar_conta() -> None:
    print('=' * 50)
    print('Dados do cliente: ')
    nome: str = input('Nome do cliente: ')
    email: str = input(f'Email de {nome}: ')
    cpf: str = input(f'CPF de {nome}: ')
    data_nascimento: str = input(f'Data de nascimento de {nome}: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)

    contas.append(conta)
    clientes.append(cliente)

    print('Conta criada com sucesso!')
    print('Dados da conta: ')
    print('-' * 50)
    print(conta)
    print('=' * 50)

    sleep(1.5)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta: '))
        conta: Conta = buscar_conta_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta de número {numero}.')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(1.5)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta: '))
        conta: Conta = buscar_conta_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))
            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta de número {numero}.')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(1.5)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta de origem: '))
        conta: Conta = buscar_conta_numero(numero)
        numero_destino: int = int(input('Informe o número da conta destino: '))
        conta_destino: Conta = buscar_conta_numero(numero_destino)

        if conta and conta_destino:
            valor: float = float(input('Informe o valor da transferência: '))
            conta.transferir(conta_destino, valor)
        else:
            print(f'Transferência inválida.')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(1.5)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('=' * 50)
        print('Listagem de contas'.center(50, '*'))
        print('=' * 50)
        for conta in contas:
            print(conta)
            print('-' * 50)
            sleep(0.8)
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(1.5)
    menu()


def buscar_conta_numero(numero: int) -> Conta:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
