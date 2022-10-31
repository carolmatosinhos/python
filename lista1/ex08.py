preco = float(input(f'\033[0;31mDigite o valor do produto: \033[m'))
porcentagem = (5/100)*preco
desc = preco-porcentagem
print(f'\033[0;31mO novo preço do produto com 5% de desconto é R${desc}\033[m')