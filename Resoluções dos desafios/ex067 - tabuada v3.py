# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o valor solicitado for negativo
print(f'{" DESAFIO 067 ":=^25}')
n = 1
while n >= 0:
    n = int(input('Qual número você quer saber a tabuada (digite um número negativo para parar): '))
    print('-' * 20)
    cont = 0
    if n < 0:
        print('Desligando...')
        break
    while cont <= 10:
        print(f'{n} x {cont:2} = {n*cont}')
        cont += 1
    print('-' * 20)
