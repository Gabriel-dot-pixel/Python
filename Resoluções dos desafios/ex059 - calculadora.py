'''
Crie um programa que leia dois valores e mostre um menu na tela:
1 - Somar
2 - Multiplicar
3 - Maior
4 - Novos números
5 - Sair do programa
Seu programa devera realizar a operação solicitada em cada caso
'''
print(f'{" DESAFIO 059 ":=^25}')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
opc = 0
while opc != 5:
    print('Aqui estão as operações que você pode fazer:')
    print('1 - Somar os dois números')
    print('2 - Multiplicar os dois números')
    print('3 - Saber qual deles é o maior')
    print('4 - Digitar novos números')
    print('5 - Sair do programa')
    opc = int(input('Digite qual das operações você quer realizar: '))
    if opc == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}\n')
    if opc == 2:
        multiplicacao = n1 * n2
        print(f'{n1} x {n2} = {multiplicacao}\n')
    if opc == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}\n')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}\n')
        else:
            print('Os dois números são iguais\n')
    if opc == 4:
        n1 = float(input('Novo valor do primeiro número: '))
        n2 = float(input('Novo valor do segundo número: '))
        print('\n')
    if opc == 5:
        print('Saindo...\n')
