dia = int(input(f'Escolha o dia da semana: \n'
                f'[1] Domingo \n'
                f'[2] Segunda-feira \n'
                f'[3] Terça-feira \n'
                f'[4] Quarta-feira \n'
                f'[5] Quinta-feira \n'
                f'[6] Sexta-feira \n'
                f'[7] Sábado \n'))
if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda-feira')
elif dia == 3:
    print('Terça-feira')
elif dia == 4:
    print('Quarta-feira')
elif dia == 5:
    print('Quinta-feira')
elif dia == 6:
    print('Sexta-feira')
elif dia == 7:
    print('Sábado')
else:
    print('Valor inválido')