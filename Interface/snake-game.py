import pygame
from pygame.locals import *
from game_screens import *
from enum import Enum

import paho.mqtt.client as mqtt

user = "Das"
passwd = "12345678"
Broker = "192.168.135.253"
Port = 1883
KeepAlive = 60

namespace = "snake_game"
snake_pos_topic = namespace + "/snake_pos"
apple_pos_topic = namespace + "/apple_pos"
state_topic = namespace + "/state"
vel_selector_topic = namespace + "/vel_selector"
mode_selector_topic = namespace + "/mode_selector"
diff_selector_topic = namespace + "/diff_selector"
########################
# Game variables
class game_state(Enum):
    IDLE                 =  [0, 0, 0, 0, 0]  # 0
    ESPERA              =  [0, 0, 1, 0, 0]  # 1
    PAUSOU               =  [1, 1, 0, 1, 0]  # B
    PERDEU               =  [1, 0, 1, 1, 0]  # D
    GANHOU               =  [0, 1, 1, 1, 0]  # E

    @classmethod
    def _missing_(cls, value):
        return cls.ESPERA
    


apple_position = [300, 300]

# binary:
bin_snake_pos = [0, 0, 0, 0, 0, 0]
bin_apple_pos = [0, 0, 0, 0, 0, 0]
bin_state = [0, 0, 0, 0, 0] 

# Game settings
bin_vel = [0]   # 0 = 8 apples to win, 1 = 16 apples to win
bin_mode = [0]  # 0 = borderless, 1 = with borders
bin_diff = [0]  # 0 = slow, 1 = fast
########################

def on_connect(client, userdata, flags, rc):
    print("Conectado com codigo " + str(rc))
    client.subscribe(snake_pos_topic, qos=0) 
    print(f'Conectado ao topico {snake_pos_topic}')

    client.subscribe(apple_pos_topic, qos=0) 
    print(f'Conectado ao topico {apple_pos_topic}')
    
    client.subscribe(state_topic, qos=0) 
    print(f'Conectado ao topico {state_topic}')

    client.subscribe(vel_selector_topic, qos=0) 
    print(f'Conectado ao topico {vel_selector_topic}')

    client.subscribe(mode_selector_topic, qos=0) 
    print(f'Conectado ao topico {mode_selector_topic}')

    client.subscribe(diff_selector_topic, qos=0)
    print(f'Conectado ao topico {diff_selector_topic}')    

# Quando receber uma mensagem (Callback de mensagem)
def on_message(client, userdata, msg):

    # print(f'Estou recebendo mensagem do topico {str(msg.topic)}')
    if (str(msg.topic) == snake_pos_topic):
        msg_string = str(msg.payload.decode("utf-8"))
        # print(f'A mensagem eh snake_pos = "{msg_string}"')

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

    elif (str(msg.topic) == vel_selector_topic):
        msg_string = str(msg.payload.decode("utf-8"))
        print(f'A mensagem eh bin_vel = "{msg_string}"')

        bin_vel[0] = int(msg_string)

    elif (str(msg.topic) == mode_selector_topic):
        msg_string = str(msg.payload.decode("utf-8"))
        print(f'A mensagem eh bin_mode = "{msg_string}"')

        bin_mode[0] = int(msg_string)

    elif (str(msg.topic) == diff_selector_topic):
        msg_string = str(msg.payload.decode("utf-8"))
        print(f'A mensagem eh bin_diff = "{msg_string}"')

        bin_diff[0] = int(msg_string)

    
    else:
        print("Erro! Mensagem recebida de tópico estranho")



def run_states(game_state, prev_state):
    num_espera = 0
     
    print(f'prev_state: {prev_state}; current_state: {game_state}')

    match game_state:

        case game_state.IDLE :
            if prev_state != game_state.IDLE:
                screen_controller.in_game_screen.reinit()
                print("REINIT")
            
            screen_controller.switch_screen(screen_controller.init_screen)
            screen_controller.current_screen.update_Init(bin_vel[0], bin_mode[0], bin_diff[0])

        case game_state.ESPERA :         
            screen_controller.switch_screen(screen_controller.in_game_screen)
            screen_controller.current_screen.update_snake(bin_apple_pos, bin_snake_pos)

        case game_state.PAUSOU :
            screen_controller.switch_screen(screen_controller.pause_screen)

        
        case game_state.PERDEU :
            if prev_state != game_state.PERDEU:
                screen_controller.in_game_screen.reinit()
                print("REINIT")

            screen_controller.switch_screen(screen_controller.game_over_screen)



        case game_state.GANHOU :
            if prev_state != game_state.GANHOU:
                screen_controller.in_game_screen.reinit()
                print("REINIT")

            screen_controller.switch_screen(screen_controller.game_won_screen)
            prev_state = game_state.GANHOU


        case _ :
            pass
            #print(game_state)
                


screen_controller = GameScreenController(bin_apple_pos, bin_snake_pos, bin_vel, bin_mode, bin_diff)

def main():
    running = True

    # WARNING: If you can't run this file because of API version problems, comment the following line and uncomment the next one  
    client = mqtt.Client()
    # client = mqtt.Client(callback_api_version = mqtt.CallbackAPIVersion.VERSION1)            
    
    
    client.on_connect = on_connect      
    client.on_message = on_message  

    client.username_pw_set(user, passwd)

    client.connect(Broker, Port, KeepAlive)

    client.loop_start() 

    prev_state = game_state.IDLE
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        states = game_state(bin_state)
        # game_state transitions                
        run_states(states, prev_state)
        # print(bin_state)
        prev_state = states
        print(f'bin_vel: {bin_vel}; bin_mode: {bin_mode}; bin_diff: {bin_diff}')
        

        screen_controller.render_current_screen()
main()



# TODO: Fazer a conexão com o MQTT
# - Pegar os sinais necessários da ESP
# -- Os principais sao as entradas dos botoes