'''
Crie um programa que leia dois valores e mostre um menu na tela:
1 - Somar
2 - Multiplicar
3 - Maior
4 - Novos números
5 - Sair do programa
Seu programa devera realizar a operação solicitada em cada caso
'''
from time import sleep
print(f'{" DESAFIO 059 ":=^25}')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
lFlag = False
while not lFlag:
    print('Aqui estão as operações que você pode fazer:')
    print('1 - Somar os dois números')
    print('2 - Multiplicar os dois números')
    print('3 - Saber qual deles é o maior')
    print('4 - Digitar novos números')
    print('5 - Sair do programa')
    opc = int(input('Digite qual das operações você quer realizar: '))
    if opc < 1 or opc > 5:
        while opc < 1 or opc > 5:
            opc = int(input('\033[31mOPÇÃO INVÁLIDA!\033[m Digite novamente: '))
    if opc == 1:
        soma = n1 + n2
        print('Calculando...')
        sleep(2)
        print(f'{n1} + {n2} = {soma}')
    elif opc == 2:
        multiplicacao = n1 * n2
        print('Calculando...')
        sleep(2)
        print(f'{n1} x {n2} = {multiplicacao}')
    elif opc == 3:
        print('Avaliando...')
        sleep(2)
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else:
            print('Os dois números são iguais')
    elif opc == 4:
        n1 = float(input('Novo valor do primeiro número: '))
        n2 = float(input('Novo valor do segundo número: '))
        print('Inserindo valores...')
        sleep(2)
    elif opc == 5:
        print('Desligando...')
        sleep(2)
        lFlag = True
    print('=-=' * 10)
