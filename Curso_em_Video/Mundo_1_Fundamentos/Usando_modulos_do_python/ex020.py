#Desafio 020 do curso em video

#Programa que sortea uma ordem na lista de itens

#https://www.youtube.com/watch?v=OPh0nngbBSY&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=21

from random import shuffle
print()
n1 = str(input('Primeiro item da lista: '))
n2 = str(input('Segundo item da lista: '))
n3 = str(input('Terceiro item da lista: '))
n4 = str(input('Quarto item da lista: '))
n5 = str(input('Quinto item da lista: '))
lista = [n1, n2, n3, n4, n5]
shuffle(lista)
print('A ordem de apresentação será...')
print(lista)
print()

