# Crie um programa que leia varios números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao se ele quer ou não continuar a digitar valores
print(f'{" DESAFIO 065 ":=^25}')
n = 1
s = 0
quant = 0
r = 'S'
while r != 'N':
    n = int(input('Digite um número: '))
    if quant == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    s += n
    quant += 1
    r = str(input('Você quer digitar mais números (S/N)? ')).strip().upper()
    while r != 'S' and r != 'N':
        r = str(input('\033[31mRESPOSTA INVÁLIDA!\033[m Digite novamente: ')).strip().upper()
media = s / quant
print(f'A média entre todos os valores digitados é {media:.2f}')
print(f'O maior valor digitado foi {maior} e o menor valor foi {menor}')
