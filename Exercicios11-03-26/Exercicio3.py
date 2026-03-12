Base = float(input('Digite a medida da base do retangulo: '))
Altura = float(input('Digite a medida da altura do retangulo: '))

if Base == Altura:
    print('Erro isso é um quadrado!!')
else:
    Area = Base * Altura
    print('A area do retangulo é: ',Area)
