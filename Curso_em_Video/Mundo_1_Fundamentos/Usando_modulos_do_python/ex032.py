#Desafio 032 do curso em video

#Programa que calcula ano bissexto

#https://www.youtube.com/watch?v=cyGY_83m4Xw&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=33

from datetime import date
print()
ano = int(input('Que ano você quer analizar? Coloque 0 para analizar o ano atual: '))
print()
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO É BISSEXTO.')
print()

