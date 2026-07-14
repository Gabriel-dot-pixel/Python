'''
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "a"
- Em que posição ela aparece pela primeira vez
- Em que posição ela aparece pela ultima vez
'''
print('====== DESAFIO 026 ======')
frase = str(input('Digite uma frase qualquer: ')).upper().strip()
contador = frase.count('A')
print(f'A letra "A" aparece {contador} vezes na frase')
primeiro = frase.find('A') + 1
print(f'A letra "A" aparece pela primeira vez na posição {primeiro}')
ultimo = frase.rfind('A') + 1
print(f'A letra "A" aparece pela ultima vez na posição {ultimo}')
