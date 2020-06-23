import sys
import pygame

def run_game():
    # initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 900))

    pygame.display.set_caption("Key Game")

    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
            
run_game()

