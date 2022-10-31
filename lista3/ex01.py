import random
opcao = input('Vamos jogar jokenpô! Escolha uma opção: \n'
          'PEDRA \n'
          'PAPEL \n'
          'TESOURA \n').upper()

lista =['PEDRA', 'PAPEL', 'TESOURA']

print(random.choice(lista))

if opcao == lista:
    print('Você venceu!')
else:
    print('Você perdeu!')