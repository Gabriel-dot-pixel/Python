# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usúario escolher, só que agora utilizando for
print(f'{" DESAFIO 049 ":=^25}')
n = int(input('Digite o número que você quer saber a tabuada: '))
for i in range(0, 11):
    print(f'{n} x {i:2} = {n*i}')
