from BancoLib import Banco

# iniciando Menu
def imprimeMenu():
    print("Menu")
    print("0 - Sair")
    print("1 - Criar uma Nova Conta")
    print("2 - Consultar Saldo Conta")
    print("3 - Depositar na Conta")
    print("4 - Sacar na Conta")

# iniciando o programa
print("Bem-vindo")
bancoUfrpe = Banco("UABJ")
imprimeMenu()
escolha = int(input("digite a opção desejada:"))
# enquanto a escolha for diferente de 0, o programa continua
while escolha > 0:
    if escolha == 1:
        # criar uma conta
        print("Criando Conta...")
        numConta = bancoUfrpe.criarConta()
        print("Conta criada:", numConta)
    elif escolha == 2:
        print("Consultando Saldo...")
        numConta = int(input("digite o numero da conta:"))
        saldo = bancoUfrpe.consultaSaldo(numConta)
        print("o saldo da conta", numConta, "é", saldo, "R$")
    elif escolha == 3:
        print("Depositando Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja depositar:"))
        saldo = bancoUfrpe.depositar(numConta, valor)
        print("Valor Depositado")
    elif escolha == 4:
        print("Sacando da Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja sacar:"))
        resp = bancoUfrpe.sacar(numConta, valor)
        if resp:  # significa resp == True
            print("Valor Sacado")
        else:
            print("Saldo Insuficiente")
    imprimeMenu()
    escolha = int(input("digite a opção desejada:"))