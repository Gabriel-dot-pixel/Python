# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
print(f'{" DESAFIO 052 ":=^25}')
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
invertido = ''
for i in range(len(junto) - 1, -1, -1):
    invertido += junto[i]
# É possivel usar tambem invertido = junto[::-1], pois usa uma técnica de "fatiamento" de strings que pega a string inteira e "pula" ela de -1 em -1, invertendo de trás pra frente sem uso do for
if invertido == junto:
    print(f'{junto} de trás para frente é {invertido}')
    print(f'Portanto, {junto} é um PALINDROMO')
else:
    print(f'{junto} de trás para frente é {invertido}')
    print(f'Portanto, {junto} NÃO É um PALINDROMO')
