import random
num = int(input('Digite um número de 0 a 5: '))
game = random.randrange(1, 5)

print(game)
if num == game:
    print('você venceu')
else:
    print('você perdeu')