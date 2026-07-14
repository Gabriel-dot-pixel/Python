# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e a raiz quadrada
print('====== DESAFIO 006 ======')
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n * (1/2)
print('O dobro de {} é {}, o triplo é {} e sua raiz quadrada é {:.2f}'.format(n, d, t, r))
