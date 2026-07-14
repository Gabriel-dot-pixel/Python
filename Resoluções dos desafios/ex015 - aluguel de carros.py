# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o custa R$ 60 por dia e R$ 0,15 por km rodado
print('====== DESAFIO 015 ======')
dia = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos km você andou com o carro? '))
preco = (dia * 60) + (km * 0.15)
print('O valor total do aluguel será de R$ {:.2f}'.format(preco))
