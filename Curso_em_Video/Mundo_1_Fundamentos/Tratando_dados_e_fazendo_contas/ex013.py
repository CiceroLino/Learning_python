#Desafio 013 do curso em video

#Programa que calcula aumento salarial

#https://www.youtube.com/watch?v=cTkivN8XcJ0&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=14

value = float(input('Qual é o salário do funcionário? '))
value_up = int(input('Qual é o percentual do aumento de salário? '))
new_value = value + (value * value_up/100)
print(f'O funcionário que passava a ganhar R${value}, com {value_up}% de aumento, passa a receber R${new_value} ')
print()

