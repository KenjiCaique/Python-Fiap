from jinja2.nodes import Break

num = int(input('Digite um Numero: '))

if num == 0:
    print('Este numero é o zero')
    exit()
else:
    restante = num % 2
if restante == 0:
    print('Este numero é par')
else:
    print('Este numero é impar')