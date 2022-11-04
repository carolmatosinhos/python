a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('Informe o terceiro número: '))

if a < c:
    a, c = c, a

if a < b:
    a, b = b, a

if b < c:
    b, c = c, b

print(f'A ordem decrescente é {a}, {b} e {c}')