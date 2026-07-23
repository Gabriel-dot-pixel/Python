'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados de forma tabular
'''
print(f'{" DESAFIO 076 ":=^25}')
compras = ()
while True:
    produto = str(input('Digite o nome do produto: ')).strip().capitalize()
    preco = float(input('Digite o preço do produto: R$'))
    compras += (produto, preco)
    r = str(input('Mais alguma coisa? (S/N) ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('\033[31mVALOR INVÁLIDO!\033[m Digite novamente: ')).strip().upper()[0]
    if r == 'N':
        break
print('-' * 40)
print(f"{'LISTAGEM DE COMPRAS':^40}")
for i in range(0, len(compras), 2):
    produto = compras[i]
    preco = compras[i+1]
    print(f'{produto:.<30}R$ {preco:>.2f}')
print('-' * 40)
