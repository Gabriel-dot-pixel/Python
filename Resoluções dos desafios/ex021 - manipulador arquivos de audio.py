# Faça um programa em python que abra e reproduza o aúdio de um arquivo .mp3
import pygame
print('====== DESAFIO 021 ======')
pygame.init()
# Colocado o caminho de onde o arquivo estava para não dar erro devido a limitações do pygame-ce
pygame.mixer.music.load('Resoluções dos desafios/ex021.mp3')
pygame.mixer.music.play()
# input usado para manter o programa rodando enquanto a música toca, senão o programa fecha tão rápido que não da tempo da música começar
input('Aperte ENTER para parar a música....')
