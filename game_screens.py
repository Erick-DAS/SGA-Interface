import pygame
from pygame.locals import *
import random

pygame.init()
pygame.font.init()

########################################
# window values
bounds = (800,800) # grid_size
block_size = 100
window = pygame.display.set_mode(bounds)

# set up fonts
font_path = 'PressStart2P-Regular.ttf'
big_font_size = 60
small_font_size = 30
big_font = pygame.font.Font(font_path, big_font_size)
small_font = pygame.font.Font(font_path, small_font_size)



step_size = 100  # Adjust based on your grid size
UP = (0, -step_size)
DOWN = (0, step_size)
LEFT = (-step_size, 0)
RIGHT = (step_size, 0)
########################################


class GameScreenController:
    def __init__(self):
        # Initialize the window and font values used throughout the game
        self.window = window
        self.big_font = big_font
        self.small_font = small_font

        # Initialize all screen instances
        self.init_screen = InitScreen(window, big_font, small_font)
        self.game_over_screen = GameOverScreen(window, big_font, small_font)
        self.game_won_screen = GameWonScreen(window, big_font, small_font)
        self.pause_screen = PauseScreen(window, big_font, small_font)
        self.in_game_screen = InGameScreen(window, big_font, small_font)
        
        # Start with the initial screen
        self.current_screen = self.init_screen

    def switch_screen(self, new_screen):
        #Switch the current screen to the specified one
        self.current_screen = new_screen

    def render_current_screen(self):
        #Render the currently active screen
        self.current_screen.render()

class GameScreens:
    def __init__(self, window, big_font, small_font):
        self.window = window
        self.big_font = big_font    
        self.small_font = small_font
    
    def render(self):
        pass
    
class InitScreen(GameScreens):

    def render(self):
        self.window.fill((0,0,0))
        # declare what will be written
        text1 = self.big_font.render('S.G.A', True, (255,255,255))
        text2 = self.small_font.render('Jogar', True, (255,255,255))
        # declare the position of the text
        text1_rect = text1.get_rect(center=(bounds[0]/2, bounds[1]/2 - 120))
        text2_rect = text2.get_rect(center=(bounds[0]/2, bounds[1]/2 + 60))

        self.window.blit(text1, text1_rect)
        self.window.blit(text2, text2_rect)
        pygame.display.update()

class GameOverScreen(GameScreens):
    def render(self):
        self.window.fill((0,0,0))
        # declare what will be written
        text1 = self.big_font.render('Game Over', True, (255,255,255))

        # declare the position of the text
        text1_rect = text1.get_rect(center=(bounds[0]/2, bounds[1]/2 - 120))

        self.window.blit(text1, text1_rect)
        pygame.display.update()


class GameWonScreen(GameScreens):

    def render(self):
        self.window.fill((0,0,0))
        # declare what will be written
        text1 = self.big_font.render('Ganhou!', True, (255,255,255))

        # declare the position of the text
        text1_rect = text1.get_rect(center=(bounds[0]/2, bounds[1]/2 - 120))

        self.window.blit(text1, text1_rect)
        pygame.display.update()

class PauseScreen(GameScreens):

    def render(self):
        self.window.fill((0,0,0))
        # declare what will be written
        text1 = self.big_font.render('Pause', True, (255,255,255))

        # declare the position of the text
        text1_rect = text1.get_rect(center=(bounds[0]/2, bounds[1]/2 - 120))

        self.window.blit(text1, text1_rect)
        pygame.display.update()

class InGameScreen(GameScreens):
    def __init__(self, window, big_font, small_font):
        super().__init__(window, big_font, small_font)
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.snake_dir = RIGHT  # Start moving right
        self.food_pos = self.get_random_food_position()
        self.food_eaten = False

    def get_random_food_position(self):
        return (random.randint(0, (bounds[0] // block_size) - 1) * block_size,
                random.randint(0, (bounds[1] // block_size) - 1) * block_size)

    def update_snake(self):
        # Calculate new head position
        new_head = (self.snake[0][0] + self.snake_dir[0], self.snake[0][1] + self.snake_dir[1])
        pygame.time.delay(100)
        pygame.time.delay(100)

        # Check for collisions with boundaries or self
        if (new_head[0] >= bounds[0] or new_head[0] < 0 or
            new_head[1] >= bounds[1] or new_head[1] < 0 or
            new_head in self.snake):
            return True  # Indicate game over

        # Insert new head
        self.snake.insert(0, new_head)

        # Check for food collision
        if new_head == self.food_pos:
            self.food_eaten = True
            self.food_pos = self.get_random_food_position()  # Place new food
        else:
            self.snake.pop()  # Remove tail

        return False  # Game continues

    def render(self):
        self.window.fill((0,0,0))
        for pos in self.snake:
            pygame.draw.rect(self.window, (0, 255, 0), (*pos, block_size - 10, block_size - 10))
        pygame.draw.rect(self.window, (255, 0, 0), (*self.food_pos, block_size, block_size))

        # draw score
        score = len(self.snake) - 3
        score_text = self.small_font.render(f'Score: {score}', True, (255, 255, 255))
        self.window.blit(score_text, (10, 10))

        pygame.display.update()

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.snake_dir != DOWN:
                self.snake_dir = UP
            elif event.key == pygame.K_DOWN and self.snake_dir != UP:
                self.snake_dir = DOWN
            elif event.key == pygame.K_LEFT and self.snake_dir != RIGHT:
                self.snake_dir = LEFT
            elif event.key == pygame.K_RIGHT and self.snake_dir != LEFT:
                self.snake_dir = RIGHT

    def reinit(self):
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.snake_dir = RIGHT
        self.food_pos = self.get_random_food_position()
        self.food_eaten = False