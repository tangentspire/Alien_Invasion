import pygame

class Rocket():

    def __init__(self, screen):
        """Initialize the rocket and its starting position."""
        self.screen = screen

        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each rocket in the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.center = self.screen_rect.center

        # Movement Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        elif self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
