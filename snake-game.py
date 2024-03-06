import pygame
from pygame.locals import *

import paho.mqtt.client as mqtt
import time

user = "T1BB3"
password = "T1BB3-senha"

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