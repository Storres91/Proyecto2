import pygame

class Player (pygame.sprite.Sprite):
    def __init__ (self, COLORKEY, pos_x, pos_y, speed_y, ):
        super().__init__
        BLACK = (0, 0, 0)
        
        self.image = pygame.image.load("./assets/raqueta.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed_y = speed_y
        
