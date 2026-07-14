# Desenvolva um programa que leia o comprimento de três retas e diga ao usúario se elas podem ou não formar um triângulo
print('====== DESAFIO 035 ======')
a = float(input('Digite o comprimento da reta a: '))
b = float(input('Digite o comprimento da reta b: '))
c = float(input('Digite o comprimento da reta c: '))
if a + b > c and a + c > b and b + c > a:
    print('As retas podem formar um triângulo')
else:
    print('As retas não podem formar um triângulo')
