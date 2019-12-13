print('---'*20)
aluno = input('Digite o número que simboliza a posição de registro do aluno: ')
print('---'*20)
semestre = input('Digite o número do semestre do aluno:\nOpção válida somente 1 ou 2 ')

print()
engenharia = ['produção','petróleo','civil','elétrica','mecânica','automoção']

ano_ingresso = input('Digite o ano que irá ingressar na Universidade: ')
print('---'*20)

print('==='*20)
print('Cursos de engenharia disponíveis: ')
print('==='*20)

print('Engenharias:\n\n[0] Produção\n[1] Petróleo\n[2] Civil\n[3] Elétrica\n[4] Mecânica\n[5] Automoção\n')

curso = input('Digite um número para a engenharia escolhida: ')

#Exemplo de ID = [ano = 119] [1 = curso] [521 = alunos] [2 = semestre]
ID = ano_ingresso + curso + aluno + semestre
print(f'O ID do aluno será {ID}')
