# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
print('====== DESAFIO 025 ======')
nome = str(input('Digite o seu nome? ')).upper().strip()
verificado = 'SILVA' in nome
print(f'Você tem "SILVA" no nome? {verificado}')
