from Board import Board
import pygame as p
from pygame.locals import *

WIDTH = HEIGHT = 512
DIMENSION = 20
IMAGES = {}
SCALE = HEIGHT // DIMENSION
MAX_FPS = 30

def load_images():
    board = Board(5,5)

    for i in range(board.x):
        IMAGES[i] = p.transform.scale(p.image.load('res/gray.png'), (SCALE, SCALE))



def main():
    p.init()

    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("black "))
    gs = Board(DIMENSION, DIMENSION)
    print(gs.board)
    load_images() #only do this once
    running = True

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        draw_game_state(screen, gs )
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for graphics in the game
'''
def draw_game_state(screen, gs):
    draw_board(screen)
    draw_nodes(screen, gs.board)


def draw_board(screen):
    colors = [p.Color('White'), p.Color('Black')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c) % 2]
            p.draw.rect(screen, color, p.Rect(c*SCALE, r*SCALE, SCALE, SCALE))

def draw_nodes(screen, board):
    pass

if __name__ == "__main__":
    main()