nota = float(input('Digite sua nota: '))

resultado = "Aprovado" if nota >= 7 and nota <= 10 else\
            "Recuperação" if nota >= 5 and nota <=7 else\
            "Reprovado" if nota < 5 else\
            "Opção invalida"

print(resultado)