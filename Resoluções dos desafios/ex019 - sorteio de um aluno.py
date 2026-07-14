# Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
from random import choice
print('====== DESAFIO 019 ======')
nome1 = input('Digite o nome do aluno 1: ')
nome2 = input('Digite o nome do aluno 2: ')
nome3 = input('Digite o nome do aluno 3: ')
nome4 = input('Digite o nome do aluno 4: ')
list = [nome1, nome2, nome3, nome4]
sorteado = choice(list)
print(f'O aluno(a) sorteado(a) para apagar o quadro foi o(a) {sorteado}')
