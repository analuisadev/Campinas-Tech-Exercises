from random import randint
from time import sleep
computer = randint(0, 100)
print ('{:=^40}'.format(' LOTERIA '))
name = input('Seu nome: ')
number = int(input('Escolha um número de 1 a 100: '))
sleep(1)
print ('PROCESSANDO...')
sleep(1)
if number == computer:
    print (f'{name} você acertou!\n O número que você digitou foi {number}\n e o sorteado foi o mesmo valor!\n')
else:
    print (f'{name} você errou! O número digitado foi {number} e o sorteado foi {computer}')