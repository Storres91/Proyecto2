import pygame

class Player_Cover(pygame.sprite.Sprite):
    def __init__(self, COLORKEY):
        super().__init__()
        
        self.image = pygame.image.load("./assets/frontRaqueta.png").convert()
        self.image.set_colorkey(COLORKEY)
        self.rect = self.image.get_rect()