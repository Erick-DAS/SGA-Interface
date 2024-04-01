import pygame
from pygame.locals import *
from game_screens import *
from enum import Enum

import paho.mqtt.client as mqtt
import time

user = "Das"
passwd = "12345678"
Broker = "192.168.135.253"
Port = 1883
KeepAlive = 60

namespace = "snake_game"
snake_pos_topic = namespace + "/snake_pos"
apple_pos_topic = namespace + "/apple_pos"
state_topic = namespace + "/state"
comeu_maca_topic = namespace + "/comeu_maca"

########################
# Game variables
class game_state(Enum):
    IDLE                 =  [0, 0, 0, 0, 0]  # 0
    PREPARA              =  [0, 0, 0, 0, 1]  # 1
    GERA_MACA_INICIAL    =  [0, 0, 0, 1, 0]  # 2
    RENDERIZA            =  [0, 0, 0, 1, 1]  # 3
    ESPERA               =  [0, 0, 1, 0, 0]  # 4
    REGISTRA             =  [0, 0, 1, 0, 1]  # 5
    MOVE                 =  [0, 0, 1, 1, 0]  # 6
    COMPARA              =  [0, 0, 1, 1, 1]  # 7
    VERIFICA_MACA        =  [0, 1, 0, 0, 0]  # 8
    CRESCE               =  [0, 1, 0, 0, 1]  # 9
    GERA_MACA            =  [0, 1, 0, 1, 0]  # A
    PAUSOU               =  [0, 1, 0, 1, 1]  # B
    FEZ_NADA             =  [0, 1, 1, 0, 0]  # C
    PERDEU               =  [0, 1, 1, 0, 1]  # D
    GANHOU               =  [0, 1, 1, 1, 0]  # E
    PROXIMO_RENDER       =  [0, 1, 1, 1, 1]  # F
    ATUALIZA_MEMORIA     =  [1, 0, 0, 0, 0]  # G
    ContaRAM             =  [1, 0, 0, 0, 1]  # h
    WriteRAM             =  [1, 0, 0, 1, 0]  # i
    ComparaRAM           =  [1, 0, 0, 1, 1]  # j
    RESETMATRIZ          =  [1, 0, 1, 0, 0]  # k
    COMPARASELF          =  [1, 0, 1, 0, 1]  # l
    CONTASELF            =  [1, 0, 1, 1, 0]  # m
    ATUALIZA_MEMORIASELF =  [1, 0, 1, 1, 1]  # n
    COMPARAMACA          =  [1, 1, 0, 0, 0]  # o
    CONTAMACA            =  [1, 1, 0, 0, 1]  # p
    ATUALIZA_MEMORIAMACA =  [1, 1, 0, 1, 0]  # q
    ZERA_CONTAGEMMACA    =  [1, 1, 0, 1, 1]  # r


apple_position = [300, 300]

# binary:
bin_snake_pos = [0, 0, 0, 0, 0, 0]
bin_apple_pos = [0, 0, 0, 0, 0, 0]
bin_state = [0, 0, 0, 0, 0]

comeu_maca = False

# Game settings
difficulty = 0 # 0 = 8 apples to win, 1 = 16 apples to win
mode = 0 # 0 = borderless, 1 = with borders
speed = 0 # 0 = slow, 1 = fast
########################

def on_connect(client, userdata, flags, rc):
    print("Conectado com codigo " + str(rc))
    client.subscribe(snake_pos_topic, qos=0) 
    print(f'Conectado ao topico {snake_pos_topic}')

    client.subscribe(apple_pos_topic, qos=0) 
    print(f'Conectado ao topico {apple_pos_topic}')
    
    client.subscribe(state_topic, qos=0) 
    print(f'Conectado ao topico {state_topic}')
    
    client.subscribe(comeu_maca_topic, qos=0) 
    print(f'Conectado ao topico {comeu_maca_topic}')

# Quando receber uma mensagem (Callback de mensagem)
def on_message(client, userdata, msg):

    # print(f'Estou recebendo mensagem do topico {str(msg.topic)}')
    if (str(msg.topic) == snake_pos_topic):
        msg_string = str(msg.payload.decode("utf-8"))
        print(f'A mensagem eh snake_pos = "{msg_string}"')

        for i in range(0, len(msg_string)):
            bin_snake_pos[i] = int(msg_string[i])

    elif (str(msg.topic) == apple_pos_topic):
        msg_string = str(msg.payload.decode("utf-8"))
        # print(f'A mensagem eh apple_pos = "{msg_string}"')

        for i in range(0, len(msg_string)):
            bin_apple_pos[i] = int(msg_string[i])

    elif (str(msg.topic) == state_topic):
        msg_string = str(msg.payload.decode("utf-8"))
        # print(f'A mensagem eh state = "{msg_string}"')

        for i in range(0, len(msg_string)):
            bin_state[i] = int(msg_string[i])
    
    elif (str(msg.topic) == comeu_maca_topic):
        msg_string = str(msg.payload.decode("utf-8"))
        # print(f'A mensagem eh comeu_maca = "{msg_string}"')

        comeu_maca = bool(int(msg_string))

    else:
        print("Erro! Mensagem recebida de tópico estranho")

def run_states(game_state):
    match game_state:

        case game_state.IDLE :
            screen_controller.switch_screen(screen_controller.init_screen)

        case game_state.ESPERA :
            screen_controller.switch_screen(screen_controller.in_game_screen)

        case game_state.PAUSOU :
            screen_controller.switch_screen(screen_controller.pause_screen)
        
        case game_state.PERDEU :
            screen_controller.current_screen.reinit()
            screen_controller.switch_screen(screen_controller.game_over_screen)

        case game_state.GANHOU :
            screen_controller.current_screen.reinit()
            screen_controller.switch_screen(screen_controller.game_won_screen)

        case _ :
            print(game_state)
                


screen_controller = GameScreenController(bin_apple_pos, bin_snake_pos)

def main():
    running = True

    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)            
    client.on_connect = on_connect      
    client.on_message = on_message  

    client.username_pw_set(user, passwd)

    client.connect(Broker, Port, KeepAlive)

    client.loop_start() 

    states = game_state(bin_state)
    
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # game_state transitions
            run_states(states)

        screen_controller.render_current_screen()
        pygame.time.delay(100)
main()



# TODO: Fazer a conexão com o MQTT
# - Pegar os sinais necessários da ESP
# -- Os principais sao as entradas dos botoes