# Faça um programa que calcule a soma entre todos os números que são ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500
print(f'{" DESAFIO 048 ":=^25}')
s = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
print(f'Somatório entre todos os números ímpares múltiplos de 3 entre 1 e 500: {s}')
