nota = float(input('Digite a sua nota: '))

if nota >= 7:
    print('Voce foi aprovado!!')
elif nota >= 5  and nota < 7:
    print('Voce esta de recuperação')
else:
    print('Voce esta reprovado')