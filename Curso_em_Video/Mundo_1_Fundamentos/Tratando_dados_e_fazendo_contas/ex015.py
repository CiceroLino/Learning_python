#Desafio 015 do curso em video

#Programa que simula o aluguel de carros

#https://www.youtube.com/watch?v=I4NYUeetLAc&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=16

print()
days = int(input('Quantos dias se passaram desde que o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
value = (days * 60) + (km * 0.15)
print(f'O total a pagar é de R${value}')
print()

