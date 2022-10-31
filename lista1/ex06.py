real = float(input('\033[0;35mDigite o valor em R$: \033[m'))
conversor = (real/5.32)
print(f'\033[0;35mR${real} em dólar é US${conversor:,.2f}\033[m\n')