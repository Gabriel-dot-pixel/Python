# Refazer o DESAFIO 064 só que usando o break
print(f'{" DESAFIO 066 ":=^25}')
n = 0
cont = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Foram digitados {cont} números e a soma entre eles vale {s}')
