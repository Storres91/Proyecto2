import pygame

class Ball (pygame.sprite.Sprite):
    def __init__(self, COLORKEY, pos_x, pos_y, speed_y, speed_x) -> None:
        super().__init__()
        
        self.image = pygame.image.load("ball.png").convert()
        self.image.set_colorkey(COLORKEY)
        self.rect = self.image.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed_y = speed_y
        self.speed_x = speed_x