#Desafio 004 do curso em video

#Programa que disseca uma variável

#https://www.youtube.com/watch?v=tHYxjJxtJko&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=4

algo = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(algo))
print('Só tem espaços? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético? ', algo.isalpha())
print('É alfanumérico? ', algo.isalnum())
print('Está em maiúsculas? ', algo.isupper())
print('Está em minúsculas? ', algo.islower())
print('Está capitalizada? ', algo.istitle())

