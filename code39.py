import numpy as np

def initialize_grid(size):
    return np.full((size, size), ' ')

def print_grid(grid):
    size = len(grid)
    for i in range(size):
        for j in range(size):
            print(grid[i][j], end=' ')
        print()

def place_word_horizontal(grid, word, row, col):
    for i, letter in enumerate(word):
        grid[row][col + i] = letter

def place_word_vertical(grid, word, row, col):
    for i, letter in enumerate(word):
        grid[row + i][col] = letter

def can_place_word_horizontal(grid, word, row, col):
    size = len(grid)
    word_len = len(word)
    if col + word_len > size:
        return False
    for i, letter in enumerate(word):
        if grid[row][col + i] != ' ' and grid[row][col + i] != letter:
            return False
    return True

def can_place_word_vertical(grid, word, row, col):
    size = len(grid)
    word_len = len(word)
    if row + word_len > size:
        return False
    for i, letter in enumerate(word):
        if grid[row + i][col] != ' ' and grid[row + i][col] != letter:
            return False
    return True

def solve_crossword(grid, words):
    size = len(grid)
    for word in words:
        word_len = len(word)
        for i in range(size):
            for j in range(size):
                if can_place_word_horizontal(grid, word, i, j):
                    place_word_horizontal(grid, word, i, j)
                    return True
                elif can_place_word_vertical(grid, word, i, j):
                    place_word_vertical(grid, word, i, j)
                    return True
    return False

# Example usage:
if __name__ == "__main__":
    grid_size = 5
    grid = initialize_grid(grid_size)

    words = ["hello", "world", "python", "crossword", "code"]

    if solve_crossword(grid, words):
        print("Crossword puzzle solved!")
        print_grid(grid)
    else:
        print("Could not solve the crossword puzzle.")
