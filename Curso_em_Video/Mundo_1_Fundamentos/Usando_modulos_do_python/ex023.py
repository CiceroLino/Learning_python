#Desafio 023 do curso em video

#Programa que separa dígitos de um número

#https://www.youtube.com/watch?v=wD2aerLMBWA&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=24

print()
num = int(input('Informe um número: '))
print(f'Analizando o número {num}...')

#Primeiro método que está comentado é Válido para somente e todo número na casa de milhar
'''
n = str(num)
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')
print()
'''

#Segundo método é capaz de receber outros números de até 3 dígitos. Sem a obrigatoriedade de ser 4.
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
print()

