# Crie um programa onde o usúario possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente
valores = [[], []]
for i in range(0, 7):
    n = int(input(f'Digite o {i+1}º número: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
print(f'Os valores digitados foram: {valores}')
valores[0].sort()
valores[1].sort()
if valores[0]:
    print(f'Os valores pares digitados foram: {valores[0]}')
else:
    print('Nenhum valor par foi digitado')
if valores[1]:
    print(f'Os valores ímpares digitados foram: {valores[1]}')
else:
    print('Nenhum valor ímpar foi digitado')
