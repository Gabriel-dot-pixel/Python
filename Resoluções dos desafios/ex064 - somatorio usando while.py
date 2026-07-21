# Crie um programa que leia varios números inteiros pelo teclado. O programa só para quando o usúario digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. (desconsiderando o flag)
print(f'{" DESAFIO 064 ":=^25}')
n = 0
cont = 0
s = 0
while n != 999:
    n = int(input('Digite um número (digite 999 para parar o programa): '))
    if n != 999:
        s += n
        cont += 1
print(f'Foram digitados {cont} números e a soma entre eles é {s}')
