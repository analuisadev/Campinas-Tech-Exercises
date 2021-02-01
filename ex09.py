#importando o math
import math
#Definindo o raio e area do círculo 
raio = float(input('Digite o raio do circulo em metros: '))
area = math.pi * (raio ** 2)
print (f'A área do cícurlo é {raio:2.f}')
#Definindo perímetro do cículo
perimetro = 2 * (math.pi * (raio**2))
print (f'O perímetro do cículo é {perimetro:.2f}')