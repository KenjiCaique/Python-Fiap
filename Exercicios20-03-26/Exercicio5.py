num = int(input('Digite um numero de 1 a 10: '))
tabuada = 1
resultado = 0

while tabuada <= 10:
    print(num,'x',tabuada,'=',resultado)
    tabuada += 1
    resultado = num*tabuada