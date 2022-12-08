#Faça um programa que use a função valorPagamento para
#determinar o valor a ser pago por uma prestação de uma conta. O 
#programa deverá solicitar ao usuário o valor da prestação e o
#número de dias em atraso e passar estes valores para a função
#valorPagamento, que calculará o valor a ser pago e devolverá este
#valor ao programa que a chamou. O programa deverá então exibir o
#valor a ser pago na tela. Após a execução o programa deverá voltar
#a pedir outro valor de prestação e assim continuar até que seja
#informado um valor igual a zero para a prestação. Neste momento o
#programa deverá ser encerrado, exibindo o relatório do dia, que
#conterá a quantidade e o valor total de prestações pagas no dia. O
#cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos
#sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar
#3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(valorPrestacao, diasAtraso): #função que calcula o valor a ser pago
    valorPrestacao = valorPrestacao + (valorPrestacao * 0.03) + (valorPrestacao * 0.001 * diasAtraso) #calcula o valor a ser pago
    return valorPrestacao #retorna o valor a ser pago

valorPrestacao = 1 #valor da prestação
valorTotal = 0  #valor total pago
contador = 0 #contador de prestações pagas

while(valorPrestacao != 0): #enquanto o valor da prestação for diferente de zero
    valorPrestacao = float(input("Digite o valor da prestação: ")) #lê o valor da prestação
    diasAtraso = int(input("Digite o número de dias em atraso: ")) #lê o número de dias em atraso
    valorTotal += valorPagamento(valorPrestacao, diasAtraso) #calcula o valor a ser pago e incrementa o valor total pago
    contador += 1 #incrementa o contador de prestações pagas

print("O valor total pago é: %.2f" % valorTotal) #imprime o valor total pago
print("O número de prestações pagas é: %d" % contador) #imprime o número de prestações pagas
