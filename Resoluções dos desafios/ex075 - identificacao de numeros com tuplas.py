'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares
'''
print(f'{" DESAFIO 075 ":=^25}')
numeros = ()
pares = ()
cont9 = 0
for i in range(0, 4):
    n = int(input(f'Digite o {i+1}º número: '))
    if n == 9:
        cont9 += 1
    if n % 2 == 0:
        pares += (n,)
    numeros += (n,)
print(f'Os números digitados foram: {numeros}')
if cont9 > 0:
    print(f'O número 9 apareceu {cont9} vezes')
else:
    print('O número 9 não apareceu nenhuma vez')
if 3 in numeros:
    print(f'O número 3 apareceu pela primeira vez na {numeros.index(3)+1}º posição')
else:
    print('O número 3 não apareceu em nenhuma posição')
if pares:
    print(f'Os números pares digitados foram: {pares}')
else:
    print('Nenhum número par foi digitado')
