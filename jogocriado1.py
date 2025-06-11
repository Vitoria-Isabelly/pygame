# Importa o módulo pygame e a função quit do módulo sys
import pygame
import sys

# Inicializa todos os módulos do pygame
pygame.init()

# Define o tamanho da janela do jogo (largura x altura)
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))

# Define o título da janela
pygame.display.set_caption("Quadrado que se move")

# Define a cor de fundo (preto) e a cor do quadrado (azul)
cor_fundo = (0, 0, 0)  # RGB para preto
cor_quadrado = (0, 0, 255)  # RGB para azul

# Define o tamanho do quadrado
tamanho_quadrado = 50

# Define a posição inicial do quadrado no centro da tela
x = largura // 2 - tamanho_quadrado // 2
y = altura // 2 - tamanho_quadrado // 2

# Velocidade do quadrado
velocidade = 5

# Controla a taxa de atualização da tela (frames por segundo)
clock = pygame.time.Clock()

# Loop principal do jogo (vai continuar rodando até o jogador sair)
while True:
    # Trata os eventos (como pressionar uma tecla ou fechar a janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            # Encerra o pygame e o programa
            pygame.quit()
            sys.exit()

    # Captura as teclas pressionadas no momento
    teclas = pygame.key.get_pressed()

    # Atualiza a posição do quadrado baseado nas teclas pressionadas
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # Evita que o quadrado saia da tela
    x = max(0, min(largura - tamanho_quadrado, x))
    y = max(0, min(altura - tamanho_quadrado, y))

    # Preenche a tela com a cor de fundo
    tela.fill(cor_fundo)

    # Desenha o quadrado na nova posição
    pygame.draw.rect(tela, cor_quadrado, (x, y, tamanho_quadrado, tamanho_quadrado))

    # Atualiza a tela com o novo frame
    pygame.display.flip()

    # Aguarda para manter a taxa de 60 FPS
    clock.tick(60)
