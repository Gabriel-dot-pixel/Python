# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
print(f'{" DESAFIO 052 ":=^25}')
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
invertido = ''
for i in range(0, len(junto)):
    invertido += junto[(len(junto)-1)-i]
if invertido == junto:
    print(f'A frase "{frase}" é um Palindromo')
else:
    print(f'A frase "{frase}" não é um Palindromo')
