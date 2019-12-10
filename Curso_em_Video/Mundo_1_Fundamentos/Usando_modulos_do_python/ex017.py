#Desafio 017 do curso em video

#Programa que calcula os catetos e devolve o valor da hipotenusa

#https://www.youtube.com/watch?v=vmPW9iWsYkY&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=18

#Outro método aceitável com a biblioteca math
#from math import hypot
co = float(input('Comprimento do cateto oposto; '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
#O substituto para função acima seria...
#hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi}')
print()

