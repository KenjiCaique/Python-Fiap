nota = float(input('Digite sua nota: '))

if nota < 0 or nota > 10:
    print('Esta nota é invalida!!')
    exit()

if nota >= 9:
    print('Sua nota é A')
elif nota >= 7:
    print('Sua nota é B')
elif nota >= 5:
    print('Sua nota é C')
else:
    print('Sua nota é D')