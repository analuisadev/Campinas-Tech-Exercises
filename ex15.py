#importação de tempo
from time import sleep
print ('{:=^40}'.format(' FEIRA DO JAPÃO '))
#nome
name = str(input('Nome: '))
#seção de escolha
print ('{:=^40}'.format(' SEÇÃO DE FRUTAS '))
sleep(1)
print('''1) Manga
2) Maçã 
3) Uva
4) Pinha
5) Pêra
6) Mamão
7) Melancia
8) Abacate
9) Banana
10) Blueberry ''')
option = int(input('Sua escolha: '))
#seção de resultado
if option > 10: 
    print ('{name} infelizmente não temos mais que 10 opções de frutas disponíveis no momento...')
else: 
    print (f'{name} você escolheu a {option}° fruta')
