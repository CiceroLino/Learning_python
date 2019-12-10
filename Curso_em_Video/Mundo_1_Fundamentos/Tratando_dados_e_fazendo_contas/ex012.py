#Desafio 012 do curso em video

#Programa que calcula descontos

#https://www.youtube.com/watch?v=4MAmKOT9FeU&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=13

print('--'*25)
value = float(input('Qual é o preço do produto? R$ '))
num = int(input('Quanto é a porcentagem do desconto do produto? ')) 
new_value = value - (value * num / 100)
print(f'O produto que custava {value}, na promoção com desconto de {num}% vai custar R${new_value}')
print()

