import pygame
import random 
import sys

# Initialize pygame
pygame.init()


# TODO: add more content to the game over screen
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
snake_length = 1
score = 0 

# Speed limit
speed_limit = snake_speed + 388

# High score
best_score = [0]

def snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(window, white, [x[0], x[1], snake_block, snake_block])

def check_high_score():
    if score > best_score[0]:
        return True


# Game over message that is displayed to the user when the game has finished
def game_over_message():
    window.fill(game_over_color)
    font = pygame.font.Font(None, 36)
    message = font.render("Game over press SPACE key to play again", True, white)
    message_rect = message.get_rect(center=(window_width // 2, window_height // 2))
    window.blit(message, message_rect)
    pygame.display.update()

    # Set a timer for how long the message should be displayed (in milliseconds)
    message_duration = 5000  # 3 seconds
    start_time = pygame.time.get_ticks()

    while pygame.time.get_ticks() - start_time < message_duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return True

        # You can add any other game logic here that you want to run during the message display

    return False   

def game_loop():
    global game_over, snake_speed, best_score, snake_length, score

    while True:
        # Reset game variables
        snake_length = 1
        snake_speed = 12
        score = 0
        game_over = False  # Reset game_over flag

        # Define the snake's initital position and size
        snake_list = []
        snake_x, snake_y = window_width / 2, window_height / 2
        snake_change_x, snake_change_y = 0, 0
            

        # Load a font for displaying the score
        font = pygame.font.Font(None, 30)

        # Generate random food position
        food_x, food_y = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0, round(
            random.randrange(0, window_height - snake_block) / 10.0) * 10.0
        
        # window.fill(black)
        pygame.display.update()
            

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    # Quit the game if the user presses the X on the window
                    pygame.quit()
                    sys.exit()

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

            # Interacting with the best_score variable
            if check_high_score():
                del best_score[0]
                best_score.append(score)
                
                
            # Check for window boundaries collision
            if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
                game_over = True
                if game_over_message():
                    break
                


            # Check for self-collision
            for segment in snake_list[:-1]:
                if segment == snake_head:
                    game_over = True
                    if game_over_message():
                        break
                    
        print(best_score)
        

    """
        # If the score is bigger than the high_score, append it to high_score and delete the previous value
        if score > best_score:
        best_score.append(score)
        del best_score[0]
        print(best_score)
    """
  




if __name__ == '__main__':
    game_loop()
