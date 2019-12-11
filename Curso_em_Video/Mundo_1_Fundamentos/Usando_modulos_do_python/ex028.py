#Desafio 028 do curso em video

#Jogo da adivinhação

#https://www.youtube.com/watch?v=kchC5KLZSZ4&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=29

from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')

