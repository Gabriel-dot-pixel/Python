# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
print(f"{' DESAFIO 047 ':=^25}")
print('Todos os pares entre 1 e 50: ')
for i in range(2, 51, 2): # Um laço dessa forma consome menos processamento do que um laço 1 por 1 com condição
        print(i, end=' ')
