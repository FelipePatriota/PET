#Faça um programa que leia 5 valores inteiros. Conte quantos
#destes valores digitados são pares e mostre esta informação.

contadorPar = 0 #contador de números pares

for i in range(5): #repete 5 vezes
    i = int(input("Digite um número inteiro: ")) #lê um número inteiro
    if i % 2 == 0: #verifica se o número é par
        contadorPar += 1  #incrementa o contador de números pares

print("Você digitou %d números pares." % contadorPar) #imprime o resultado