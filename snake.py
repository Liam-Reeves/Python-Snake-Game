from tkinter import *
import tkinter as tk
import random
import pygame
import sys

pygame.init()

# from tkinter import colorchooser
# def choose_color():
#     color = colorchooser.askcolor()
#     print("Selected color:", color)

# red = (255, 0, 0)
# green = (0, 255, 0)
# black = (0, 0, 0)
GAME_WIDTH = 700

GAME_HEIGHT = 700

SPEED = 50

SPACE_SIZE = 50

BODY_PARTS = 3

SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"


# class Snake:
#     class Food:
#
#      def __int__(self):
#         x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
#         y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
#
#         self.coordinates = [x, y]
#
#         canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR,)
class Snake:
    def __int__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)


# Program imekataa kutoka hapa mazee need help.....


class Food:
    def __int__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR,)


def next_turn():
    pass


def change_direction(new_direction):
    pass


def check_collisions():
    pass


def game_over():
    pass


window = Tk()

window.title("Snake game")
# window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()

food = Food()

window.mainloop()
