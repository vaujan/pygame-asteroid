import pygame
from circleshape import *
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    clock = pygame.time.Clock()
    dt = 0
    
    # Game font setup - only need to do this once
    game_font_title = pygame.font.Font(None, 74)
    game_font_subtitle = pygame.font.Font(None, 32)
    game_over_text = game_font_title.render("Game Over", True, "white")
    press_r_text = game_font_subtitle.render("Press r to restart", True, "white")
    game_over_text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    press_r_text_subtitle_rect = press_r_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))

    def init_game():
        # Initialize all sprite groups
        updateable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroid = pygame.sprite.Group()
        shots = pygame.sprite.Group()

        # Set up sprite containers
        Player.containers = (updateable, drawable)
        Asteroid.containers = (asteroid, updateable, drawable)
        AsteroidField.containers = (updateable)
        Shot.containers = (shots, updateable, drawable)

        # Create game objects 
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        asteroid_field = AsteroidField()
        
        return updateable, drawable, asteroid, shots, player, asteroid_field, False

    # Initial game setup
    updateable, drawable, asteroid, shots, player, asteroid_field, game_over = init_game()

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Game Logic
        keys = pygame.key.get_pressed()
       
        if game_over and keys[pygame.K_r]:
            # Reset entire game state
            updateable, drawable, asteroid, shots, player, asteroid_field, game_over = init_game()
        elif not game_over:
            # Update all sprites
            for sprite in updateable:
                sprite.update(dt)

            # Check collisions
            for asteroid_sprite in asteroid:
                if player.is_collided(asteroid_sprite):
                    game_over = True
                for shot in shots:
                    if shot.is_collided(asteroid_sprite):
                        asteroid_sprite.split()
                        shot.kill()

        # Rendering
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        # Game over conditions
        if game_over:
           screen.blit(game_over_text, game_over_text_rect)
           screen.blit(press_r_text, press_r_text_subtitle_rect)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
