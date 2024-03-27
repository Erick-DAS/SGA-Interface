import pygame
from pygame.locals import *
from game_screens import *
from enum import Enum

import paho.mqtt.client as mqtt
import time

user = "T1BB3"
password = "T1BB3-senha"

screen_controller = GameScreenController()

########################
# Game variables
class game_state(Enum):
    IDLE                 = '00000'  # 0
    PREPARA              = '00001' # 1
    GERA_MACA_INICIAL    = '00010'  # 2
    RENDERIZA            = '00011'  # 3
    ESPERA               = '00100'  # 4
    REGISTRA             = '00101'  # 5
    MOVE                 = '00110'  # 6
    COMPARA              = '00111'  # 7
    VERIFICA_MACA        = '01000'  # 8
    CRESCE               = '01001'  # 9
    GERA_MACA            = '01010'  # A
    PAUSOU               = '01011'  # B
    FEZ_NADA             = '01100'  # C
    PERDEU               = '01101'  # D
    GANHOU               = '01110'  # E
    PROXIMO_RENDER       = '01111'  # F
    ATUALIZA_MEMORIA     = '10000'  # G
    ContaRAM             = '10001'  # h
    WriteRAM             = '10010'  # i
    ComparaRAM           = '10011'  # j
    RESETMATRIZ          = '10100'  # k
    COMPARASELF          = '10101'  # l
    CONTASELF            = '10110'  # m
    ATUALIZA_MEMORIASELF = '10111'  # n
    COMPARAMACA          = '11000'  # o
    CONTAMACA            = '11001'  # p
    ATUALIZA_MEMORIAMACA = '11010'  # q
    ZERA_CONTAGEMMACA    = '11011'  # r


apple_position = [300, 300];

# Snake variables
snake_head = [100, 100]
snake = [snake_head, [90, 100], [80, 100]]

# Game settings
difficulty = 0 # 0 = 8 apples to win, 1 = 16 apples to win
mode = 0 # 0 = borderless, 1 = with borders
speed = 0 # 0 = slow, 1 = fast
########################


def run_states(game_state):
    match game_state:
        case IDLE:
                



def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # game_state transition
            

            # Start the game from the initial screen
            if screen_controller.current_screen == screen_controller.init_screen:
                screen_controller.current_screen.handle_input(event)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if screen_controller.current_screen == screen_controller.init_screen:
                    screen_controller.switch_screen(screen_controller.in_game_screen)

                # Restart game from game over screen
                elif screen_controller.current_screen == screen_controller.game_over_screen:
                    screen_controller.switch_screen(screen_controller.init_screen)

            # Handle snake movement keys within the game screen
            if screen_controller.current_screen == screen_controller.in_game_screen:
                screen_controller.current_screen.handle_input(event)

            # Check for pause toggle
            if event.type == pygame.KEYDOWN and (screen_controller.current_screen == screen_controller.in_game_screen or screen_controller.current_screen == screen_controller.pause_screen):
                if event.key == pygame.K_SPACE:
                    if screen_controller.current_screen == screen_controller.in_game_screen:
                        screen_controller.switch_screen(screen_controller.pause_screen)
                    elif screen_controller.current_screen == screen_controller.pause_screen:
                        screen_controller.switch_screen(screen_controller.in_game_screen)
                         
                        continue

        # Update and render the current screen
        if screen_controller.current_screen == screen_controller.in_game_screen:
            game_over = screen_controller.current_screen.update_snake()
            if game_over:
                screen_controller.current_screen.reinit()
                screen_controller.switch_screen(screen_controller.game_over_screen)

        screen_controller.render_current_screen()
        pygame.time.delay(100)

main()



# TODO: Fazer a conexão com o MQTT
# - Pegar os sinais necessários da ESP
# -- Os principais sao as entradas dos botoes