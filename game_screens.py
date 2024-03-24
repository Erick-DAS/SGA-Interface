import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

bounds = (400,400) # grid_size
block_size = 100
window = pygame.display.set_mode(bounds)

# set up fonts
font_path = 'PressStart2P-Regular.ttf'
big_font_size = 60
small_font_size = 30
big_font = pygame.font.Font(font_path, big_font_size)
small_font = pygame.font.Font(font_path, small_font_size)


def init_screen():
    window.fill((0,0,0))
    # declare what will be written
    text1 = big_font.render('S.G.A', True, (255,255,255))
    text2 = small_font.render('Jogar', True, (255,255,255))
    # declare the position of the text
    text1_rect = text1.get_rect(center=(bounds[0]/2, bounds[1]/2 - 120))
    text2_rect = text2.get_rect(center=(bounds[0]/2, bounds[1]/2 + 60))

    window.blit(text1, text1_rect)
    window.blit(text2, text2_rect)
    pygame.display.update()

def game_over_screen():
    window.fill((0,0,0))
    # declare what will be written
    text1 = big_font.render('Game Over', True, (255,255,255))

    # declare the position of the text
    text1_rect = text1.get_rect(center=(bounds[0]/2, bounds[1]/2 - 120))

    window.blit(text1, text1_rect)
    pygame.display.update()


def game_won_screen():
    window.fill((0,0,0))
    # declare what will be written
    text1 = big_font.render('Ganhou!', True, (255,255,255))

    # declare the position of the text
    text1_rect = text1.get_rect(center=(bounds[0]/2, bounds[1]/2 - 120))

    window.blit(text1, text1_rect)
    pygame.display.update()

def pause_screen():
    window.fill((0,0,0))
    # declare what will be written
    text1 = big_font.render('Pause', True, (255,255,255))

    # declare the position of the text
    text1_rect = text1.get_rect(center=(bounds[0]/2, bounds[1]/2 - 120))

    window.blit(text1, text1_rect)
    pygame.display.update()

def in_game_screen():
    # screen used during game
    window.fill((0,0,0))