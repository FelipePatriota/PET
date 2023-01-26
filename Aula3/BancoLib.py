import random
import mysql.connector

# Aluno: Felipe Patriota 
# a linha abaixo cria uma conexão com o banco de dados 
con = mysql.connector.connect(user='sql10593359',
                              password='InzuW7Dv37',
                              host='sql10.freemysqlhosting.net',
                              port=3306,
                              database='sql10593359')

# a linha abaixo cria um cursor para executar comandos SQL
cursor = con.cursor()

# Criação da tabela Conta
class Conta():
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0

    def deposite(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return True
        else:
            return False


class Banco():
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        c = Conta(num)
        self.contas.append(c)
        return num

    def consultaSaldo(self, numConta):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.saldo
        return -1

    def depositar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                conta.deposite(valor)

    def sacar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.sacar(valor)