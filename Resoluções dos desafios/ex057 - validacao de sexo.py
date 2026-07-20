# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" e "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.
print(f'{" DESAFIO 057 ":=^25}')
sexo = str(input('Digite o seu sexo (M/F): ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('\033[31mVALOR INVÁLIDO!\033[m Digite novamente: ')).strip().upper()[0]
if sexo == 'M':
    print('Você pertencence ao sexo masculino')
elif sexo == 'F':
    print('Você pertence ao sexo feminino')
