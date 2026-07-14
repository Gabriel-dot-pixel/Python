'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
Ex: Ana Maria de Souza
Primeiro: Ana
Ultimo: Souza
'''
print('====== DESAFIO 027 ======')
nome = input('Digite o seu nome completo: ')
separado = nome.split()
primeiro = separado[0]
tamanho = len(separado)
ultimo = separado[tamanho-1]
print(f'Primeiro nome: {primeiro}')
print(f'Ultimo nome: {ultimo}')