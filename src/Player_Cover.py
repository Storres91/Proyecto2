import pygame


class Player_Cover(pygame.sprite.Sprite):
    def __init__(self, color_key):
        super().__init__()
        
        self.image = pygame.image.load("../assets/frontRaqueta.png").convert()
        self.image.set_colorkey(color_key)
        self.rect = self.image.get_rect()