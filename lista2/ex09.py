valor = int(input('Digite o valor do produto: '))
pagamento = int(input(f'Digite a forma de pagamento: \n'
                      '1 - Dinheiro/Cheque \n'
                      '2 - A vista cartão \n'
                      '3 - 2x no cartão \n'
                      '4 - 3x ou mais no cartão \n'))

dinheiro = (valor*10)/100
cartaoav = (valor*5)/100
cartaoap = (valor*20)/100
cartao = valor

if pagamento == 1:
    print(f'Você recebeu 10% de desconto. O total a pagar é: {valor-dinheiro}')
elif pagamento == 2:
    print(f'Você recebeu 5% de desconto. O total a pagar é:{valor-cartaoav}')
elif pagamento == 4:
    print(f'O pagamento no cartão a prazo é cobrado os juros. O total a pagar é:{valor+cartaoap}')
else:
    print(f'O total a pagar é:{cartao}')
