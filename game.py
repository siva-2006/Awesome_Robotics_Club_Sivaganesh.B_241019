import pygame
import random
import sys

pygame.init()

# Constants
BLOCK_SIZE = 20
WIDTH, HEIGHT = 600, 400
FONT = pygame.font.SysFont('arial', 25)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, (*block, BLOCK_SIZE, BLOCK_SIZE))

# Display score
def show_score(score):
    value = FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(value, [10, 10])

# Game over screen with replay option
def game_over_screen(score):
    screen.fill(BLACK)
    msg1 = FONT.render(f"Game Over! Final Score: {score}", True, RED)
    msg2 = FONT.render("Press R to Restart or Q to Quit", True, WHITE)
    screen.blit(msg1, [WIDTH // 2 - 150, HEIGHT // 2 - 20])
    screen.blit(msg2, [WIDTH // 2 - 170, HEIGHT // 2 + 20])
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    return  # Exit to restart game

# Main game loop
def main():
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0
    snake = [[x, y]]
    length = 1
    score = 0

    food = [random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
            random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE]

    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK_SIZE
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK_SIZE, 0

        x += dx
        y += dy
        snake.append([x, y])

        if len(snake) > length:
            del snake[0]

        # Collision detection
        if ([x, y] in snake[:-1]) or (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT):
            game_over_screen(score)
            return  # Exit this game loop to restart

        # Food eating
        if [x, y] == food:
            length += 1
            score += 1
            food = [random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                    random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE]

        pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))
        draw_snake(snake)
        show_score(score)

        pygame.display.update()
        clock.tick(10 + (length // 5))  # Increase speed as snake grows

while True:
    main()
