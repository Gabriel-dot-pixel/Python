'''
Refaca o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– Equilátero: todos os lados iguais
– Isósceles: dois lados iguais
– Escaleno: todos os lados diferentes
'''
print('====== DESAFIO 042 ======')
a = float(input('Digite o comprimento da reta a: '))
b = float(input('Digite o comprimento da reta b: '))
c = float(input('Digite o comprimento da reta c: '))
if a + b > c and a + c > b and b + c > a:
    print('As retas podem formar um triângulo')
    if a == b and a == c:
        print('As retas formarão um triângulo Equilátero')
    elif a == b or a == c:
        print('As retas formarão um triângulo Isósceles')
    else:
        print('As retas formarão um triângulo Escaleno')
else:
    print('As retas não podem formar um triângulo')
    