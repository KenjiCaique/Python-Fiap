Num1 = float(input('Digite o primeiro numero: '))
Num2 = float(input('Digite o segundo numero: '))
print('Escolha uma das opcoes: \n'
      'Soma(1) \n'
      'Subtração(2) \n'
      'Multiplicaçao(3) \n'
      'Divisão(4)')
Escolha = int(input('Digite sua escolha: '))

if Escolha == 1:
    soma = Num1 + Num2
    print('A soma dos numeros é: ',soma)
elif Escolha == 2:
    sub = Num1 - Num2
    print('A subtração dos numeros é: ',sub)
elif Escolha == 3:
    mult = Num1 * Num2
    print('A multiplicaçao dos numeros é: ',mult)
elif Escolha == 4:
    div = Num1 / Num2
    print('A divisão dos numeros é:',div)
else:
    print('Essa opcão nao existe!!!')