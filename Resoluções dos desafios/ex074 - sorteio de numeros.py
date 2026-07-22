'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números e indique o menor e o maior valor que estão na tupla
'''
from random import randint
print(f'{" DESAFIO 074 ":=^25}')
tupla = ()
for i in range(0, 5):
    sorteado = randint(0, 10)
    if i == 0:
        menor = sorteado
        maior = sorteado
    else:
        if sorteado < menor:
            menor = sorteado
        elif sorteado > maior:
            maior = sorteado
    tupla += (sorteado,)
print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')
