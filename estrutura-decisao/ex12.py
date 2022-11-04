hora = float(input('Qual o valor da sua hora de trabalho? '))
mes = float(input('Quantas horas você trabalhou no mês? '))
salariobt = hora*mes
sindicato = (3*salariobt)/100
fgts = (11*salariobt)/100
inss = (10*salariobt)/100

if salariobt <= 900:
    print(f'Salário Bruto: R${salariobt} \n'
          f'( - ) IR (5%): Isento \n'
          f'( - ) INSS (10%): {inss} \n'
          f'FGTS (11%): {fgts} \n'
          f'Total de descontos: {inss} \n'
          f'Salário Liquido: {salariobt-inss} \n')
elif salariobt <= 1500:
    print(f'Salário Bruto: R${salariobt} \n'
          f'( - ) IR (5%): {((5*salariobt)/100)} \n'
          f'( - ) INSS (10%): {inss} \n'
          f'FGTS (11%): {fgts} \n'
          f'Total de descontos: {((5*salariobt)/100) + inss} \n'
          f'Salário Liquido: {salariobt-((5*salariobt)/100)-inss} \n')
elif salariobt <= 2500:
    print(f'Salário Bruto: R${salariobt} \n'
          f'( - ) IR (5%): {((10*salariobt)/100)} \n'
          f'( - ) INSS (10%): {inss} \n'
          f'FGTS (11%): {fgts} \n'
          f'Total de descontos: {((10*salariobt)/100) + inss} \n'
          f'Salário Liquido: {salariobt-((10*salariobt)/100)-inss} \n')
elif salariobt >= 2500:
    print(f'Salário Bruto: R${salariobt} \n'
          f'( - ) IR (5%): {((20*salariobt)/100)} \n'
          f'( - ) INSS (10%): {inss} \n'
          f'FGTS (11%): {fgts} \n'
          f'Total de descontos: {((20*salariobt)/100) + inss} \n'
          f'Salário Liquido: {salariobt-((20*salariobt)/100)-inss} \n')

