import pygame
from Ball import Ball
from Player import Player

pygame.init()

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configs
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

MIN_PLAYER_HEIGHT = 80
MAX_PLAYER_HEIGHT = WINDOW_HEIGHT - 100


# Función para crear la pantalla, variable para controlar los FPS y función para poder mostrar el marcador
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
pygame.display.set_caption("PONG")

# Jugador #1
player1 = Player(BLACK, 20, WINDOW_HEIGHT/2 - 32.5)

# Jugador #2
player2 = Player(BLACK, WINDOW_WIDTH-36, WINDOW_HEIGHT/2 - 32.5)

# Bola
ball = Ball(BLACK, WINDOW_WIDTH/2 - 12.5, WINDOW_HEIGHT/2 - 12.5, 3, 3)

# Lista para guardar los sprites
allSprites = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            # Player1 move
            if event.key == pygame.K_w:
                player1.move_up()
            if event.key == pygame.K_s:
                player1.move_down()

            # Player2 move
            if event.key == pygame.K_UP:
                player2.move_up()
            if event.key == pygame.K_DOWN:
                player2.move_down()

        # Stop moving on key_up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1.stop()
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2.stop()

    # Evitar que la pelota salga por encima o por debajo del mapa
    if ball.rect.y > WINDOW_HEIGHT-50 or ball.rect.y < 50:
        ball.change_y_direction()

    # Devuelve la pelota al centro y cambia la dirección en la que iba, además aumenta los marcadores
    if ball.rect.x > WINDOW_WIDTH or ball.rect.x < 0:
        if ball.rect.x > WINDOW_WIDTH:
            player1.score_up()

        if ball.rect.x < 0:
            player2.score_up()

        ball.reset_to(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2)
        ball.change_x_direction()

    # Cambia la posición de la raqueta y de la bola
    player1.update(MIN_PLAYER_HEIGHT, MAX_PLAYER_HEIGHT)
    player2.update(MIN_PLAYER_HEIGHT, MAX_PLAYER_HEIGHT)
    ball.update()

    # Colisión entre la bola y los jugadores
    collision_Player1 = pygame.sprite.collide_mask(player1, ball)
    collision_Player2 = pygame.sprite.collide_mask(player2, ball)

    # Cambio de dirección cuando choca la bola con las raquetas
    if collision_Player1:
        if ball.rect.x < player1.rect.x + 12:
            continue
        ball.reset_to(player1.rect.x + 16, ball.rect.y)
        ball.change_x_direction()

    if collision_Player2:
        if ball.rect.x > player2.rect.x-16:
            continue
        ball.reset_to(player2.rect.x - 22, ball.rect.y)
        ball.change_x_direction()

    # Dibuja los sprites
    allSprites.add(player1, player2, ball)
    screen.fill(BLACK)
    allSprites.draw(screen)

    # Agrega el jugador y el marcador a la pantalla
    score1 = font.render(str(player1.score)+" - Jugador 1", False, WHITE)
    score2 = font.render(str(player2.score)+" - Jugador 2", False, WHITE)
    screen.blit(score1, (30, 15))
    screen.blit(score2, (WINDOW_HEIGHT-30, 15))

    pygame.display.flip()

    clock.tick(60)

#[NEAT]
