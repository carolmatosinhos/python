km = float(input('Qual a distância da viagem em km? '))
curta = 0.50*km
longa = 0.45*km

if km <= 200:
    print(f'A passagem custará R${curta}')
else: 
    print(f'A passagem custará R${longa}')