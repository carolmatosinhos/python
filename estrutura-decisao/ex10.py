turno = input('Em que turno você estuda? \n'
              '[M] Manhã \n'
              '[T] Tarde \n'
              '[N] Noite \n').upper()
if turno == 'M':
    print('Bom dia!')
elif turno == 'T':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite')
else:
    print('Opção inválida')
