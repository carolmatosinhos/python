frase1 = input("Digite a primeira string:")
frase2 = input("Digite a segunda string:")
print(f'O tamanho da frase "{frase1}" é: {len(frase1)} caracteres')
print(f'O tamanho da frase "{frase2}" é: {len(frase2)} caracteres')

if frase1 > frase2:
    print('As duas strings são de tamanhos diferentes')
    print('As duas strings possuem conteudos diferentes')
elif frase1 == frase2:
    print('As duas strings são de tamanhos iguais')
    print('As duas strings possuem conteudos iguais')
else:
    print('As duas strings são de tamanhos iguais')
    print('As duas strings possuem conteudos diferentes')