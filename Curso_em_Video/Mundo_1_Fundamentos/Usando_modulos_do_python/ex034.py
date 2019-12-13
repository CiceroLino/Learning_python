#Desafio 034 do curso em video

#Programa que calcula o aumento salarial de um funcionário

#https://www.youtube.com/watch?v=Sfadj_AzKHw&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=35

print()
salario = float(input('Digite o salário do funcionário: '))

if salario > 1250:
    salario_c = salario + (salario * (10/100))

else:
    salario_c = salario + (salario * (15/100))

print(f'O salario que antes era R${salario}, com aumento passa a ter o valor de R${salario_c}')
print()

