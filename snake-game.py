import pygame
from pygame.locals import *
from snake import Snake
from game_screens import *

import paho.mqtt.client as mqtt
import time

user = "T1BB3"
password = "T1BB3-senha"


def main():
    running = True
    while running:
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False

        #game states
        init_screen()
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