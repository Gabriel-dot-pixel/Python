'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
A) Quantos números foram digitados
B) A lista de valores ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista
'''
print(f'{" DESAFIO 081 ":=^25}')
numeros = []
cont = 0
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    cont += 1
    r = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('\033[31mVALOR INVÁLIDO!\033[m Digite novamente: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'{cont} números foram digitados')
numeros.sort(reverse=True)
print(f'A lista ordenada de forma decrescente fica: {numeros}')
if 5 in numeros:
    print('O número 5 esta na lista')
else:
    print('O número 5 não esta na lista')
