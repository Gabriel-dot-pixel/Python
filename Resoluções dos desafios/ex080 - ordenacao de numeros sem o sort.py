'''
Crie um programa onde o usúario possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort).
No final, mostre a lista ordenada na tela.
'''
print(f'{" DESAFIO 080 ":=^25}')
valores = []
for i in range(0, 5):
    n = int(input(f'Digite o {i+1}º número: '))
    if n == i:
        valores.insert(i, n)
    else:
        valores.insert(-i, n)
print(f'Os valores digitados foram {valores}')
