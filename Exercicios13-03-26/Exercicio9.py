idade = int(input('Digite sua idade: '))

if idade <= 12 and idade >= 0:
    print('Você é uma criança')
elif idade >= 13 and idade <= 17:
    print('Voce é adolecente')
elif idade >= 60:
    print('Voce é idoso')
else:
    print('Voce é adulto')
