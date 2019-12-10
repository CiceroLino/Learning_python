#Desafio 024 do curso em video

#Programa que verifica a primeira palavra de um texto e retorna o valor True/False

#https://www.youtube.com/watch?v=QroT8cZMRnc&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=25

print()
print('Digite um texto que começa com a palavra python.\nE não importa a maneira que for digitada.\nO importante é iniciar o texto com essa palavra.')
print()
palavra_V = str(input('Digite um texto: ')).strip()
print(palavra_V[:6].upper() == 'PYTHON')
print()

