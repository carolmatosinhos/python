import random
aluno1 = input('\033[0;34mInforme o nome do primeiro aluno:\033[m')
aluno2 = input('\033[0;34mInforme o nome do segundo aluno:\033[m')
aluno3 = input('\033[0;34mInforme o nome do terceiro aluno:\033[m')
aluno4 = input('\033[0;34mInforme o nome do quarto aluno:\033[m')

pessoas = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(pessoas)

print(f'\033[0;37;40mO aluno sorteado foi {sorteio}\033[m')