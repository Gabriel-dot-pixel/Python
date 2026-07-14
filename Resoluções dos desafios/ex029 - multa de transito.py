'''
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada km acima do limite.
'''
print('====== DESAFIO 029 ======')
velocidade = float(input('A quantos km/h você passou no radar? '))
if velocidade > 80.0:
    multa = (velocidade - 80.0) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print(f'A sua multa será no valor de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')
