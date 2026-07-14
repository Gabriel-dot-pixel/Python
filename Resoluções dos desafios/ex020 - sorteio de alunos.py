# O professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle
print('====== DESAFIO 020 ======')
nome1 = input('Digite o nome do aluno 1: ')
nome2 = input('Digite o nome do aluno 2: ')
nome3 = input('Digite o nome do aluno 3: ')
nome4 = input('Digite o nome do aluno 4: ')
list = [nome1, nome2, nome3, nome4]
shuffle(list)
print('A ordem de alunos(as) que irão apresentar os trabalhos é:')
print(list)
