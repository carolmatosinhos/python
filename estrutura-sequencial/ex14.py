peso = int(input('Informe o peso dos peixes: '))
excesso = peso-50
multa = float(excesso*4)


if peso > 50:
    print(f'O peso dos peixes foram maior que o permitido. Você deverá pagar multa por excesso. \n'
          f'Foram {excesso}kg de excesso \n'
          f'Valor da multa R${multa}')
else:
    print('Não houve excessos')    