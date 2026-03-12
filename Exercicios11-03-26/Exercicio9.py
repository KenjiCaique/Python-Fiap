preco = float(input('Digite o valor do produto: '))
desc = int(input('Digite o valor do desconto em %: '))

preco_final = preco * (desc/100)

print('Preço:',preco,'\n'
    'Desconto: ',desc,'\n'
    'Preço final: ',preco_final)
