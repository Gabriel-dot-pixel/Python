# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
print('====== DESAFIO 012 ======')
p = float(input('Digite o preço do produto: R$ '))
d = p - (p * 0.05)
print('O novo preço do produto, com 5% de desconto, é R$ {:.2f}'.format(d))
