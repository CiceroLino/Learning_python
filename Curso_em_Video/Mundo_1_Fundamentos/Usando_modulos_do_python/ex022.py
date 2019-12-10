#Desafio 022 do curso em video

#Programa que analisa textos

#https://www.youtube.com/watch?v=EQQt-6QqXOs&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=23

print()
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")
print()

