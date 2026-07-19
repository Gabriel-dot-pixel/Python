# Melhore o DESAFIO 062, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mosrtrar 0 termos
print(f'{" DESAFIO 062 ":=^25}')
i = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
d = i + (10-1) * r
while i < d + r:
    print(i)
    i += r
