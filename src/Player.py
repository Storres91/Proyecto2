import pygame


class Player (pygame.sprite.Sprite):
    def __init__(self, color_key, pos_x, pos_y, speed_y):
        super().__init__()
        
        self.image = pygame.image.load("../assets/raqueta.png").convert()
        self.image.set_colorkey(color_key)
        self.rect = self.image.get_rect()

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed_y = speed_y
        self.score = 0

    def score_up(self):
        self.score += 1

    def move_up(self):
        self.speed_y += -3

    def move_down(self):
        self.speed_y += 3

    def stop(self):
        self.speed_y = 0

        
