'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos
'''
print(f'{" DESAFIO 056 ":=^25}')
nome = str(input('Nome da pessoa 1: ')).strip()
idade = int(input('Idade da pessoa 1: '))
sexo = str(input('Sexo da pessoa 1 (m - masculino; f - feminino): ')).strip()
si = idade
if sexo == 'm':
    maior = idade
    mnome = nome
for i in range(2, 5):
    nome = str(input(f'Nome da pessoa {i}: ')).strip()
    idade = int(input(f'Idade da pessoa {i}: '))
    sexo = str(input(f'Sexo da pessoa {i} (m - masculino; f - feminino): ')).strip()
    if sexo == 'm' and idade > maior:
        maior = idade
        mnome = nome
#   si += idade
# media = si / 4
# print(f'A média de idade do grupo é, aproximadamente, {media:.0f} anos')
print(f'O homem mais velho se chama {mnome} e tem {maior} anos')
