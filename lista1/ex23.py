nome = input('\033[0;36mDigite seu nome completo:\033[m')
lista = nome.split()
print(f'Seu primeiro nome é {lista[0]}')
print(f'Seu último nome é {lista[-1]}')