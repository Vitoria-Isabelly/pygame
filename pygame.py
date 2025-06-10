import pygame 
from pygame import * 

pygame.init()
largura = 800
altua = 600
tela = pygame.display.set_mode((largura,altua))
pygame.display.set_caption('exemplo com pygame')
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((255,255,255))

    pygame.display.update()

pygame.quit()
