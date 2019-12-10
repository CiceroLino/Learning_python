#Desafio 019 do curso em video

#Programa que sortea um item da lista

#https://www.youtube.com/watch?v=_Nk02-mfB5I&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=20

from random import choice
print()
n1 = str(input('Primeiro item da lista: '))
n2 = str(input('Segundo item da lista: '))
n3 = str(input('Terceiro item da lista: '))
n4 = str(input('Quarto item da lista: '))
n5 = str(input('Quinto item da lista: '))
lista = [n1, n2, n3, n4, n5]
escolhido = choice(lista)
print(f'O item escolhido (ou sorteado) foi {escolhido}')
print()

