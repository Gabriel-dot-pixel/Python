# Crie um programa onde o usúario possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número ja exista la dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente
print(f'{" DESAFIO 079 ":=^25}')
valores = []
while True:
    n = int(input('Digite um valor: '))
    if n in valores:
        print('Valores duplicados não serão adicionados...')
    else:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    r = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('\033[31mVALOR INVÁLIDO!\033[m Digite novamente: ')).strip().upper()[0]
    if r == 'N':
        print('Saindo...')
        break
print(f'Os valores digitados foram {valores}')
valores.sort()
print(f'Os valores em ordem crescente ficam {valores}')
