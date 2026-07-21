# Melhore o DESAFIO 062, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mosrtrar 0 termos
print(f'{" DESAFIO 062 ":=^25}')
i = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
t = i
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(t, end=' -> ')
        t += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer ver? '))
print(f'Foram mostrados {total} termos da progressão')
