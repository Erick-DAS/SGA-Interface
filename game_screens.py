import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

########################################
# window values
bounds = (400,400) # grid_size
block_size = 100
window = pygame.display.set_mode(bounds)

# set up fonts
font_path = 'PressStart2P-Regular.ttf'
big_font_size = 60
small_font_size = 30
big_font = pygame.font.Font(font_path, big_font_size)
small_font = pygame.font.Font(font_path, small_font_size)
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

    def render(self):
        self.window.fill((0,0,0))
        pygame.display.update()