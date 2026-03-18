codigo = int(input('Digite um codigo: '))

match codigo:
    case 1|2:
        print('Alimentos')
    case 3|4:
        print('Limpeza')
    case 5|6:
        print('Higiene')
    case _:
        print('Codigo Invalido')
