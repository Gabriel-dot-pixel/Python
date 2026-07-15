'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
1 - para binário
2 - para octal 
3  -para hexadecimal
'''
print('====== DESAFIO 037 ======')
n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
opc = int(input('Sua opção: '))
if opc == 1:
    print(f'{n} convertido para base binária vale {bin(n)[2:]}')
elif opc == 2:
    print(f'{n} convertido para base octal vale {oct(n)[2:]}')
elif opc == 3:
    print(f'{n} convertido para base hexadecimal vale {hex(n)[2:]}')
else:
    print('Opção inválida!')
