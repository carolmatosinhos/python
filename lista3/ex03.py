nascimento = int(input('Informe o ano do seu nascimento: '))
verificar = 2022-nascimento

if verificar <= 9:
    print('Você está na categoria mirim')
elif verificar <= 14:
    print('Você está na categoria infantil')
elif verificar <= 19:
    print('Você está na categoria junior')
elif verificar <= 30:
    print('Você está na categoria sênior')
else:
    print('Você está na categoria master')