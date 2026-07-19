# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci
print(f'{" DESAFIO 062 ":=^25}')
n = int(input('Digite quantos elementos da Sequência de Fibonacci você quer ver: '))
prim = 0
sec = 1
cont = 0
while cont < n:
    if cont == 0:
        print(prim)
    if cont == 1:
        print(sec)
    prox = prim + sec
    prim = sec
    sec = prox
    print(prox)
    cont += 1
