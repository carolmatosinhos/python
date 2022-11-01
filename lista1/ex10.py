temperatura = int(input('\033[0;33mDigite a temperatura em graus Celsius:\033[m'))
conversor = (temperatura * 1.8) + 32

print(f'\033[0;34;40mA temperatura em é fahrenheit {conversor:,.2f}\033[m')