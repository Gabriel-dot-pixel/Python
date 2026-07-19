# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" e "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.
print(f'{" DESAFIO 057 ":=^25}')
sexo = str(input('Digite o seu sexo (M/F): ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(('Valor inválido! Digite novamente: ')).strip().upper()
if sexo == 'M':
    print('Você pertencence ao sexo masculino')
elif sexo == 'F':
    print('Você pertence ao sexo feminino')
