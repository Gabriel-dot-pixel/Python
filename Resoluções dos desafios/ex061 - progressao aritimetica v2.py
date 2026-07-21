# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while
print(f'{" DESAFIO 061 ":=^25}')
i = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
t = i
cont = 1 
while cont <= 10:
    print(t, end=' -> ')
    t += r
    cont += 1
print('FIM')
