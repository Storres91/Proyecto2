import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, color_key, pos_x, pos_y, speed_y, speed_x) -> None:
        super().__init__()

        self.image = pygame.image.load("../assets/ball.png").convert()
        self.image.set_colorkey(color_key)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed_y = speed_y
        self.speed_x = speed_x

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

    def reset_to(self, pos_x, pos_y):
        self.rect.x = pos_x
        self.rect.y = pos_y

    def change_y_direction(self):
        self.speed_y *= -1

    def change_x_direction(self):
        self.speed_x *= -1
