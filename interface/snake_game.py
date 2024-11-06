from pygame.locals import *
from game_screens import *

import pygame
import serial

from typing import List
from enum import Enum

########################
# Game variables


class GameState(Enum):
    IDLE = [0, 0, 0, 0, 0, 0]
    ESPERA = [0, 0, 0, 1, 0, 0]
    PAUSOU = [0, 0, 1, 0, 1, 1]
    PERDEU = [0, 0, 1, 1, 0, 1]
    GANHOU = [0, 0, 1, 1, 1, 0]

    @classmethod
    def _missing_(cls, _):
        return cls.ESPERA


apple_position = [300, 300]

# binary:
bin_snake_pos: List[int] = [0, 0, 0, 0, 0, 0]
bin_apple_pos: List[int] = [0, 0, 0, 0, 0, 0]
bin_state: List[int] = [0, 0, 0, 0, 0]

# Game settings
bin_vel: List[int] = [0]  # 0 = slow, 1 = fast
bin_mode: List[int] = [0]  # 0 = borderless, 1 = with borders
bin_diff: List[int] = [0]  # 0 = 8 apples to win, 1 = 16 apples to win
########################


def run_states(game_state, prev_state):
    # print(f"prev_state: {prev_state}; current_state: {game_state}")

    match game_state:
        case game_state.IDLE:
            if prev_state != game_state.IDLE:
                screen_controller.in_game_screen.reinit()
                print("REINIT")

            screen_controller.switch_screen(screen_controller.init_screen)
            screen_controller.current_screen.update_Init(
                bin_vel[0], bin_mode[0], bin_diff[0]
            )

        case game_state.ESPERA:
            screen_controller.switch_screen(screen_controller.in_game_screen)
            screen_controller.current_screen.update_snake(bin_apple_pos, bin_snake_pos)

        case game_state.PAUSOU:
            screen_controller.switch_screen(screen_controller.pause_screen)

        case game_state.PERDEU:
            if prev_state != game_state.PERDEU:
                screen_controller.in_game_screen.reinit()
                print("REINIT")

            screen_controller.switch_screen(screen_controller.game_over_screen)

        case game_state.GANHOU:
            if prev_state != game_state.GANHOU:
                screen_controller.in_game_screen.reinit()
                print("REINIT")

            screen_controller.switch_screen(screen_controller.game_won_screen)
            prev_state = game_state.GANHOU

        case _:
            pass


screen_controller = GameScreenController(
    bin_apple_pos, bin_snake_pos, bin_vel, bin_mode, bin_diff
)


def main():
    ser = serial.Serial(
        port="/dev/ttyUSB0",
        baudrate=115200,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.SEVENBITS,
    )

    header = b"\x02"
    end_byte = b"\n"
    size = 4
    msg = []

    print(f"Using serial port {ser.name}")

    running = True

    prev_state = GameState.IDLE

    while running:
        ser.reset_input_buffer()

        current_byte = ser.read()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current_byte != header:
            continue

        msg = []

        for _ in range(size):
            current_byte = ser.read()
            msg.append(current_byte)

        current_byte = ser.read()

        if current_byte == end_byte:
            print(f"Full serial message: {msg}\n")

            # msg[i][0] = i'th byte from the package
            # each byte has only 7 bits instead of 8
            # each byte can represent one big variable or multiple individual bits
            # 

            byte_value = msg[0][0]
            byte_bits = [int(bit) for bit in bin(byte_value)[2:].zfill(7)] # [2:]
            bin_snake_pos[:] = byte_bits[0:6]

            byte_value = msg[1][0]
            byte_bits = [int(bit) for bit in bin(byte_value)[2:].zfill(7)]
            bin_apple_pos[:] = byte_bits[0:6]

            byte_value = msg[2][0]
            byte_bits = [int(bit) for bit in bin(byte_value)[2:].zfill(7)]
            bin_state[:] = byte_bits[0:6]

            byte_value = msg[3][0]
            byte_bits = [int(bit) for bit in bin(byte_value)[2:].zfill(7)]
            bin_diff[0] = byte_bits[1]  
            bin_mode[0] = byte_bits[2]
            bin_vel[0] = byte_bits[3]

        msg = []

        states = GameState(bin_state)
        run_states(states, prev_state)
        prev_state = states

        screen_controller.render_current_screen()


main()
