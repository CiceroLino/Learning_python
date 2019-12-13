#Desafio 035 do curso em video

#Programa que recebe o comprimento de três retas e devolve o resultado de formar ou não um triângulo

#https://www.youtube.com/watch?v=NZiNphKkxhg&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=36

print()
a = float(input('[a] Primeiro segmento: '))
b = float(input('[b] Segundo segmento: '))
c = float(input('[c] Terceiro segmento: '))
print()

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR triângulo!')
    print('\nPROVA\n')
    print(f'a {a} < b {b} + c {c}')
    print(f'b {b} < a {a} + c {c}')
    print(f'c {c} < a {a} + b {b}')

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
    print('\nPROVA\n')
    print(f'a {a} < b {b} + c {c}')
    print(f'b {b} < a {a} + c {c}')
    print(f'c {c} < a {a} + b {b}')

print()
