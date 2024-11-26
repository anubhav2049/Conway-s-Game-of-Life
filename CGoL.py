import numpy as np
import matplotlib.pyplot as plt
import time
import os
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 50, 50
CELL_SIZE = WIDTH // COLS

ALIVE_COLOR = (0, 255, 0)
DEAD_COLOR = (0, 0, 0)
GRID_COLOR = (40, 40, 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()


def initialize_grid(rows, cols, random_fill=True):
    return np.random.choice([0,1], size=(rows, cols))
      

def count_neighbors(grid, x, y):
    rows, cols = grid.shape
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                total += grid[(x + i) % rows, (y + j) % cols]
    return total


def next_generation(grid):
    rows, cols = grid.shape
    new_grid = np.zeros((rows,cols), dtype=int)
    for x in range(rows):
        for y in range(cols):

            neighbors = count_neighbors(grid, x, y)
            if grid[x,y] == 1 and (neighbors == 2 or neighbors == 3):
                new_grid[x,y] = 1
            elif grid[x,y] == 0 and neighbors == 3:
                new_grid[x,y] = 1
    return new_grid



def draw_grid(screen, grid):
    rows, cols = grid.shape
    for x in range(rows):
        for y in range(cols):
            cell_color = ALIVE_COLOR if grid[x, y] == 1 else DEAD_COLOR
            pygame.draw.rect(screen, cell_color, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GRID_COLOR, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)


def run_simulation(rows, cols):
    grid = initialize_grid(rows, cols)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running =  False

        grid = next_generation(grid)
        screen.fill(DEAD_COLOR)
        draw_grid(screen, grid)
        pygame.display.flip()

        clock.tick(10)

    pygame.quit()


run_simulation(ROWS, COLS)
        