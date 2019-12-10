#Desafio 014 do curso em video

#Programa que converte temperaturas

#https://www.youtube.com/watch?v=9l_Gay8BuAw&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=15

print()
c = float(input('Informe a temperatura em °C: '))
op = int(input('Transformar em Kelvin digite 1, para Fahrenheit digite 2: '))

if op == 1:
    kel = c + 273
    print(f'A temperatura de {c}°C corresponde a {kel}°K ')
elif op == 2:
    fah = (1.8 * c) + 32
    print(f'A temperatura de {c}°C corresponde a {fah}°F ')
else:
    print('Opção inválida')

print()

