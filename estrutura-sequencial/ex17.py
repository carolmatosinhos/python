import math

tamanhoprd = float(input('Digite o tamanho em m² da área a ser pintada: '))
cobertura = tamanhoprd/6 
lata = cobertura/18
galao = cobertura/3.6
precolt = lata*80
precogl = galao*25


print(f'Quantidade de tinta necessárias: {cobertura:,.2f}L \n')
print(f'Você precisa de {lata} latas e o preço será {precolt}')
print(f'Você precisa de {galao} galão(es) e o preço será {precogl}')
