#Faça um algoritmo para ler um número indeterminado de 
#dados, contendo cada um, a idade de um indivíduo. O último
#dados, que não entrará nos cálculos, contém um valor de idade
#negativa. Calcular e imprimir a idade média deste grupo de
#indivíduos. 

idade = 0 #idade do indivíduo
somaIdade = 0 #soma das idades
contador = 0 #contador de idades

while(idade >= 0): #enquanto a idade for maior ou igual a zero
    idade = int(input("Digite a idade: ")) #leia a idade
    if(idade >= 0): #se a idade for maior ou igual a zero
        somaIdade += idade #incrementa a soma das idades
        contador += 1 #incrementa o contador de idades

mediaIdade = somaIdade / contador   #calcula a média de idade
print("A média de idade é: %.2f" % mediaIdade) #imprime o resultado       