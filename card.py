
import pygame

class Card:
    def __init__(self, name, path, value, suit):
        self.name = name
        self.path = path

        self.file = self.path + ".png"
        self.original_img = pygame.image.load(self.file).convert_alpha()

        # Scale the card image to 20% of its original size
        width = int(self.original_img.get_width() * 0.2)
        height = int(self.original_img.get_height() * 0.2)
        self.img = pygame.transform.smoothscale(self.original_img, (width, height))

        self.rect = self.img.get_rect(center=(500, 500))

        self.value = value
        self.suit = suit

    def get_name(self):
        return self.name

    def get_path(self):
        return self.path

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def update(self, surface):
        """
        Redraws the entity
        :param surface: The surface to draw the entity on
        """
        surface.blit(self.img, self.rect)

    def move(self, x, y):
        """
        Moves the entity by x and y amount.

        :param x: The amount to move the entity in the x direction
        :param y: The amount to move the entity in the y direction
        """
        self.rect = self.img.get_rect(center=(x, y))