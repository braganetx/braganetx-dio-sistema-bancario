class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.saques_diarios < 3:
            if 0 < valor <= 500 and valor <= self.saldo:
                self.saldo -= valor
                self.extrato.append(f"Saque: R$ {valor:.2f}")
                self.saques_diarios += 1
                print("Saque realizado com sucesso!")
            elif valor > self.saldo:
                print("Saldo insuficiente.")
            else:
                print("Valor inválido para saque.")
        else:
            print("Limite de saques diários atingido.")

    def exibir_extrato(self):
        print("\n===== Extrato =====")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in self.extrato:
                print(movimento)
            print(f"Saldo: R$ {self.saldo:.2f}")
        print("===================")


banco = Banco()

while True:
    print("\n=== Menu ===")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = input("Selecione uma opção: ")

    if opcao == '1':
        valor = float(input("Digite o valor do depósito: "))
        banco.depositar(valor)
    elif opcao == '2':
        valor = float(input("Digite o valor do saque: "))
        banco.sacar(valor)
    elif opcao == '3':
        banco.exibir_extrato()
    elif opcao == '4':
        print("Obrigado por utilizar o sistema bancário!")
        break
    else:
        print("Opção inválida.")