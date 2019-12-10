#Desafio 011 do curso em video

#Programa que entrega quantos litros de tinta serão gastos numa parede (m²)

#https://www.youtube.com/watch?v=mzSJpn9ldt4&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=12

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m²')
print()
print('Sabendo que para cada m² é necessário 1 litro de tinta...')
print()
print(f'Para pintar essa parede, você precisará de {area/2}L de tinta')
print()

