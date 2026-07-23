'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números e indique o menor e o maior valor que estão na tupla
'''
from random import randint
print(f'{" DESAFIO 074 ":=^25}')
numeros = ()
# É possivel tambem fazer numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
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
    numeros += (sorteado,)
print(f'Os valores sorteados foram: {numeros}')
# No Python existe um método max(n) que retorna o maior valor dentro de uma tupla, pode ser usado em outras estruturas como listas e dicionarios
print(f'O maior valor sorteado foi: {maior}')
# No Python existe um método min(n) que retorna o menor valor dentro de uma tupla, pode ser usado em outras estruturas como listas e dicionarios
print(f'O menor valor sorteado foi: {menor}')
