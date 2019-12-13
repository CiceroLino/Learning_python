#Desafio 036 do curso em video

#Programa que aprova ou não um emprestimo.

#https://www.youtube.com/watch?v=IV13X0QOMU8&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=37

print()
casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
minimo = salario * (30 / 100)

prestacao = casa / (anos * 12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f} ')
#print(f'COMPARANDO tem que pagar {prestacao:.2f} e o mínimo é de {minimo:.2f}')
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
print()

