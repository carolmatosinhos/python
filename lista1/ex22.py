frase = input('\033[0;36mDigite a frase:\033[m').upper()
cont = (frase.count('A'))
pri = frase.find('A')
ult = frase.rfind('A')
print(f'\033[0;36mNa frase há {cont} letras A\033[m')
print(f'\033[0;36mAparece a primeira vez na posição {pri}\033[m')
print(f'\033[0;36mAparece a última vez na posição {ult}\033[m')