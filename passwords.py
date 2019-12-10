#Creditos: Youtuber Programador Sagaz

#https://www.youtube.com/watch?v=UV8EBsnU-GQ

#Descrição do projeto segundo Programador Sagaz

#Uma das melhores maneiras de se aprofundar na programação, é criando pequenos projetos que fazem algo útil para você. 

#Nesse projeto, eu dou o primeiro passo rumo à um gerenciador de senhas real usando Python e SQLite. 

#NOTA IMPORTANTE: ESSE PROJETO É PARA FIM DE ESTUDO. Então não é recomendado o uso com suas senhas pessoais ou de quem quer que seja.
import sqlite3

MASTER_PASSWORD = "123456"

senha = input('Insira sua senha master: ')
if senha != MASTER_PASSWORD:
    print('Senha inválida. Encerrando ...')
    exit()

#Arquivo binário 'passwords.db' onde ficarão armazenado as senhas.
conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
);
''')
# Menu com as principais escolhas
def menu():
    print('******************************')
    print('* i : inserir nova senha     *')
    print('* l : listar serviços salvos *')
    print('* r : recuperar uma senha    *')
    print('* s : sair                   *')
    print('******************************')

# Função que recupera as senhas
def get_password(service):
    cursor.execute(f'''
    	SELECT username, password FROM users
    	WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
    	print('Serviço não cadastrado (use "l" para verificar os serviços).')
    else:
    	for user in cursor.fetchall():
    		print(user)

# Função para inserir senhas
def insert_password(service, username, password):
    cursor.execute(f''' 
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()

# Função que mostra os serviços
def show_services():
    cursor.execute(''' 
    	SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

        
while True:
    menu()
    op = input('O que deseja fazer? ')
    if op not in ['i', 'l', 'r', 's']:
        print('Opção inválida!')
        continue

    if op == 's':
        break

    if op == 'i':
   		service = input('Qual o nome do serviço? ')
   		username = input('Qual o nome de usuário? ')
   		password = input('Qual a senha? ')
   		insert_password(service, username, password)

    if op == 'l':
        show_services()

    if op == 'r':
    	service = input('Qual o serviço para o qual quer a senha? ')
    	get_password(service)

conn.close()
