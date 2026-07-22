lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])
print(lanche[:2])
print(lanche[-2])
print(lanche[-2:])
# Tuplas são imútaveis
# lanche[2] = 'Refrigerante' -> NÃO PODE
# Dessa forma você não consegue imprimir os indices de cada elemento, mas consegue imprimir todos os elementos sem precisar definir um indice
for c in lanche:
    print(c, end=' ')
print('\n')
# Dessa forma você consegue imprimir os indices de cada elemento, mas vai ter que definir um range de até onde vai o laço
for i in range(0, len(lanche)):
    print(f'{lanche[i]}, posição {i}')
print('\n')
# Dessa forma você consegue imprimir os indices de cada elemento junto com os elementos
for pos, c in enumerate(lanche):
    print(f'{lanche}, posição {pos}')
# sorted() coloca a tupla em ordem, mas não altera a tupla
print(sorted(lanche))
# Você pode somar duas tuplas para formar uma tupla composta
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))
# O index() mostra o indice do elemento, na primeira ocorrência, que você quer achar na tupla
print(c.index(8))
# Dessa forma você mostra o indicie do elemento, na primeira ocorrência, a partir de uma determinada posição
print(c.index(2, 4))
# Tuplas aceitam dados de diversos tipos
pessoa = ('Gabriel', 20, 'M', 100.5)
# É possivel apagar uma tupla inteira da memória do computador
del(pessoa)
print(pessoa)
