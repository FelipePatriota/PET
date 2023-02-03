#Faça uma função chamada calculaSalario que recebe como
#parâmetro o valor do salário bruto calcula o salário líquido. O salário 
#líquido é calculado a partir do salário bruto, primeiro descontando 11%
#referente ao INSS, e do resultado, descontando-se 15% de imposto de
#renda.  

def calculaSalario(salarioBruto): #função que calcula o salário líquido  
    salarioLiquido = salarioBruto - (salarioBruto * 0.11)  #desconta 11% do INSS
    salarioLiquido = salarioLiquido - (salarioLiquido * 0.15) #desconta 15% do imposto de renda
    return salarioLiquido #retorna o salário líquido

salarioBruto = float(input("Digite o salário bruto: ")) #lê o salário bruto
salarioLiquido = calculaSalario(salarioBruto) #calcula o salário líquido
print("O salário líquido é: %.2f" % salarioLiquido)  #imprime o resultado

