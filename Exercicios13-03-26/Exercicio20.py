usuario =  "admin"
senha = "python123"

user = input('Digite o usuario: ')
password = input('Digite a senha: ')

if user == usuario and password == senha:
    print('Login realizado com sucesso!!')
else:
    print('Usuario ou senha incorretos')