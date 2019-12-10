#Desafio 018 do curso em video

#Programa que calcula o ângulo e retorna o seno, cosseno e tangente.

#https://www.youtube.com/watch?v=9GvsphwW26k&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=19

from math import radians, sin, cos, tan
print()
angulo = float(input('Digite o ângulo que você deseja calcular: '))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo:.2f} tem o seno de {seno:.2f}.')
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo:.2f} tem o cosseno de {cosseno:.2f}.')
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo:.2f} tem a tangente de {tangente:.2f}.')
print()

