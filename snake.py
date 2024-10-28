import pygame

# Initialize the game
pygame.init()

# Set up display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Set FPS and clock
FPS = 20
clock = pygame.time.Clock()

SNAKE_SIZE = 20

head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT // 2 + 100

snake_dx = 0
snake_dy = 0

score = 0

# Set up colors
GREEN = (0, 255, 0)
DARKGREEN = (0, 100, 0)
RED = (255, 0, 0)
DARKRED = (100, 0, 0)
WHITE = (255, 255, 255)

# Set fonts
font = pygame.font.SysFont('gabriola', 30)

# Set text
title_text = font.render('Snake Game', True, GREEN, DARKRED)
title_text_rect = title_text.get_rect()
title_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

score_text = font.render('Score: ' + str(score), True, GREEN, DARKRED)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10, 10)

game_over_text = font.render('Game Over', True, RED, DARKGREEN)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render('Press any key to continue', True, WHITE, DARKGREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)

# Set sounds
pick_up_sound = pygame.mixer.Sound('pick_up_sound.wav')

# Set images
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)

body_coords = []

# The main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1 * SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
    display_surface.fill(WHITE)

    # Blit HUD
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(score_text, score_text_rect)

    # Blit assets
    pygame.draw.rect(display_surface, GREEN, head_coord)
    pygame.draw.rect(display_surface, RED, apple_coord)

    # Update the display
    pygame.display.update()
    clock.tick(FPS)

# Quit the game
pygame.quit()
