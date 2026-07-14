# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considerando U$ 1 = R$ 3,27
print('====== DESAFIO 010 ======')
r = float(input('Quantos reais você tem? R$ '))
d = r / 3.27
print('Você pode comprar U$ {:.2f}'.format(d))
