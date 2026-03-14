num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

operação = input('Escolha uma das 4 operações \n'
                       '+ \n'
                       '- \n'
                       '* \n'
                       '/ \n'
                       'Escolha: ')

if operação == '+':
    soma = num1 + num2
    print('A soma dos numeros é',soma)
elif operação == '-':
    sub = num1 - num2
    print('A subtração dos numeros é',sub)
elif operação == '*':
    mult = num1 * num2
    print('A multiplicação dos numeros é',mult)
elif operação == '/':
    div = num1 / num2
    print('A divisão dos numeros é',div)
else:
    print('Esta opção nao existe!!')


