import pygame
from circleshape import *
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    game_clock = pygame.time.Clock()
    dt = 0
       
    # Render the game
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # Spawning player after filling the screen with "black"
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        player.draw(screen)
        
        pygame.display.flip()

        dt = game_clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()