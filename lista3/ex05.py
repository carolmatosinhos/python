num = int(input('Digite um número inteiro: '))
conv = int(input('Qual a base de conversão? \n'
                 '[1] Binário \n'
                 '[2] Octal \n'
                 '[3] Hexadecimal \n'))

if conv == 1:
    print(f'O número {num} convertido em binário é {bin(num)}')
elif conv == 2:
    print(f'O número {num} convertido em octal é {oct(num)}')
elif conv == 3:
    print(f'O número {num} convertido em binário é {hex(num)}')
else:
    print('Valor informado invalido')