salario = float(input('Informe seu salário atual: '))
if salario <= 280:
    print(f'Seu salário era R${salario}. \n' 
          f'Você recebeu um aumento de 20%. \n' 
          f'O valor do aumento é de R${((20*salario)/100)}. \n' 
          f'Seu novo salário é {((20*salario)/100)+salario}')
elif salario > 280 and salario <= 700:
    print(f'Seu salário era R${salario}. \n' 
          f'Você recebeu um aumento de 15%. \n' 
          f'O valor do aumento é de R${((15*salario)/100)}. \n' 
          f'Seu novo salário é {((15*salario)/100)+salario}')
elif salario > 700 and salario <= 1500:
    print(f'Seu salário era R${salario}. \n' 
          f'Você recebeu um aumento de 10%. \n' 
          f'O valor do aumento é de R${((10*salario)/100)}. \n' 
          f'Seu novo salário é {((10*salario)/100)+salario}')
else:
    print(f'Seu salário era R${salario}. \n' 
          f'Você recebeu um aumento de 5%. \n' 
          f'O valor do aumento é de R${((5*salario)/100)}. \n' 
          f'Seu novo salário é {((5*salario)/100)+salario}')


