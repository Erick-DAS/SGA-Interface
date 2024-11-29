# game_screens.py

import os
import pygame
from pygame.locals import *
from typing import List

pygame.init()
pygame.font.init()

########################################
# Window values
bounds = (800, 800)  # Grid size
block_size = 100
window = pygame.display.set_mode(bounds)
pygame.display.set_caption('Snake Game')

# Set up fonts
system_path = os.path.dirname(os.path.abspath(__file__))
assets_path = os.path.join(os.path.dirname(system_path), "assets")

font_path = os.path.join(assets_path, "PressStart2P-Regular.ttf")
little_bigger_font_size = 85
big_font_size = 85
small_font_size = 25
little_bigger_font = pygame.font.Font(font_path, little_bigger_font_size)
big_font = pygame.font.Font(font_path, big_font_size)
small_font = pygame.font.Font(font_path, small_font_size)

# Load assets
apple_asset = pygame.image.load(os.path.join(assets_path, "apple_asset.png"))
apple_asset = pygame.transform.scale(apple_asset, (block_size, block_size))

background = pygame.image.load(os.path.join(assets_path, "grass.png"))
background = pygame.transform.scale(background, bounds)

background2 = pygame.image.load(os.path.join(assets_path, "grass_apple.png"))
background2 = pygame.transform.scale(background2, bounds)

snake_head_asset = pygame.image.load(os.path.join(assets_path, "snake_head.png"))
snake_mouth_open_asset = pygame.image.load(os.path.join(assets_path, "snake_mouth_open.png"))
snake_body_asset = pygame.image.load(os.path.join(assets_path, "snake_body.png"))
snake_curve_asset = pygame.image.load(os.path.join(assets_path, "snake_curve.png"))
snake_tail_asset = pygame.image.load(os.path.join(assets_path, "snake_tail.png"))

########################################

class GameScreenController:
    def __init__(self, bin_apple_pos, bin_snake_pos, bin_vel, bin_mode, bin_diff):
        self.window = window
        self.big_font = big_font
        self.small_font = small_font

        # Initialize all screen instances
        self.init_screen = InitScreen(
            window, big_font, small_font, bin_vel, bin_mode, bin_diff
        )
        self.game_over_screen = GameOverScreen(
            window, big_font, small_font, little_bigger_font
        )
        self.game_won_screen = GameWonScreen(
            window, big_font, small_font, little_bigger_font
        )
        self.pause_screen = PauseScreen(
            window, big_font, small_font, little_bigger_font
        )
        self.in_game_screen = InGameScreen(
            window, big_font, small_font, bin_snake_pos, bin_apple_pos
        )

        # Start with the initial screen
        self.current_screen = self.init_screen

    def switch_screen(self, new_screen):
        self.current_screen = new_screen

    def render_current_screen(self):
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
        self.bin_vel = bin_vel
        self.bin_mode = bin_mode
        self.bin_diff = bin_diff
        self.background1_coords = -800
        self.background2_coords = 0

    def render(self):
        velocity = self.bin_vel
        boundary = self.bin_mode
        difficulty = self.bin_diff

        # Background animation
        self.window.blit(background, (int(self.background1_coords), 0))
        self.window.blit(background2, (int(self.background2_coords), 0))

        self.background1_coords += 1
        self.background2_coords += 1

        if self.background1_coords >= 800:
            self.background1_coords = -800

        if self.background2_coords >= 800:
            self.background2_coords = -800

        # Title and options
        title_background_text = self.little_bigger_font.render("S.G.A 2.0", True, (0, 0, 0))
        title_background_rect = title_background_text.get_rect(
            center=(bounds[0] / 2 + 6, bounds[1] / 2 - 115)
        )

        title_text = self.big_font.render("S.G.A 2.0", True, (179, 20, 58))
        title_rect = title_text.get_rect(center=(bounds[0] / 2, bounds[1] / 2 - 120))

        boundary_text = self.small_font.render(
            f"Mode: {'No Border' if boundary == 0 else 'Border'}",
            True,
            (24, 106, 237) if boundary == 0 else (209, 38, 38)
        )
        boundary_rect = boundary_text.get_rect(center=(bounds[0] / 2, bounds[1] / 2))

        difficulty_text = self.small_font.render(
            f"Difficulty: {'Normal' if difficulty == 0 else 'Hard'}",
            True,
            (24, 106, 237) if difficulty == 0 else (209, 38, 38)
        )
        difficulty_rect = difficulty_text.get_rect(center=(bounds[0] / 2, bounds[1] / 2 + 40))

        velocity_text = self.small_font.render(
            f"Speed: {'Normal' if velocity == 0 else 'Fast'}",
            True,
            (24, 106, 237) if velocity == 0 else (209, 38, 38)
        )
        velocity_rect = velocity_text.get_rect(center=(bounds[0] / 2, bounds[1] / 2 + 80))

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
        self.window.blit(background, (0, 0))

        text1_background = self.little_bigger_font.render("Game Over", True, (0, 0, 0))
        text1 = self.big_font.render("Game Over", True, (179, 20, 58))

        text1_background_rect = text1_background.get_rect(
            center=(bounds[0] / 2 + 6, bounds[1] / 2 - 115)
        )
        text1_rect = text1.get_rect(center=(bounds[0] / 2, bounds[1] / 2 - 120))

        self.window.blit(text1_background, text1_background_rect)
        self.window.blit(text1, text1_rect)
        pygame.display.update()

class GameWonScreen(GameScreens):
    def render(self):
        self.window.blit(background, (0, 0))

        text1_background = self.little_bigger_font.render("You Won!", True, (0, 0, 0))
        text1 = self.big_font.render("You Won!", True, (179, 20, 58))

        text1_background_rect = text1_background.get_rect(
            center=(bounds[0] / 2 + 6, bounds[1] / 2 - 115)
        )
        text1_rect = text1.get_rect(center=(bounds[0] / 2, bounds[1] / 2 - 120))

        self.window.blit(text1_background, text1_background_rect)
        self.window.blit(text1, text1_rect)
        pygame.display.update()

class PauseScreen(GameScreens):
    def render(self):
        self.window.blit(background, (0, 0))

        text1_background = self.little_bigger_font.render("Pause", True, (0, 0, 0))
        text1 = self.big_font.render("Pause", True, (179, 20, 58))

        text1_background_rect = text1_background.get_rect(
            center=(bounds[0] / 2 + 6, bounds[1] / 2 - 115)
        )
        text1_rect = text1.get_rect(center=(bounds[0] / 2, bounds[1] / 2 - 120))

        self.window.blit(text1_background, text1_background_rect)
        self.window.blit(text1, text1_rect)
        pygame.display.update()

class InGameScreen(GameScreens):
    def __init__(self, window, big_font, small_font, bin_snake_pos, bin_apple_pos):
        super().__init__(window, big_font, small_font, little_bigger_font)
        self.clock = pygame.time.Clock()

        self.bin_snake_pos = bin_snake_pos
        self.bin_apple_pos = bin_apple_pos

        self.snake = []  # List of positions representing the snake's body
        self.snake_length = 2  # Initial length of the snake

        self.food_pos = self.bits_to_position(self.bin_apple_pos)
        self.prev_food_pos = self.food_pos
        self.food_eaten = False

    def bits_to_position(self, bits: List[int]):
        # Convert 6 bits into x, y coordinates (3 bits each)
        x_bits = bits[3:6]
        y_bits = bits[0:3]
        x = (x_bits[0] * 4 + x_bits[1] * 2 + x_bits[2]) * block_size + block_size // 2
        y = (y_bits[0] * 4 + y_bits[1] * 2 + y_bits[2]) * block_size + block_size // 2
        return [x, y]

    def update_snake(self, bin_apple_pos, bin_snake_pos):
        self.bin_snake_pos = bin_snake_pos
        self.bin_apple_pos = bin_apple_pos

        self.food_pos = self.bits_to_position(self.bin_apple_pos)
        new_head = self.bits_to_position(self.bin_snake_pos)

        # Initialize snake body if empty
        if not self.snake:
            self.snake.append(new_head)
            return

        # Calculate direction based on new head position
        prev_head = self.snake[0]
        if new_head != prev_head:
            self.snake.insert(0, new_head)
            # Check for food collision
            if new_head == self.food_pos:
                self.snake_length += 1  # Increase length
                self.food_eaten = True
                print("Snake ate the food")
            else:
                self.food_eaten = False

            # Trim the snake body to maintain the length
            if len(self.snake) > self.snake_length:
                self.snake.pop()

    def render(self):
        # Background
        self.window.blit(background, (0, 0))

        for pos in self.snake:
            pygame.draw.rect(
                self.window, (35, 165, 35), (*pos, block_size - 10, block_size - 10)
            )

        # Draw the eyes on the snake's head
        if len(self.snake) >= 1:
            head = self.snake[0]
            head_x, head_y = head

            if len(self.snake) > 1:
                neck = self.snake[1]
                # Calculate direction vector from neck to head
                dx = head_x - neck[0]
                dy = head_y - neck[1]
            else:
                # Default direction if only one segment
                dx, dy = 0, -1  # Moving upwards

            # Normalize the direction vector
            length = (dx ** 2 + dy ** 2) ** 0.5
            if length != 0:
                dx /= length
                dy /= length
            else:
                dx, dy = 0, -1  # Default direction

            # Calculate the perpendicular vector for eye positioning
            ex = -dy
            ey = dx

            # Set the distance from the center to the eyes
            eye_distance = (block_size - 10) // 4
            eye_radius = (block_size - 10) // 8

            # Calculate the center of the head
            head_center_x = head_x + (block_size - 10) // 2
            head_center_y = head_y + (block_size - 10) // 2

            # Calculate eye positions
            eye1_x = int(head_center_x + ex * eye_distance + dx * eye_distance)
            eye1_y = int(head_center_y + ey * eye_distance + dy * eye_distance)
            eye2_x = int(head_center_x - ex * eye_distance + dx * eye_distance)
            eye2_y = int(head_center_y - ey * eye_distance + dy * eye_distance)

            # Draw the eyes as red rectangles
            eye_width = eye_radius * 2
            eye_height = eye_radius * 2

            # Create rectangles for the eyes
            eye1_rect = pygame.Rect(
                eye1_x - eye_radius, eye1_y - eye_radius, eye_width, eye_height
            )
            eye2_rect = pygame.Rect(
                eye2_x - eye_radius, eye2_y - eye_radius, eye_width, eye_height
            )

            # Draw the eyes
            pygame.draw.rect(self.window, (255, 0, 0), eye1_rect)
            pygame.draw.rect(self.window, (255, 0, 0), eye2_rect)

        # Draw the apple
        self.window.blit(apple_asset, self.food_pos)

        # Draw score
        score = len(self.snake) - 2
        score_text = self.small_font.render(f"Score: {score}", True, (179, 20, 58))
        self.window.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()



    def reinit(self):
        self.snake_body = []
        self.snake_length = 2
        self.food_pos = self.bits_to_position(self.bin_apple_pos)
        self.food_eaten = False
