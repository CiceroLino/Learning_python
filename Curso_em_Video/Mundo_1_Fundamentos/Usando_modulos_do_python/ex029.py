#Desafio 029 do curso em video

#Programa que simula um radar eletrônico

#https://www.youtube.com/watch?v=hgJ_ETNGSj8&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=30

velocidade = float(input('Qual é a velocidade atual do carro? '))
print()
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 Km/h')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
else:
    print('Tenha um bom dia! Dirija com segurança!')
print()

