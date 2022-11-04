nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

if media < 4:
    print(f'Suas notas foram {nota1} e {nota2} \n'
          f'Sua média foi {media} \n'
          f'Seu conceito foi E \n'
          f'Você está REPROVADO \n')

elif media < 6:
    print(f'Suas notas foram {nota1} e {nota2} \n'
          f'Sua média foi {media} \n'
          f'Seu conceito foi D \n'
          f'Você está REPROVADO \n')

elif media < 7.5:
    print(f'Suas notas foram {nota1} e {nota2} \n'
          f'Sua média foi {media} \n'
          f'Seu conceito foi C \n'
          f'Você está APROVADO \n')

elif media < 9:
    print(f'Suas notas foram {nota1} e {nota2} \n'
          f'Sua média foi {media} \n'
          f'Seu conceito foi B \n'
          f'Você está APROVADO \n')

elif media <= 10:
    print(f'Suas notas foram {nota1} e {nota2} \n'
          f'Sua média foi {media} \n'
          f'Seu conceito foi A \n'
          f'Você está APROVADO \n')
else:
    print('Valores inválidos')