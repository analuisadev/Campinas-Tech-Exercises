from time import sleep
import sys
print ('{:=^40}'.format(' TUTORIAL PARA LIGAR UM CARRO '))
resp = str(input('Deseja prosseguir? S/N ')).upper().strip()[0]
if resp in 'N':
    sys.exit()
else: 
    print ('{:=^40}'.format(' TUTORIAL '))
    sleep(1)
    print ('1° Pegue a chave do carro')
    sleep(1)
    print ('2° Abra a porta do carro')
    sleep(1)
    print ('3° Entre dentro do carro e sente no banco')
    sleep(1)
    print ('4° Coloque a chave no lugar correto')
    sleep(1)
    print ('5° Vire a chave, ligando o carro')
print ('{:=^40}'.format(' FIM '))
