peso= float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

IMC = peso / (altura*altura)

if IMC < 18.5:
    print('Abaixo do peso')
elif IMC >= 18.5 or IMC <= 24.9:
    print('Normal')
elif IMC >=30:
    print('Obesidade')
else:
    print('Sobrepeso')
