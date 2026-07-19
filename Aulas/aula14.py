# Laço while padrão
i = 1
while i < 10:
    print(i)
    i += 1
print('Fim')
# Laço while com entrada de dados
n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('Fim')
# Laço while com entrada de dados e de variavel de parada
r = 'S'
while r == 'S':
    v = float(input('Digite o valor do produto: R$'))
    r = str(input('Mais alguma coisa (S/N)? ')).upper()
# Laço while com condição
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Foram digitados {par} valores pares e {impar} valores ímpares')
