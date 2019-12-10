#Desafio 010 do curso em video

#Programa que faz a conversão do real para moeda escolhida

#Terceira vez que refaço o desafio

op = ['dolar', 'euro', 'iene']
values = [4, 4.44, 0.037]
print('=='* 25)
print('Opções:\n(0) para dolar\n(1) para euro\n(2) para iene')
op = int(input('Qual tipo de conversão você desenha? '))
print('=='* 25)
print()
print()
real = float(input('Digite quantos reais você quer converter. '))
print(f'{real} reais é equivalente a {real/values[op]} ')
print()


