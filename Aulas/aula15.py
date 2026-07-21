# Estrutura while com looping infinito
cont = 1
while True:
    print(cont, '-> ', end='')
    cont += 1
print('Fim')
# Estrutura while com looping e interrupção
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
