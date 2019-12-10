#Desafio 008 do curso em video

#Programa que converte medidas

#https://www.youtube.com/watch?v=KjcdG05EAZc&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=9

medida = float(input('Uma distância em metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print(f'A medida de {medida} corresponde a:\n{km}km\n{hm}hm\n{dam}dam\n{dm}dm\n{cm}cm\n{mm}mm')
print()

