import pygame
pygame.init()

#Colores
black = (0, 0, 0)
white = (255, 255, 255)

#Definir tamaño de la pantalla
size = (800, 600)

#Jugador #1
player1_pos_x = 5
player1_pos_y = 250
player1_speed_y = 0

#Jugador #2
player2_pos_x = 720
player2_pos_y = 250
player2_speed_y = 0

#Bola
ball_pos_x = (size[0]/2)
ball_pos_y = (size[1]/2)
ball_speed_x = 3
ball_speed_y = 3

#marcador
score_player1 = 0
score_player2 = 0

#Función para crear la pantalla, variable para controlar los FPS y función para poder mostrar el marcador
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
pygame.display.set_caption("PONG")

#Clases de los jugadores y la bola
class player1(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("raqueta.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

class player2(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("raqueta.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

class ball(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("ball.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

#Lista para guardar los sprites
allSprites = pygame.sprite.Group()

#Asignar a una variable la clase
player1 = player1()
player2 = player2()
ball = ball()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        #Cambio de velocidad raqueta player 1, subir o bajar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_speed_y += -3
            if event.key == pygame.K_s:
                player1_speed_y += 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_speed_y = 0
            if event.key == pygame.K_s:
                player1_speed_y = 0

        #Cambio de velocidad raqueta player 2, subir o bajar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player2_speed_y += -3
            if event.key == pygame.K_DOWN:
                player2_speed_y += 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player2_speed_y = 0
            if event.key == pygame.K_DOWN:
                player2_speed_y = 0

    #Evitar que la pelota salga por encima o por debajo del mapa
    if ball_pos_y > 550 or ball_pos_y < 50:
        ball_speed_y *= -1

    #Devuelve la pelota al centro y cambia la dirección en la que iba, además aumenta los marcadores
    if ball_pos_x > 800:
        ball_pos_x = (size[0]/2)
        ball_pos_y = (size[1]/2)
        ball_speed_x *= -1
        score_player1 += 1
    
    if ball_pos_x < 0:
        ball_pos_x = (size[0]/2)
        ball_pos_y = (size[1]/2)
        ball_speed_x *= -1
        score_player2 += 1
    
    #Cambia la posición de la raqueta y de la bola
    player1_pos_y += player1_speed_y
    player2_pos_y += player2_speed_y
    ball_pos_x += ball_speed_x
    ball_pos_y += ball_speed_y

    #Evita que la raqueta salga del campo de juego
    if player1_pos_y < 50 or player1_pos_y > 500:
        player1_speed_y = 0
    if player2_pos_y < 50 or player2_pos_y > 500:
        player2_speed_y = 0
    
    #Coordenadas de player 1
    player1.rect.x = player1_pos_x
    player1.rect.y = player1_pos_y

    #Coordenadas de player 2
    player2.rect.x = player2_pos_x
    player2.rect.y = player2_pos_y

    #Coordenadas de la bola
    ball.rect.x = ball_pos_x
    ball.rect.y = ball_pos_y

    #Colisión entre la bola y los jugadores
    collision_Player1 = pygame.sprite.collide_mask(player1, ball)
    collision_Player2 = pygame.sprite.collide_mask(player2, ball)
    if collision_Player1 or collision_Player2:
        ball_speed_x *= -1

    #Agrega los sprites a una lista para poder dibujarlo
    allSprites.add(player1, player2, ball)
    
    screen.fill(black)

    #Dibuja los sprites
    allSprites.draw(screen)

    #Agrega el jugador y el marcador a la pantalla
    score1 = font.render(str(score_player1), 0, white)
    score2 = font.render(str(score_player2), 0, white)
    Player1 = font.render("- Jugador 1", 0, white )
    Player2 = font.render("- Jugador 2", 0, white)
    screen.blit(score1, (20,15))
    screen.blit(score2, (570,15))
    screen.blit(Player1, (50, 15))
    screen.blit(Player2, (600,15))

    pygame.display.flip()

    clock.tick(60)