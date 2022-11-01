import random
jogador = int(input('Vamos jogar jokenpô! Escolha uma opção: \n'
                '[0] Pedra \n'
                '[1] Papel \n'
                '[2] Tesoura '))

game = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)


print(f'Computador jogou: {game[computador]}')


if computador == 0:
    if jogador == 0:
        print('Empate')

    elif jogador == 1:
        print('Jogador venceu!')

    elif jogador == 2:
        print('Computador venceu!')

    else:
        print('Jogada inválida')

elif computador == 1:
    if jogador == 0:
        print('Computador venceu')

    elif jogador == 1:
        print('Empate')

    elif jogador == 2:
        print('Jogador venceu!')

    else:
        print('Jogada inválida')

elif computador == 2:
    if jogador == 0:
        print('Jogador venceu')

    elif jogador == 1:
        print('Computador venceu')

    elif jogador == 2:
        print('Empate')

    else:
        print('Jogada inválida')