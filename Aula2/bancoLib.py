import random

# Classe Conta
class Conta():

    # "Construtor" da classe Conta
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0

    # Métodos deposite com desconto de 0.1%, usando o valor de entrada
    def depositeComDesconto(self, valor):
        self.saldo = self.saldo + valor - (valor*0.1)/100

    # Método sacar valor da conta, se o saldo for maior que o valor de entrada 
    # faz a operação e retorna True, senão retorna False
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return True
        else:
            return False     

# Classe Conta Bonificada 
class contaBonificada(Conta):

    # "Construtor" da classe Conta Bonificada
    def __init__(self, numConta):
        super().__init__(numConta)
        self.bonus = 0

    # Método deposite com desconto e bonus de 0.1% e 0.01% respectivamente
    def depositaComBonus(self, valor):
        self.saldo = (self.saldo + valor) - (valor*0.1)/100
        self.bonus += (valor*0.01)/100

    # Método render bonus se o saldo for maior que o valor de entrada
    def renderBonus(self):
        self.saldo = self.saldo + self.bonus
        self.bonus = 0            

# Classe Poupança  
class Poupanca(Conta):

    # metodo render, rende o saldo com 0.01% de juros 
    def render(self):
        self.saldo = self.saldo + self.saldo*0.01

# Classe Banco 
class Banco():

    # "Construtor" da classe Banco
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    # método getNome, retorna o nome do banco
    def getNome(self):
        return self.nome

    # método criarConta gerar um número aleatório 
    # entre 0 e 1000, que será o número da conta
    def criarConta(self):
        num = random.randint(0, 1000)
        c = Conta(num)
        self.contas.append(c)
        return num

    # método criarContaBonificada, gerar um número aleatório 
    # entre 0 e 1000, que será o número da conta bonificada
    def criarContaBonificada(self):
        num = random.randint(0, 1000)
        a = contaBonificada(num)
        self.contas.append(a)
        return num    

    # método criarPoupanca
    def criarPoupanca(self):
        num = random.randint(0, 1000)
        p = Poupanca(num)
        self.contas.append(p)
        return num

    # método consultaSaldo
    def consultaSaldo(self, numConta):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.saldo
        return -1

    # método depositar nele é verificado se a conta existe 
    # e se é uma conta bonificada se for deposita com bonus
    def depositarComDesconto(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta and isinstance(conta, contaBonificada):
                conta.depositaComBonus(valor)
                return True
            else:
                conta.depositeComDesconto(valor)
                
                return True   
        return False      

    # método sacar nele é verificado se a conta existe 
    # e se o saldo é maior que o valor de entrada
    def sacar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.sacar(valor)
        return False

    # método renderPoupanca nele é verificado 
    # se a conta existe e se é uma conta poupança  
    def renderPoupanca(self, numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i, Poupanca):
                i.render()
                return True
        return False

    # método renderBonus nele é verificado 
    # se a conta existe e se é uma conta bonificada
    def renderBonus(self, numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i, contaBonificada):
                i.renderBonus()
                return True
        return False
     

 

