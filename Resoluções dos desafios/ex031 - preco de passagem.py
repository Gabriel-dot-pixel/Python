'''
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas
'''
print('====== DESAFIO 031 ======')
distancia = float(input('Quantos km você vai viajar? '))
if distancia <= 200.0:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
print(f'A sua passagem vai custar R$ {passagem:.2f}')