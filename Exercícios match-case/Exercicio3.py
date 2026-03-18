letra = input('digite uma letra: ')

match letra:
    case 'm':
        print('Bom Dia')
    case 't':
        print('Boa Tarde')
    case 'n':
        print('Boa Noite')
    case _:
        print('Turno Invalido')