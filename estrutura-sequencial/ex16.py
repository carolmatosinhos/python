tamanhoprd = float(input('Digite o tamanho em m² da área a ser pintada: '))
cobertura = tamanhoprd/3 
lata = cobertura/18 
preco = lata*80

print(f'Quantidade de latas necessárias: {lata} \n'
      f'Preço total a ser pago: {preco}')