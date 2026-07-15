'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
– Se ele ainda vai se alistar ao serviço militar.
– Se é a hora de se alistar.
– Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
print('====== DESAFIO 039 ======')
nasc = int(input('Digite o ano em que você nasceu: '))
hoje = date.today().year
idade = hoje - nasc
if idade < 18:
    print('Você ainda vai se alistar')
    print(f'Falta(am) {18-idade} ano(s) para você se alistar')
elif idade == 18:
    print('Ja é hora de se alistar')
else:
    print('Ja passou da hora de você se alistar')
    print(f'Passou {idade-18} ano(s) do alistamento')
