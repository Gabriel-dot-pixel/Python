# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci
print(f'{" DESAFIO 062 ":=^25}')
n = int(input('Digite quantos elementos da Sequência de Fibonacci você quer ver: '))
prim = 0
sec = 1
cont = 0
print(prim, end=' -> ')
print(sec, end=' -> ')
while cont < n:
    prox = prim + sec
    prim = sec
    sec = prox
    print(prox, end=' -> ')
    cont += 1
print('FIM')
