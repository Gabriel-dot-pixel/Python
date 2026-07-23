# Listas são identificas com []
# Listas são mutaveis
lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)
# Para adicionar novos elementos na lista usa-se o método append()
lanche.append('Cookie')
print(lanche)
# Pode-se usar tambem o insert() para adicionar novos elementos na lista na posição que você quer
lanche.insert(0, 'Cachorro-Quente')
print(lanche)
# Para eliminar elementos de posições especificas usa-se o del()
del(lanche[3])
print(lanche)
# Pode usar tambem o pop() que elimina o elemento de uma determinada posição passando somente o índice dele, se não passar valor nenhum no    pop() ele vai eliminar o último elemento da lista
# lanche.pop(3)
# Tambem pode usar o remove() que você passa o valor do elemento que você quer eliminar, o remove só elimina a primeira ocorrência do elemento
# lanche.remove('Pizza')
# É possivel tambem criar listas usando range()
valores = list(range(4, 11))
print(valores)
# Se você tiver uma lista desorganizada e quiser organiza-lá, você pode usar o método sort()
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)
valores.sort()
print(valores)
# Se você quiser a ordem reversa dos valores usando sort, basta usar sort(reverse=True)
valores.sort(reverse=True)
print(valores)