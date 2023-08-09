import pygame
import random 
import sys

# Initialize pygame
pygame.init()


# TODO: add more content to the game over screen
# TODO: figure out how to keep track of the best score
# TODO: find a way to restart the game loop so that it's playable again
# TODO: add a record variable that will serve as a goal 
# TODO: chage the food square to be an icone of some sorts 
# Set up the window dimensions


window_width, window_height = 640, 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game by Vuk')


# Set up the game clock
clock = pygame.time.Clock()


# Define colors (optional)
black = (0, 0, 0)
white = (255, 255, 255)
game_over_color = (255, 0, 0)

# Indicate that the player has lost
game_over = False

# Size of the snake square
snake_block = 10
snake_speed = 12

# Speed limit
speed_limit = snake_speed + 388

# High score
best_score = 0

def snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(window, white, [x[0], x[1], snake_block, snake_block])


# Game over message that is displayed to the user when the game has finished
def game_over_message():
    window.fill(game_over_color)
    font = pygame.font.Font(None, 36)
    message = font.render("Game over", True, black)
    window.blit(message, (window_width // 2 - 80, window_height // 2 - 20))
    pygame.display.update()

# Wait for restart function 
def wait_for_restart():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.K_SPACE:
                waiting = False

def game_loop():
    global game_over, snake_speed, best_score

    # Define the snake's initial position and size
    snake_list = []
    snake_length = 1
    snake_x, snake_y = window_width / 2, window_height / 2
    snake_change_x, snake_change_y = 0, 0
    score = 0 

    # Load a font for displaying the score
    font = pygame.font.Font(None, 30)

     # Generate random food position
    food_x, food_y = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0, round(
        random.randrange(0, window_height - snake_block) / 10.0) * 10.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

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


        # Deletes the first value given to snake_list and ensures that there is always no pair of values in the list to choose from 
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
            # Increase the snake's speed and control it with a maximum value
            snake_speed = min(snake_speed + 2, speed_limit)
            score += 1 

        # Check for window boundaries collision
        if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
            game_over = True
            game_over_message()


        # Check for self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True
                game_over_message()
    
    
    wait_for_restart()



if __name__ == '__main__':
    game_loop()

