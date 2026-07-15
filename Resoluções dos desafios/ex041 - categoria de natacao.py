'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JUNIOR
– Até 20 anos: SÊNIOR
– Acima: MASTER
'''
from datetime import date
print('====== DESAFIO 041 ======')
ano = int(input('Digite o seu ano de nascimento: '))
hoje = date.today().year
idade = hoje - ano
if idade <= 9:
    print(f'Você tem {idade} anos e está na classificação MIRIM de natação')
elif idade <= 14:
    print(f'Você tem {idade} anos e está na classificação INFANTIL de natação')
elif idade <= 19:
    print(f'Você tem {idade} anos e está na classificação JÚNIOR de natação')
elif idade <= 20:
    print(f'Você tem {idade} anos e está na classificação SÊNIOR de natação')
else:
    print(f'Você tem {idade} anos e está na classificação MASTER de natação')
