from Board import Board
import pygame as p
from pygame.locals import *
import random

WIDTH = HEIGHT = 512
DIMENSION = 10
IMAGES = {}
SCALE = HEIGHT // DIMENSION
MAX_FPS = 30


class snake():
    def __init__(self):
        self.length = 1
        self.positions = [((DIMENSION /2 ), (DIMENSION/2),)]
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        self.colour =  p.Color("dark green")

    def get_head_pos(self):
        return self.positions[0]

    def turn(self, point):
        if(self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction):
            return
        else:
            self.direction = point

    def move(self):
        current = self.get_head_pos()



def load_images():
    board = Board(5,5)

    for i in range(board.x):
        IMAGES[i] = p.transform.scale(p.image.load('res/gray.png'), (SCALE, SCALE))



def main():
    p.init()

    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("black "))
    board = Board(DIMENSION, DIMENSION)

    snake = snake()

    load_images() #only do this once
    running = True

    score = 0
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        draw_game_state(screen, board)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for graphics in the game
'''
def draw_game_state(screen, gs):
    draw_board(screen)
    draw_snake(screen, gs.board)


def draw_board(screen):
    colors = [p.Color('White'), p.Color('Black')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c) % 2]
            p.draw.rect(screen, color, p.Rect(c*SCALE, r*SCALE, SCALE, SCALE))

def draw_snake(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            if(board[r][c].head == True or board[r][c].body == True):
                p.draw.rect(screen, p.Color("dark green"), p.Rect(c*SCALE, r*SCALE, SCALE, SCALE))


if __name__ == "__main__":
    main()