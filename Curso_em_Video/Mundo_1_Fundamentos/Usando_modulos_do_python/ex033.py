#Desafio 033 do curso em video

#Programa que lê três números e mostre qual é o maior e qual é o menor.

#https://www.youtube.com/watch?v=a_8FbW5oH6I&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=34

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#Menor

if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Maior

if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

'''
else:
	print('Todos os números são iguais.')
'''

print(f'Menor valor é {menor} e o maior é {maior}')

