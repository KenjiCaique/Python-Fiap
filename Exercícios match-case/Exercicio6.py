num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
operador = input('Digite um operador entre \n'
                 '+ \n'
                 '- \n'
                 '* \n'
                 '/ \n'
                 'Escolha: ')
match operador:
    case '+':
        soma = num1 + num2
        print('A soma dos numeros da:',soma)
    case '-':
        sub = num1 - num2
        print('A subtração dos numeros da:', sub)
    case '*':
        mult = num1 * num2
        print('A multiplicação dos numeros da:', mult)
    case '/':
        div = num1 / num2
        print('A divisão dos numeos da:',div)
    case _:
        print('Opção invalida')


