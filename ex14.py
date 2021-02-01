#importação de tempo
from time import sleep
print ('{:=^40}'.format(' BIBLIOTECA '))
sleep(1)
name = input('Nome do solicitante: ')
#seção de escolha de livros
print('Escolha uma das opções abaixo')
sleep(1)
print ('''1) Me Poupe!
2) Seja Foda!
3) O Milagre da manhã
4) Namoro Blindado 
5) Quem pensa enriquece 
6) Descubra o seu destino
7) O poder da ação
8) Treinamento em Lógica de Programação
9) Pense em Python
10) Aprenda Python 3 do jeito certo!
       ''')
#seção para escolha do usuário
option = int(input('Sua escolha: '))
if option > 10:
    print (f'{name} você não escolheu a opção correta... Tente novamente')
else: 
    print (f'{name} você escolheu o {option}° livro')