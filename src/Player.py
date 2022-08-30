from typing import Tuple
import pygame


class Player (pygame.sprite.Sprite):
    def __init__(self, color_key: Tuple[int, int, int], pos_x: float, pos_y: float):
        super().__init__()
        
        self.image = pygame.image.load("../assets/raqueta.png").convert()
        self.image.set_colorkey(color_key)
        self.rect = self.image.get_rect()

        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed_y = 0
        self.score = 0

    def update(self, min_height: float, max_height: float):
        """
        update(self) -> None
        Updates this player's y_pos according to the y_speed
        """
        self.rect.y += self.speed_y

        # Evita que la raqueta salga del campo de juego
        if self.rect.y < min_height or self.rect.y > max_height:
            self.speed_y = 0

    def score_up(self):
        """
        score_up(self) -> None
        Player score += 1 adds 1 to this player's score
        """
        self.score += 1

    def move_up(self):
        """
        move_up(self, min_height, max_height) -> None
        Speed_y = -3 make the player go up (negative y) to a maximum height of max_height
        """
        self.speed_y += -3

    def move_down(self):
        """
        move_down(self, min_height, max_height) -> None
        Speed_y = 3 make the player go down (positive y) to a minimum height of min_height
        """
        self.speed_y += 3

    def stop(self):
        """
        stop(self) -> None
        Speed_y = 0 avoid player from moving
        """
        self.speed_y = 0

        
