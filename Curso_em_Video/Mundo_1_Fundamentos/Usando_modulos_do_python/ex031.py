#Desafio 031 do curso em video

#Programa que calcula o custo da viagem

#https://www.youtube.com/watch?v=PGqHyzWoagc&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=32

from time import sleep
print()
distancia = float(input('Qual é a distância da sua viagem? '))
print()
sleep(1)
print(f'Você está preste a começar uma viagem de {distancia}Km')
sleep(1)
print()
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E o preço da sua passagem será de R${preco:.2f}')
print()

