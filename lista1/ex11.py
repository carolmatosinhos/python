km = int(input('\033[0;33mInforme a quantidade de km percorridos:\033[m'))
dias = int(input('\033[0;33mInforme a quantidade de dias que o carro foi alugado:\033[m'))

carrodia = 60
kmdia = 0.15
pagar = (km*kmdia)+(dias*carrodia)
print(f'\033[0;33mTotal a pagar: R${pagar}\033[m')