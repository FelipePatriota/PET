from BancoLib import Banco
# from ContaLib import Conta


print("Bem-vindo")
bancoUfrpe = Banco("UABJ")
print("Menu")
print("0 - Sair")
print("1 - Criar uma Nova Conta")
print("2 - Consultar Saldo Conta")
print("3 - Depositar na Conta")
print("4 - Sacar na Conta")
print("5 - Render Poupanca")
print("6 - Render Bonus")

escolha = int(input("digite a opção desejada:")) 

while escolha > 0: # enquanto a escolha for diferente de 0

    if escolha == 1:
        # criar uma conta
        print("Criando Conta...")
        print("1 - Conta Corrente")
        print("2 - Conta Poupanca")
        print("3 - Conta Bonificada")
        opcao = int(input("digite o tipo da conta:"))

        if opcao == 1:
            numConta = bancoUfrpe.criarConta() # cria uma conta normal
        elif opcao == 2:
            numConta = bancoUfrpe.criarPoupanca() # cria uma poupanca
        else :
            numConta = bancoUfrpe.criarContaBonificada() # cria uma conta bonificada   
        print("Conta criada:", numConta)

    # consultar saldo da conta 
    elif escolha == 2:
        print("Consultando Saldo...")
        numConta = int(input("digite o numero da conta:"))
        saldo = bancoUfrpe.consultaSaldo(numConta)
        print("o saldo da conta", numConta, "é R$", saldo)

    # depositar na conta com desconto
    elif escolha == 3:
        print("Depositando Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja depositar:"))
        saldo = bancoUfrpe.depositarComDesconto(numConta, valor)
        print("Valor Depositado")

    # sacar de qualquer conta 
    elif escolha == 4:
        print("Sacando da Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja sacar:"))
        resp = bancoUfrpe.sacar(numConta, valor)
        if resp:  # significa resp == True
            print("Valor Sacado")
        else:
            print("Saldo Insuficiente")

    # render poupanca da conta poupanca           
    elif escolha == 5:
        print("Rendendo Poupanca...")
        numConta = int(input("digite o numero da conta poupanca:"))
        resp = bancoUfrpe.renderPoupanca(numConta)
        if resp:
            print("Poupanca com novo saldo")
        else:
            print("A conta não é poupanca ou não existe")

    # render bonus da conta bonificada se tiver bonus          
    elif escolha == 6:
        print("Será que vai dar bonus?")
        numConta = int(input("digite o numero da conta bonificada:"))
        resp = bancoUfrpe.renderBonus(numConta)
        if resp:
            print("Bonus com novo saldo")
        else:
            print("A conta não é bonificada ou não existe")             
       


    escolha = int(input("digite a opção desejada:"))