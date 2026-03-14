lado1 = float(input('Digite o primeiro lado do triangulo: '))
lado2 = float(input('Digite o segundo lado do triangulo: '))
lado3 = float(input('Digie o terceiro lado do triangulo: '))

if lado1 == lado2 == lado3:
    print('Este triangulo é Equilatero')
elif lado1 != lado2 != lado3:
    print('Este triangulo é Escaleno')
else:
    print('Este triangulo é Isosceles')