num = int(input('Digite um numero: '))

if num % 3 == 0 and num % 5 == 0:
    print('O numero é divisivel por 3 e 5')
elif num % 3 == 0 and num % 5 != 0:
    print('O numero é divisivel por 3 e não por 5')
elif num % 3 != 0 and num % 5 == 0:
    print('O numero é divisivel por 5 e não por 3')
else:
    print('O numero não é divisivel por 3 e 5')