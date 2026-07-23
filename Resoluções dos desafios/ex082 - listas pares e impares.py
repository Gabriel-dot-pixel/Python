# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o contéudo das três listas geradas.
numeros = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('\033[31mVALOR INVÁLIDO!\033[m Digite novamente: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Os números digitados foram: {numeros}')
if pares:
    print(f'Os números pares da lista são: {pares}')
else:
    print('Nenhum número par foi digitado')
if impares:
    print(f'Os números ímpares da lista são: {impares}')
else:
    print('Nenhum número ímpar foi digitado')
