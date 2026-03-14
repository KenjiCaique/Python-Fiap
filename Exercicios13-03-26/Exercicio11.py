compra = float(input('Digite o valor da compra: '))

if compra >= 1000:
    desconto = (10/100)*compra
    valfinal = compra - desconto
    print('O valor do desconto é', desconto, 'e o valor final do prouto fica', valfinal)
elif compra >= 500 and  compra < 1000:
    desconto = (5/100)*compra
    valfinal = compra - desconto
    print('O valor do desconto é',desconto,'e o valor final do prouto fica',valfinal)
else:
    print('Não tem desconto')