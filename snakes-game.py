import pygame
import random 
import sys

pygame.init()

# Set up the window dimensions
window_width, window_height = 640, 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game by Vuk')


# Set up the game clock
clock = pygame.time.Clock()

snake_block = 10

# Define colors (optional)
black = (0, 0, 0)
white = (255, 255, 255)

def snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(window, white, [x[0], x[1], snake_block, snake_block])

def game_loop():
    # Define the snake's initial position and size
    snake_list = []
    snake_length = 1
    snake_x, snake_y = window_width / 2, window_height / 2
    snake_change_x, snake_change_y = 0, 0
    snake_speed = 12
    speed_increase = snake_speed + 20
    score = 0 

    # Load a font for displaying the score
    font = pygame.font.Font(None, 30)

     # Generate random food position
    food_x, food_y = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0, round(
        random.randrange(0, window_height - snake_block) / 10.0) * 10.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                sys.exit()

            # Handle key presses to change the snake's direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_change_x, snake_change_y = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    snake_change_x, snake_change_y = 0, snake_block
                elif event.key == pygame.K_LEFT:
                    snake_change_x, snake_change_y = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    snake_change_x, snake_change_y = snake_block, 0

        # Update the snake's position
        snake_x += snake_change_x
        snake_y += snake_change_y
        # Clear the screen
        window.fill(black)

        # Draw the food
        pygame.draw.rect(window, white, [food_x, food_y, snake_block, snake_block])

        # Draw the snake
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        snake(snake_list)

        # Display the player's score on the game window
        score_display = font.render("Score: " + str(score), True, white)
        window.blit(score_display, (10, 10))

        # Update the screen
        pygame.display.update()

        # Set the frame rate
        clock.tick(snake_speed)

        # Check if the snake eats the food
        if snake_x == food_x and snake_y == food_y:
            food_x, food_y = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0, round(
                random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            snake_length += 1
            # Increase the speed at which the snake is moving 
            clock.tick(speed_increase)
            score += 1 

        # Check for window boundaries collision
        if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
            running = False
            sys.exit()
            
        # Check for self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                running = False
                sys.exit()

if __name__ == '__main__':
    game_loop()

