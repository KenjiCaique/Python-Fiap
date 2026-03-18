compra = float(input('Digite o valor de uma compra: '))

desconto = compra-(compra*0.1) if compra >= 100 else compra

print('O valor da compra é:',desconto)