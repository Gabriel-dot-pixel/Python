# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o valor solicitado for negativo
print(f'{" DESAFIO 067 ":=^25}')
n = 1
while True:
    n = int(input('Qual número você quer saber a tabuada (digite um número negativo para parar): '))
    print('-' * 20)
    if n < 0:
        print('Desligando...')
        break
    for i in range(1, 11):
        print(f'{n} x {i:2} = {n*i}')
    print('-' * 20)
