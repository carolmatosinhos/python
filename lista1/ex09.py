salario = float(input(f'\033[0;32mInforme o salário: \033[m'))
porcentagem = (15/100)*salario
aumento = porcentagem + salario
print(f'\033[0;32mO valor do novo salário é R${aumento}\033[m')