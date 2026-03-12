Num = float(input('Digite um numero: '))
print('Escolha uma das opcoes: \n'
      'Dobro(1) \n'
      'Triplo(2) \n'
      'Raiz quadrada(3)')
Escolha = int(input('Digite sua escolha: '))

if Escolha == 1:
    dobro = Num * 2
    print('O dobro é: ',dobro)
elif Escolha == 2:
    triplo = Num * 3
    print('O triplo é: ',triplo)
elif Escolha == 3:
    Raiz_quadrada = Num ** 0.5
    print('A raiz quadrada é: ',Raiz_quadrada)
else:
    print('Essa opcão nao existe!!!')