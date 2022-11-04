produto1 = float(input('Informe o preço do 1º produto: '))
produto2 = float(input('Informe o preço do 2º produto: '))
produto3 = float(input('Informe o preço do 3º produto: '))

if produto1 < produto2 and produto1 < produto3:
    print('Você deve comprar o 1º produto.')
elif produto2 < produto1 and produto2 < produto3:
    print('Você deve comprar o 2º produto.')
elif produto3 < produto1 and produto3 < produto2:
    print('Você deve comprar o 3º produto.')
else:
    print('Há valores repetidos')