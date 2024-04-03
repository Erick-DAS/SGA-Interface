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


UP = (0, -block_size)
DOWN = (0, block_size)
LEFT = (-block_size, 0)
RIGHT = (block_size, 0)
########################################


class GameScreenController:
    def __init__(self, bin_apple_pos, bin_snake_pos):
        # Initialize the window and font values used throughout the game
        self.window = window
        self.big_font = big_font
        self.small_font = small_font

        # Initialize all screen instances
        self.init_screen = InitScreen(window, big_font, small_font)
        self.game_over_screen = GameOverScreen(window, big_font, small_font)
        self.game_won_screen = GameWonScreen(window, big_font, small_font)
        self.pause_screen = PauseScreen(window, big_font, small_font)
        self.in_game_screen = InGameScreen(window, big_font, small_font,bin_apple_pos,bin_snake_pos)
        
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
    

    def __init__(self, window, big_font, small_font):
        super().__init__(window, big_font, small_font)
        self.options = ["Border", "Difficulty", "speed"]
        self.current_selection = 0  # Index of the currently selected option

    def render(self):
        velocity = 1
        boundary = 0
        difficulty = 1

        self.window.fill((0,0,0))

        # Title
        title_text = self.big_font.render('S.G.A', True, (255,255,255))
        title_rect = title_text.get_rect(center=(bounds[0]/2, bounds[1]/2 - 120))

        if boundary == 0:
            boundary_text = self.small_font.render('Mode: Border', True, (214,205,84))
        else:
            boundary_text = self.small_font.render('Mode: No Border', True, (209,38,38))
        
        boundary_rect = boundary_text.get_rect(center=(bounds[0]/2, bounds[1]/2))

        if difficulty == 0:
            difficulty_text = self.small_font.render('Difficulty: Normal', True, (214,205,84))
        else:
            difficulty_text = self.small_font.render('Difficulty: Hard', True, (209,38,38))
        
        difficulty_rect = difficulty_text.get_rect(center=(bounds[0]/2, bounds[1]/2 + 40))

        if velocity == 0:
            velocity_text = self.small_font.render('Speed: Normal', True, (214,205,84))
        else:
            velocity_text = self.small_font.render('Speed: Fast', True, (209,38,38))

        velocity_rect = velocity_text.get_rect(center=(bounds[0]/2, bounds[1]/2 + 80))

        self.window.blit(title_text, title_rect)
        self.window.blit(boundary_text, boundary_rect)
        self.window.blit(difficulty_text, difficulty_rect)
        self.window.blit(velocity_text, velocity_rect)

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
    
    def __init__(self, window, big_font, small_font, snake_pos, apple_pos):
        super().__init__(window, big_font, small_font)

        # Initialize the snake and food
        self.snake = [[2*block_size, 1*block_size], [1*block_size, 1*block_size]]
        self.food_pos = [((apple_pos[3]*4 + apple_pos[4]*2 + apple_pos[5]*1)*block_size), ((apple_pos[0]*4 + apple_pos[1]*2 + apple_pos[2]*1)*block_size)]
        self.food_eaten = False
        self.snake_pos = snake_pos
        self.apple_pos = apple_pos
        self.prev_food_pos = apple_pos
        self.new_food_item = 0

    def update_snake(self, apple_pos, snake_pos):

        self.snake_pos = snake_pos
        self.apple_pos = apple_pos
        self.food_pos = [((apple_pos[3]*4 + apple_pos[4]*2 + apple_pos[5]*1)*block_size), ((apple_pos[0]*4 + apple_pos[1]*2 + apple_pos[2]*1)*block_size)]
        

        # Calculate new head position
        new_head = [((self.snake_pos[3]*4 + self.snake_pos[4]*2 + self.snake_pos[5]*1)*block_size), ((self.snake_pos[0]*4 + self.snake_pos[1]*2 + self.snake_pos[2]*1)*block_size)]
        changed_pos = False
        
        # Insert new head
        if new_head != self.snake[0]:
            self.snake.insert(0, new_head)
            changed_pos = True
        else:
            changed_pos = False

        # Check for food collision
            
        # rint(f'changed_pos: {changed_pos}; new_head != self.food_pos : {new_head != self.food_pos}; new_head: {new_head}; food_pos: {self.food_pos}')

        if new_head != self.prev_food_pos and changed_pos == True:
            self.snake.pop()  # Remove tail
        elif new_head == self.food_pos and changed_pos == True:
            print("ENTREI NA MACA")
        
        self.prev_food_pos = self.food_pos

        # print(self.snake)
        return False  # Game continues
    

    def render(self):
        self.window.fill((0,0,0))
        for pos in self.snake:
            pygame.draw.rect(self.window, (0, 255, 0), (*pos, block_size - 10, block_size - 10))
        pygame.draw.rect(self.window, (255, 0, 0), (*self.food_pos, block_size, block_size))

        # draw score
        score = len(self.snake) - 2
        score_text = self.small_font.render(f'Score: {score}', True, (255, 255, 255))
        self.window.blit(score_text, (10, 10))

        pygame.display.update()

    def reinit(self):
        self.snake = [(3*block_size, 1*block_size), (2*block_size, 1*block_size)]
        self.food_pos = [((self.apple_pos[3]*4 + self.apple_pos[4]*2 + self.apple_pos[5]*1)*block_size), ((self.apple_pos[0]*4 + self.apple_pos[1]*2 + self.apple_pos[2]*1)*block_size)]
        self.food_eaten = False