num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))

if num1 == num2 == num3:
    print('Esses numeros são iguais')
elif num1 > num2 and num1 > num3:
    print('O',num1,'é o maior numero entre os tres')
elif num2 > num1 and num2 > num3:
    print('O',num2,'é o maior numero entre os tres')
else:
    print('O', num3, 'é o maior numero entre os tres')