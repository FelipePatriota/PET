#Escreva um programa que repita a leitura de uma senha até
#que ela seja válida. Para cada leitura de senha incorreta
#informada, escrever a mensagem "Senha incorreta. Tente
#novamente". Quando a senha for informada corretamente deve ser
#impressa a mensagem "Acesso permitido" e o algoritmo encerrado.
#Considere que a senha correta é o valor 2022. 
#Aluno: Felipe Patriota

senhaSalva = 2022 #senha correta
senhaInserida = '' #senha inserida pelo usuário

while(senhaSalva != senhaInserida): #enquanto a senha inserida for diferente da senha correta
    senhaInserida = int(input("Digite a senha: ")) #lê a senha inserida
    if(senhaInserida != 2022): #se a senha inserida for diferente da senha correta
        print("Senha incorreta, tente novamente!") #imprime a mensagem de senha incorreta
    elif (senhaInserida == 2022): #se a senha inserida for igual a senha correta
        print("Acesso permitido") #imprime a mensagem de acesso permitido
 