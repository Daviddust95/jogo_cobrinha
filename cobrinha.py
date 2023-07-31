import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

INITIAL_LENGTH = 3
SPEED = 15

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo da Cobrinha")
clock = pygame.time.Clock()

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))

def draw_food(food_position):
    pygame.draw.rect(screen, RED, pygame.Rect(food_position[0], food_position[1], GRID_SIZE, GRID_SIZE))

def show_score(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score), True, GREEN)
    screen.blit(text, (10, 10))

def game_over():
    font = pygame.font.SysFont(None, 50)
    text = font.render("Perdeu kkk", True, GREEN)
    screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(2000)
    main()

def main():
    snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    snake_direction = (GRID_SIZE, 0)
    snake_length = INITIAL_LENGTH
    food_position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and snake_direction != (GRID_SIZE, 0):
            snake_direction = (-GRID_SIZE, 0)
        elif keys[pygame.K_RIGHT] and snake_direction != (-GRID_SIZE, 0):
            snake_direction = (GRID_SIZE, 0)
        elif keys[pygame.K_UP] and snake_direction != (0, GRID_SIZE):
            snake_direction = (0, -GRID_SIZE)
        elif keys[pygame.K_DOWN] and snake_direction != (0, -GRID_SIZE):
            snake_direction = (0, GRID_SIZE)

        snake_head = ((snake[0][0] + snake_direction[0]), (snake[0][1] + snake_direction[1]))
        snake.insert(0, snake_head)

        if snake_head == food_position:
            food_position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
            snake_length += 1
            score += 10

        if len(snake) > snake_length:
            snake.pop()

        if snake_head[0] < 0 or snake_head[0] >= SCREEN_WIDTH or snake_head[1] < 0 or snake_head[1] >= SCREEN_HEIGHT:
            game_over()

        screen.fill(BLACK)
        draw_snake(snake)
        draw_food(food_position)
        show_score(score)

        pygame.display.update()
        clock.tick(SPEED)

    pygame.quit()

if __name__ == "__main__":
    main()
