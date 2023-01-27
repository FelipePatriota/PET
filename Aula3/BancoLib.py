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


    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        # a linha abaixo insere uma nova conta no banco de dados
        self.cursor.execute(f"INSERT INTO CONTAS (NUM, SALDO) VALUES ({num}, 0)")
        # a linha abaixo salva as alterações no banco de dados
        self.con.commit()
        return num

    def consultaSaldo(self, numConta):
        # a linha abaixo consulta o saldo de uma conta no banco de dados
        self.cursor.execute(f"SELECT SALDO FROM CONTAS WHERE NUM = {numConta}")
        # a linha abaixo recupera o saldo da conta
        saldo = self.cursor.fetchone()
        if saldo:
            return saldo[0]
        else:
            return None

    def depositar(self, numConta, valor):
        # a linha abaixo atualiza o saldo de uma conta no banco de dados
        self.cursor.execute(f"UPDATE CONTAS SET SALDO = SALDO + %s WHERE NUM = %s", (valor, numConta))
        # a linha abaixo salva as alterações no banco de dados
        self.con.commit()
  

    def sacar(self, numConta, valor):
        # a linha abaixo consulta o saldo de uma conta no banco de dados
        self.cursor.execute("SELECT SALDO FROM CONTAS WHERE NUM = %s", (numConta,))
        # a linha abaixo recupera o saldo da conta
        saldo = self.cursor.fetchone()
        if saldo and saldo[0] >= valor:
            # a linha abaixo atualiza o saldo de uma conta no banco de dados
            self.cursor.execute("UPDATE CONTAS SET SALDO = SALDO - %s WHERE NUM = %s", (valor, numConta))
            self.con.commit()
            return True
        else:
            return False

    def close(self):
        # a linha abaixo fecha a conexão com o banco de dados
        self.con.close()   
        # a linha abaixo fecha o cursor	
        self.cursor.close()