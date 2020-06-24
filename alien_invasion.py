import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events and close the game if pygame
        # quit event is detected.
        gf.check_events(ai_settings, screen, ship, bullets)
        # Update the ship's position
        ship.update()
        bullets.update()
        # Redraw the screen during each pass through the look.
        gf.update_screen(ai_settings, screen, ship, bullets)     

run_game()
