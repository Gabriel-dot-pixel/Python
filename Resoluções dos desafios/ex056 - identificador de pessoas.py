'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos
'''
print(f'{" DESAFIO 056 ":=^25}')
si = 0
idadehomen = 0
nomehomem = ''
mulher20 = 0
for i in range(1, 5):
    print(f'----- {i}ª Pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (m - masculino; f - feminino): ')).strip()
    si += idade
    if i == 1 and sexo in 'Mm':
        idadehomen = idade
        nomehomem = nome
    if sexo in 'Mm' and idade > idadehomen:
        idadehomen = idade
        nomehomem = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
media = si / 4
print(f'A média de idade do grupo é, aproximadamente, {media:.0f} anos')
print(f'O homem mais velho se chama {nomehomem} e tem {idadehomen} anos')
print(f'{mulher20} mulheres tem menos de 20 anos')
