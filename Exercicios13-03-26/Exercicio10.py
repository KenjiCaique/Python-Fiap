num = int(input('Digite um Ano: '))

restante = num % 4

if restante == 0:
    print('Este ano é bissexto')
else:
    print('Este ano não é bissexto')