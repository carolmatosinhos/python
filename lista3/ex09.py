velocidade = float(input('Informe a velocidade do carro em km: '))
multa = (velocidade-80)*7
if velocidade > 80:
    print(f'Você ultrapassou o limite de velocidade! \n'
           f'O valor da sua multa será {multa}')
else:
    print('Você está dentro do limite de velocidade')