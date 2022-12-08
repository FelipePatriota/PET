#Leia a hora inicial, minuto inicial, hora final e minuto final de
#um jogo. A seguir calcule a duração do jogo.
#Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

horaInicial = int ( input ( "Digite a hora inicial: " ) ) #leia a hora inicial
minutoInicial = int ( input ( "Digite o minuto inicial: " ) ) #leia o minuto inicial
horaFinal = int ( input ( "Digite a hora final: " ) ) #leia a hora final
minutoFinal = int ( input ( "Digite o minuto final: " ) ) #leia o minuto final

if ( horaInicial < horaFinal ) : #se a hora inicial for menor que a hora final
    duracaoHoras = horaFinal - horaInicial #calcule a duração em horas
    duracaoMinutos = minutoFinal - minutoInicial #calcule a duração em minutos
else : #se a hora inicial for maior ou igual a hora final
    duracaoHoras = 24 - horaInicial + horaFinal #calcule a duração em horas
    duracaoMinutos = minutoFinal - minutoInicial #calcule a duração em minutos

if ( duracaoMinutos < 0 ) : #se a duração em minutos for negativa
    duracaoHoras -= 1 #decrementa a duração em horas
    duracaoMinutos += 60 #incrementa a duração em minutos

print ( "O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % ( duracaoHoras , duracaoMinutos ) ) #imprime o resultado





