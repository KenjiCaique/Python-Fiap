num1= float(input('Digite a primeira nota: '))
num2= float(input('Digite a segunda nota: '))

media = (num1 + num2)/2

if media >= 6:
    print('Voce esta aprovado com a media de:',media)
else:
    print('Voce esta reprovado')