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

# Criação da tabela Banco
class Banco():

    def __init__(self, nome):
        
        self.nome = nome
        self.con = con
        # a linha abaixo cria um cursor para executar comandos SQL
        self.cursor = self.con.cursor()
        # a linha abaixo cria a tabela Conta caso ela não exista
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Conta (numero INT, saldo INT)''')
        # a linha abaixo salva as alterações no banco de dados
        self.con.commit()


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