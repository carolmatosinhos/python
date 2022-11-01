nascimento = int(input('Informe seu ano de nascimento: '))
verificar = 2022-nascimento

if verificar <= 17:
    print('Você ainda vai se alistar no serviço militar')
    print(f'Ainda faltam {18 - verificar} para você se alistar')
elif verificar == 18:
    print('Está na hora de você se alistar no serviço militar')
else:
    print('Você já deveria estar alistado')
    print(f'Você está {verificar-18} anos atrasado')