peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso/(altura*altura)

if imc <= 18.5:
    print('Você está abaixo do peso')
elif imc <=25:
    print('Você está com o peso ideal')
elif imc <= 30:
    print('Você está com sobrepeso')
elif imc <= 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')