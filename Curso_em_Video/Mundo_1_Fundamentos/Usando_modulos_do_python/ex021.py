#Desafio 021 do curso em video

#Programa que toca uma musica (formato mp3)

#https://www.youtube.com/watch?v=9FiEji_fzvk&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=22

from pygame import mixer
pygame.init()
mixer.music.load('Terranigma_magirock.mp3')
mixer.music.play()
pygame.event.wait()

