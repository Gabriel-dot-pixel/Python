'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usúario quer ou não continuar. No final mostre:
A) Quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos
'''
print(f'{" DESAFIO 069 ":=^25}')
quant = 1
quant18 = 0
quanthomem = 0
mulher20 = 0
while True:
    print(f'---- {quant}ª Pessoa ----')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: (M/F) ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('\033[31mVALOR INVÁLIDO!\033[m Digite novamente: ')).strip().upper()[0]
    if idade > 18:
        quant18 += 1
    if sexo == 'M':
        quanthomem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    quant += 1
    r = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    if r == 'N':
        break
    while r not in 'SN':
        r = str(input('\033[31mVALOR INVÁLIDO! Digite novamente: ')).strip().upper()[0]
print(f'{quant18} pessoas com mais de 18 anos foram cadastradas')
print(f'{quanthomem} homens foram cadastrados')
print(f'{mulher20} mulheres com menos de 20 anos foram cadastradas')
