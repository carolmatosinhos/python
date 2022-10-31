salario = float(input('Qual é o seu salário? '))
if salario > 1250.00:
    print(f'Seu novo salário é {(salario*10)/100+salario}')
else:
    print(f'Seu novo salário é {(salario*15)/100+salario}')