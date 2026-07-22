'''
Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados
B) Os ultimos 4 colocados
C) Uma lista com os times em ordem alfabética
D) Em que posição da tabela esta o time da Chapecoense
'''
times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Bragantino', 'Athletico-PR', 'Bahia', 'Coritiba', 'São Paulo', 'Botafogo', 'Atlético-MG', 'Vitória', 'Corinthias', 'Cruzeiro', 'Internacional', 'Santos', 'Grêmio', 'Vasco', 'Mirassol', 'Remo', 'Chapecoense')
print('=-' * 90)
print(f'Os times da tabela do brasileirão de 2026 são: {times}')
print('=-' * 90)
print(f'Os 5 primeiros colocados da tabela são: {times[:5]}')
print('=-' * 90)
print(f'Os 4 últimos colocados da tabela são: {times[16:]}')
print('=-' * 90)
print(f'A tabela ordenada por ordem alfabética fica: {sorted(times)}')
print('=-' * 90)
print(f'O time da Chapecoense está, atualmente, na {times.index('Chapecoense')+1}º colocação')
