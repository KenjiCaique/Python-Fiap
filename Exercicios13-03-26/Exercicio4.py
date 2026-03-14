num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

if num1 == num2:
    print('Esses numeros são iguais')
elif num1 > num2:
    print('O',num1,'é maior que o',num2)
else:
    print('O',num2,'é maior que o',num1)