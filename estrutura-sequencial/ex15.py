hora = float(input('Quanto você ganha por hora? '))
trabalho = int(input('Quantas horas você trabalhou esse mês? '))


salariobt = (hora * trabalho)
inss = float((8*salariobt)/100)
sindicato = float((5*salariobt)/100)
impostorenda = float((11*salariobt)/100)
salariolq = float(salariobt-inss-sindicato-impostorenda)

print(f'+ Salário Bruto: R${salariobt} \n'
      f'- IR (11%): R${impostorenda} \n'
      f'- INSS (8%): R${inss} \n'
      f'- Sindicato (5%): R${sindicato} \n'
      f'= Salário Liquido:  R${salariolq} \n')