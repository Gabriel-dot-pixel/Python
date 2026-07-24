# Crie um programa onde o usúario digite uma expressão qualquer que use parênteses. Sua aplicação deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta
print(f'{" DESAFIO 083 ":=^25}')
exp = str(input('Digite a expressão: ')).strip()
pilha = []
for simb in exp:
    # Se o usúario digitar "(" o programa vai adicioná-lo na pilha
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        # Se o usúario digitar ")" e o tamanho da pilha for maior que 0 ele vai remover o último elemento da pilha, se o tamanho da pilha for maior que zero ele adiciona mais um ")" no final da pilha e quebra a estrutura
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
# No final, se o tamanho da pilha for igual a 0 a expressão é válida, ou seja, o número de "(" é o mesmo número de ")"
if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')
