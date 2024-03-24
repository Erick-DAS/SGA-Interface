import pygame
from pygame.locals import *
from snake import Snake
from game_screens import *

import paho.mqtt.client as mqtt
import time

user = "T1BB3"
password = "T1BB3-senha"

screen_controller = GameScreenController()

########################
# Snake variables
game_state = 0 # 0 = init, 1 = in_game, 2 = game over, 3 = pause
direction = 'right' # Initial direction

########################
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Start the game from the initial screen
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



# TODO: Criar uma função para cada uma das telas:
# - Inicio
# -- Tem que ter o botao "jogar" que leva pra tela do game. Premite também fechar a janela
# - Perdeu
# -- Tela simples com "perdeu" escrito na tela. Permite voltar para a tela inicial ou fechar a janela
# - Ganhou
# -- Tela simples com "ganhou" escrito na tela. Permite voltar para a tela inicial ou fechar a janela 
# - Pausa
# -- Tela simples que permite despausar o game, voltar para a tela inicial ou fechar a janela
# - Tela do game em si
# -- Pode levar a qualquer uma das outras telas

# TODO: Fazer a conexão com o MQTT
# - Pegar os sinais necessários da ESP
# -- Os principais sao as entradas dos botoes