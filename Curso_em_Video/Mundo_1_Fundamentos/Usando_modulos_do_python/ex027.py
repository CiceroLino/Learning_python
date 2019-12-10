#Desafio 027 do curso em video

#Outro programa que mostra a primeira string e ultima string dentro de uma string (transformada em lista)

#https://www.youtube.com/watch?v=SifYYsXhLM8&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=28

print()
nome = str(input('Digite seu nome completo: ')).strip()
lista_nome = nome.split()
print(lista_nome)
print(f'Seu primeiro nome é {lista_nome[0]}')
print(f'Seu último nome é {lista_nome[-1]}')
print()

