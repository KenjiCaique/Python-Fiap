idade=int(input('Digite sua idade: '))

if idade < 16:
    print('Não Vota!!')
elif idade >=16 or  idade <= 17 or idade >= 70:
    print('Voto opcional')
else:
    print('Voto Obigatorio!!')