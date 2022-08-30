import pygame
from typing import Tuple


class Ball(pygame.sprite.Sprite):
    def __init__(self, color_key: Tuple[int, int, int], pos_x: float, pos_y: float, speed_y: float, speed_x: float):
        super().__init__()

        self.image = pygame.image.load("../assets/ball.png").convert()
        self.image.set_colorkey(color_key)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed_y = speed_y
        self.speed_x = speed_x

    def update(self):
        """
        update(self) -> None
        Updates this ball's y_pos and x_pos according to the current x/y_speed
        """
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

    def reset_to(self, pos_x, pos_y):
        """
        reset_to(self, pos_x, pos_y) -> None
        Resets this ball to a set position in x (pos_x) and y (pos_y)
        """
        self.rect.x = pos_x
        self.rect.y = pos_y

    def change_y_direction(self):
        """
        change_y_direction(self) -> None
        Speed_y *= -1 Inverts y direction of the ball
        """
        self.speed_y *= -1

    def change_x_direction(self):
        """
        change_x_direction(self) -> None
        Speed_x *= -1 Inverts x direction of the ball
        """
        self.speed_x *= -1
