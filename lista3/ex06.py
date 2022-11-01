from sys import float_repr_style


seg1 = float(input('Informe o primeiro segmento de reta: '))
seg2 = float(input('Informe o segundo segmento de reta: '))
seg3 = float(input('Informe o terceiro segmento de reta: '))

verificar =  seg1+seg2

if verificar < seg3:
    print('Os segmentos podem formar um triângulo')
else:
    print('Os segmentos não podem formar um triângulo')