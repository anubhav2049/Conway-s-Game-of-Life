import numpy as np
import matplotlib.pyplot as plt
import time
import os

def initialize_grid(rows, cols, random_fill=True):
    if random_fill:
        return np.random.choice([0,1], size=(rows,cols))
    else:
        return np.zeros((rows, cols), dtype=int)
    

def display_grid_with_plot(grid, generation):
    plt.clf()
    plt.imshow(grid, cmap='binary')
    plt.title(f"Generation: {generation}")
    plt.axis('off')
    plt.pause(0.3)    

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



def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(' '.join('█' if cell else ' ' for cell in row))


def run_simulation(rows, cols, generations):
    grid = initialize_grid(rows, cols)
    plt.ion()
    for gen in range(generations):
        display_grid_with_plot(grid, gen)
        grid = next_generation(grid)
    plt.ioff()
    plt.show()


ROWS = 20
COLS = 40
GENERATIONS = 100

run_simulation(ROWS, COLS, GENERATIONS)
        