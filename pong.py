import pygame
pygame.init()

#Colores
black = (0, 0, 0)
white = (255, 255, 255)

size = (800, 600)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#Tamaño raquetas
player_width = 20
player_height = 90

#Jugador #1
player1_pos_x = 20
player1_pos_y = 300
player1_speed_y = 0

#Jugador #2
player2_pos_x = 760
player2_pos_y = 300
player2_speed_y = 0

#Bola
ball_pos_x = 400
ball_pos_y = 300
ball_speed_x = 3
ball_speed_y = 3


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        #Movimiento jugador #1
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
        
        #Movimiento jugador #2
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
    if ball_pos_y > 600-(player_height/2) or ball_pos_y < 5+(player_height/2):
        ball_speed_y *= -1
    
    #Devuelve la pelota al centro y cambia la dirección en la que iba
    if ball_pos_x > 800 or ball_pos_x < 0:
        ball_pos_x = 400
        ball_pos_y = 300
        ball_speed_x *= -1
    
    #Define la posición de las raquetas y de la pelota según condiciones anteriores
    player1_pos_y += player1_speed_y
    player2_pos_y += player2_speed_y
    ball_pos_x += ball_speed_x
    ball_pos_y += ball_speed_y

    #Evita que la raqueta salga del campo de juego
    if (player1_pos_y - player_height) < 0 or (player1_pos_y + player_height)> 600:
        player1_speed_y = 0
    if player2_pos_y < 5 or (player2_pos_y + player_height)> 600-5:
        player2_speed_y = 0

    screen.fill(black)

    #Dibujar las raquetas y la pelota
    player1 = pygame.draw.rect (screen, white, (player1_pos_x, player1_pos_y-(player_height/2), player_width, player_height))
    player2 = pygame.draw.rect (screen, white, (player2_pos_x, player2_pos_y-(player_height/2), player_width, player_height))
    ball = pygame.draw.circle (screen, white, (ball_pos_x, ball_pos_y), 10)
    
    #Genera el cambio de dirección de la pelota al colisionar con la raqueta
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1



    pygame.display.flip()
    clock.tick(60)