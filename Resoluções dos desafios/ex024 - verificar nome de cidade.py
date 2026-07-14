# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
print('====== DESAFIO 024 ======')
cidade = str(input('Digite o nome de uma cidade: ')).upper().strip()
separado = cidade.split()
prim = separado[0]
verificado = prim == 'SANTO'
print(f'O nome dessa cidade começa com "SANTO"? {verificado}')
