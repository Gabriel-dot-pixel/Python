# Laço que imprime "oi" seis vezes
for i in range(0, 6):
    print('oi')
print('FIM')
# Laço que imprime numeros de 0 a 5
for i in range(0, 6):
    print(i)
print('FIM')
# Laço que imprime numeros de 1 a 6
for i in range(1, 7):
    print(i)
print('FIM')
# Laço que imprime numeros de 6 a 0 regressivamente
for i in range(6, 0, -1):
    print(i)
print('FIM')
# Laço que imprime numeros de 0 a 6 saltando de 2 em 2
for i in range(0, 6, 2):
    print(i)
print('FIM')
# Laço que imprime números de 0 a um numero digitado pelo usúario + 1
n = int(input('Digite um número: '))
for i in range(0, n+1):
    print(i)
print('FIM')
# Laço com controle total do usúario
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
# Laço pedindo pro usúario digitar valores um determinado número de vezes
for i in range(0, 3):
    n = int(input('Digite um número: '))
print('FIM')
# Exemplo de somatório com laço
s = 0
for i in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'Somatório: {s}')
print('FIM')
