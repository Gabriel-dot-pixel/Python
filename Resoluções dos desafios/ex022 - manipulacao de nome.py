'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo (sem contar espaços)
- Quantas letras tem o primeiro nome
'''
print('===== DESAFIO 022 ======')
nome = str(input('Digite o seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
sem_espaco = len(nome) - nome.count(' ')
print(f'Seu nome tem {sem_espaco} letras')
separado = nome.split()
prim_nome = len(separado[0])
print(f'Seu primeiro nome tem {prim_nome} letras')
