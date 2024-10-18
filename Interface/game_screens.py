import os
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

########################################
# window values
bounds = (800,800) # grid_size
block_size = 100
window = pygame.display.set_mode(bounds)

# set up fonts

# select current path of where the file is being executed
system_path = os.path.dirname(os.path.abspath(__file__))
# return to parent folder;
system_path = os.path.dirname(system_path)   
# enter assets folder
assets_path = os.path.join(system_path, 'assets')

font_path = os.path.join(assets_path, 'PressStart2P-Regular.ttf')
little_bigger_font_size = 85
big_font_size = 85
small_font_size = 25
little_bigger_font = pygame.font.Font(font_path, little_bigger_font_size)
big_font = pygame.font.Font(font_path, big_font_size)
small_font = pygame.font.Font(font_path, small_font_size)


# load assets

## Apple
apple_asset = pygame.image.load(os.path.join(assets_path, 'apple_asset.png'))
apple_asset = pygame.transform.scale(apple_asset, (block_size, block_size))

## Background
background = pygame.image.load(os.path.join(assets_path, 'grass.png'))
background = pygame.transform.scale(background, bounds)

background2 = pygame.image.load(os.path.join(assets_path, 'grass_apple.png'))
background2 = pygame.transform.scale(background2, bounds)


background1_coords = -800
background2_coords = 0
## Snake



UP = (0, -block_size)
DOWN = (0, block_size)
LEFT = (-block_size, 0)
RIGHT = (block_size, 0)
########################################


class GameScreenController:
    def __init__(self, bin_apple_pos, bin_snake_pos, bin_vel, bin_mode, bin_diff):
        # Initialize the window and font values used throughout the game
        self.window = window
        self.big_font = big_font
        self.small_font = small_font

        # Initialize all screen instances
        self.init_screen = InitScreen(window, big_font, small_font, bin_vel, bin_mode, bin_diff)
        self.game_over_screen = GameOverScreen(window, big_font, small_font, little_bigger_font)
        self.game_won_screen = GameWonScreen(window, big_font, small_font, little_bigger_font)
        self.pause_screen = PauseScreen(window, big_font, small_font, little_bigger_font)
        self.in_game_screen = InGameScreen(window, big_font, small_font, bin_apple_pos, bin_snake_pos)
        
        # Start with the initial screen
        self.current_screen = self.init_screen

    def switch_screen(self, new_screen):
        #Switch the current screen to the specified one
        self.current_screen = new_screen

    def render_current_screen(self):
        #Render the currently active screen
        self.current_screen.render()

class GameScreens:
    def __init__(self, window, big_font, small_font, little_bigger_font):
        self.window = window
        self.big_font = big_font    
        self.small_font = small_font
        self.little_bigger_font = little_bigger_font
    
    def render(self):
        pass
    
class InitScreen(GameScreens):
    

    def __init__(self, window, big_font, small_font, bin_vel, bin_mode, bin_diff):
        super().__init__(window, big_font, small_font, little_bigger_font)
        self.options = ["Border", "Difficulty", "speed"]
        self.current_selection = 0  # Index of the currently selected option
        self.bin_vel = bin_vel
        self.bin_mode = bin_mode
        self.bin_diff = bin_diff
        self.background1_coords = -800
        self.background2_coords = 0

    def render(self):
        velocity = self.bin_vel
        boundary = self.bin_mode
        difficulty = self.bin_diff
        

        #background
        self.window.blit(background, (int(self.background1_coords), 0))
        self.window.blit(background2, (int(self.background2_coords), 0))
        
        self.background1_coords += 1
        self.background2_coords += 1

        if self.background1_coords >= 800:
            self.background1_coords = -800
        
        if self.background2_coords >= 800:
            self.background2_coords = -800



        # Title
        title_background_text = self.little_bigger_font.render('S.G.A', True, (0, 0, 0))
        title_background_rect = title_background_text.get_rect(center=(bounds[0]/2 + 6, bounds[1]/2 - 115))

        title_text = self.big_font.render('S.G.A', True, (179, 20, 58)) #122, 13, 39  24, 106, 237   179, 20, 58
        title_rect = title_text.get_rect(center=(bounds[0]/2, bounds[1]/2 - 120))

        if boundary == 0:
            boundary_text = self.small_font.render('Mode: No Border', True, (24, 106, 237))
        else:
            boundary_text = self.small_font.render('Mode: Border', True, (209,38,38))
        
        boundary_rect = boundary_text.get_rect(center=(bounds[0]/2, bounds[1]/2))

        if difficulty == 0:
            difficulty_text = self.small_font.render('Difficulty: Normal', True, (24, 106, 237))
        else:
            difficulty_text = self.small_font.render('Difficulty: Hard', True, (209,38,38))
        
        difficulty_rect = difficulty_text.get_rect(center=(bounds[0]/2, bounds[1]/2 + 40))

        if velocity == 0:
            velocity_text = self.small_font.render('Speed: Normal', True, (24, 106, 237))
        else:
            velocity_text = self.small_font.render('Speed: Fast', True, (209,38,38))

        velocity_rect = velocity_text.get_rect(center=(bounds[0]/2, bounds[1]/2 + 80))

        self.window.blit(title_background_text, title_background_rect)
        self.window.blit(title_text, title_rect)
        self.window.blit(boundary_text, boundary_rect)
        self.window.blit(difficulty_text, difficulty_rect)
        self.window.blit(velocity_text, velocity_rect)

        pygame.display.update()

    def update_Init(self, bin_vel, bin_mode, bin_diff):
        self.bin_vel = bin_vel
        self.bin_mode = bin_mode
        self.bin_diff = bin_diff

class GameOverScreen(GameScreens):
    def render(self):
        
        #background
        self.window.blit(background, (0, 0))

        #text backgrounf
        text1_background = self.little_bigger_font.render('Game Over', True, (0, 0, 0))

        # declare what will be written
        text1 = self.big_font.render('Game Over', True, (179, 20, 58))

        # declare the position of the text
        text1_background_rect = text1_background.get_rect(center=(bounds[0]/2 + 6, bounds[1]/2 - 115))

        text1_rect = text1.get_rect(center=(bounds[0]/2, bounds[1]/2 - 120))

        self.window.blit(text1_background, text1_background_rect)
        self.window.blit(text1, text1_rect)
        pygame.display.update()


class GameWonScreen(GameScreens):

    def render(self):

        #background
        self.window.blit(background, (0, 0))

        #text background
        text1_background = self.little_bigger_font.render('Ganhou!', True, (0, 0, 0))

        # declare what will be written
        text1 = self.big_font.render('Ganhou!', True, (179, 20, 58))

        # declare the position of the text
        text1_background_rect = text1_background.get_rect(center=(bounds[0]/2 + 6, bounds[1]/2 - 115))
        text1_rect = text1.get_rect(center=(bounds[0]/2, bounds[1]/2 - 120))

        self.window.blit(text1_background, text1_background_rect)
        self.window.blit(text1, text1_rect)
        pygame.display.update()

class PauseScreen(GameScreens):

    def render(self):

        #background
        self.window.blit(background, (0, 0))

        #text background
        text1_background = self.little_bigger_font.render('Pause', True, (0, 0, 0))

        # declare what will be written
        text1 = self.big_font.render('Pause', True, (179, 20, 58))

        # declare the position of the text
        text1_background_rect = text1_background.get_rect(center=(bounds[0]/2 + 6, bounds[1]/2 - 115))
        text1_rect = text1.get_rect(center=(bounds[0]/2, bounds[1]/2 - 120))

        self.window.blit(text1_background, text1_background_rect)
        self.window.blit(text1, text1_rect)
        pygame.display.update()

class InGameScreen(GameScreens):

    def __init__(self, window, big_font, small_font, snake_pos, apple_pos):
        super().__init__(window, big_font, small_font, little_bigger_font)

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
            
        # print(f'changed_pos: {changed_pos}; new_head != self.food_pos : {new_head != self.food_pos}; new_head: {new_head}; food_pos: {self.food_pos}')

        if new_head != self.prev_food_pos and changed_pos == True:
            self.snake.pop()  # Remove tail
        elif new_head == self.food_pos and changed_pos == True:
            print("ENTREI NA MACA")
        
        self.prev_food_pos = self.food_pos

        # print(self.snake)
        return False  # Game continues
    

    def render(self):

        #background
        self.window.blit(background, (0, 0))

        # draw snake
        for pos in self.snake:
            pygame.draw.rect(self.window, (35, 165, 35), (*pos, block_size - 10, block_size - 10))
        

        #print the apple asset
        self.window.blit(apple_asset, self.food_pos)

        # draw score
        score = len(self.snake) - 2
        score_text = self.small_font.render(f'Score: {score}', True, (179, 20, 58))
        self.window.blit(score_text, (10, 10))

        pygame.display.update()

    def reinit(self):
        self.snake = [(3*block_size, 1*block_size), (2*block_size, 1*block_size)]
        self.food_pos = [((self.apple_pos[3]*4 + self.apple_pos[4]*2 + self.apple_pos[5]*1)*block_size), ((self.apple_pos[0]*4 + self.apple_pos[1]*2 + self.apple_pos[2]*1)*block_size)]
        self.food_eaten = False
