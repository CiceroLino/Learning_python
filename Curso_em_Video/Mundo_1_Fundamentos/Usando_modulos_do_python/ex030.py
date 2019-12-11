#Desafio 030 do curso em video

#Programa que verifica se um número é par ou ímpar

#https://www.youtube.com/watch?v=4vFCzKuHOn4&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=31

print()
num = int(input('Digite um número inteiro qualquer: '))
resultado = num % 2
print()
if resultado == 0:
    print(f'O número {num} é PAR.')
else:
    print(f'O número {num} é ÍMPAR.')
print()

