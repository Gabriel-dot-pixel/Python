'''
Crie um programa onde o usúario possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort).
No final, mostre a lista ordenada na tela.
'''
print(f'{" DESAFIO 080 ":=^25}')
valores = []
for i in range(0, 5):
    n = int(input(f'Digite o {i+1}º número: '))
    # É o primeiro número ou ele é maior que todos? Coloque no final, como o objetivo é ter uma lista crescente, o ultimo elemento sempre é o maior
    if i == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        # O programa vai varrer a lista a partir da primeira posição
        pos = 0
        while pos < len(valores):
            # O novo número deve ficar antes do número desta posição? Insira aqui
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1
print(f'Os valores digitados foram {valores}')
