idade = int(input('Digite sua idade: '))
tem_autorizacao = False

if idade >= 16 or (idade >= 12 and tem_autorizacao == False):
    print('Pode assistir o filme')
else:
    print('Não pode assistir o filme')