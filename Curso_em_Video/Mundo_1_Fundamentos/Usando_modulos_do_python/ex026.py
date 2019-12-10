#Desafio 026 do curso em video

#Programa que verifica a primeira e a última ocorrência de uma string

#https://www.youtube.com/watch?v=23UOVEetNPY&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=27

print()
frase = str(input('Digite uma frase: ')).lower().strip()
print(f"A letra (a) aparece {frase.count('a')} vezes na frase")
print(f'A primeira letra (a) apareceu na posição {frase.find("a") + 1}')
print(f'A ultima letra (a) apareceu na posição {frase.rfind("a") + 1}')
print()

