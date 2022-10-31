casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Em quantos anos você deseja pagar a casa? '))
mes = anos * 12
negado = (salario*30)/100
prestacao = casa/mes
print(f'O valor a pagar por mês é {prestacao:.2f}')

if prestacao >= negado:
    print('Empréstimo negado')
else:
    print('Empréstimo aceito')