import pygame
import time

# Inicializa o Pygame
pygame.init()

# Definir a largura e altura da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Pong')

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Tamanho das raquetes e bola
raquete_largura = 15
raquete_altura = 100
bola_raio = 15

# Velocidade do jogo
velocidade_raquete = 15
velocidade_bola_x = 5
velocidade_bola_y = 5

# Função para desenhar as raquetes e bola
def desenhar_raquete(x, y):
    pygame.draw.rect(tela, branco, [x, y, raquete_largura, raquete_altura])

def desenhar_bola(x, y):
    pygame.draw.circle(tela, branco, (x, y), bola_raio)

# Função para exibir o placar na tela
def mostrar_pontuacao(jogador1, jogador2):
    fonte = pygame.font.SysFont('arial', 30)
    texto = fonte.render(f'{jogador1} - {jogador2}', True, branco)
    tela.blit(texto, [largura // 2 - texto.get_width() // 2, 10])

# Função para atualizar o arquivo de pontuação
def atualizar_placar(jogador1, jogador2):
    with open('placar.txt', 'a') as arquivo:
        arquivo.write(f'Jogador 1: {jogador1} - Jogador 2: {jogador2}\n')

# Função principal do jogo
def jogo():
    # Posições iniciais
    x_raquete1 = 50
    y_raquete1 = altura // 2 - raquete_altura // 2
    x_raquete2 = largura - 50 - raquete_largura
    y_raquete2 = altura // 2 - raquete_altura // 2
    x_bola = largura // 2
    y_bola = altura // 2
    velocidade_bola_x = 5
    velocidade_bola_y = 5

    # Pontuação
    pontuacao_jogador1 = 0
    pontuacao_jogador2 = 0

    # Inicializa o relógio para controle da taxa de quadros
    relogio = pygame.time.Clock()

    # Loop principal do jogo
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Controles das raquetes
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and y_raquete1 > 0:
            y_raquete1 -= velocidade_raquete
        if teclas[pygame.K_s] and y_raquete1 < altura - raquete_altura:
            y_raquete1 += velocidade_raquete
        if teclas[pygame.K_UP] and y_raquete2 > 0:
            y_raquete2 -= velocidade_raquete
        if teclas[pygame.K_DOWN] and y_raquete2 < altura - raquete_altura:
            y_raquete2 += velocidade_raquete

        # Movimento da bola
        x_bola += velocidade_bola_x
        y_bola += velocidade_bola_y

        # Colisão com as paredes superior e inferior
        if y_bola - bola_raio <= 0 or y_bola + bola_raio >= altura:
            velocidade_bola_y = -velocidade_bola_y

        # Colisão com as raquetes
        if (x_bola - bola_raio <= x_raquete1 + raquete_largura and
            y_raquete1 <= y_bola <= y_raquete1 + raquete_altura) or \
           (x_bola + bola_raio >= x_raquete2 and
            y_raquete2 <= y_bola <= y_raquete2 + raquete_altura):
            velocidade_bola_x = -velocidade_bola_x

        # Pontuação
        if x_bola - bola_raio <= 0:
            pontuacao_jogador2 += 1
            x_bola = largura // 2
            y_bola = altura // 2
            velocidade_bola_x = -velocidade_bola_x
            time.sleep(1)

        if x_bola + bola_raio >= largura:
            pontuacao_jogador1 += 1
            x_bola = largura // 2
            y_bola = altura // 2
            velocidade_bola_x = -velocidade_bola_x
            time.sleep(1)

        # Desenho na tela
        tela.fill(preto)
        desenhar_raquete(x_raquete1, y_raquete1)
        desenhar_raquete(x_raquete2, y_raquete2)
        desenhar_bola(x_bola, y_bola)
        mostrar_pontuacao(pontuacao_jogador1, pontuacao_jogador2)

        # Atualizar o placar no arquivo
        atualizar_placar(pontuacao_jogador1, pontuacao_jogador2)

        # Atualizar a tela
        pygame.display.update()

        # Controlar a taxa de quadros
        relogio.tick(60)

# Iniciar o jogo
if __name__ == "__main__":
    jogo()
