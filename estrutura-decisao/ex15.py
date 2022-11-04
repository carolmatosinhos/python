lado1 = float(input('Informe o primeiro lado do triângulo: '))
lado2 = float(input('Informe o segundo lado do triângulo: '))
lado3 = float(input('Informe o terceiro lado do triângulo: '))

if lado1+lado2 >= lado3:
    print('É um triangulo')
    if lado1 == lado2 and lado1 != lado3 or lado2 == lado3 and lado1 != lado3 or lado3 == lado1 and lado2 != lado1:
        print('O triangulo é isósceles')
    elif lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print('O triangulo é equilátero')
    else:
        print('O triangulo é escaleno')
else:
    print('Não é um triângulo')