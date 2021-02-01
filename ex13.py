from time import sleep
print ('{:=^40}'.format(' AEROPORTO INTERNACIONAL '))
#leitura de nome
name = str(input('Nome: '))
sleep(1)
#seção de opções
print ('{:=^40}'.format(' OPÇÕES DE DESTINO '))
print(''' Canadá
Inglaterra
Estados Unidos
Portugal 
Rússia
Coreia do Sul
Japão
Reino Unido
África do Sul
Alemanha
Egito
Holanda''')
#resultado
option = str(input(f'{name} qual será o seu destino? ')).upper().strip()
print (f'{name} o seu destino será {option}')