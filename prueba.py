import pygame
import numpy as np

# Constants
SIZE = 200
CELL_SIZE = 2  # Smaller cell size for a smaller window
WINDOW_WIDTH = SIZE * CELL_SIZE
WINDOW_HEIGHT = SIZE * CELL_SIZE
NEIGHBORHOOD = 1
FILE_PATH = "./data.txt"

# Function to determine the new cell value
def determine_value(value1, value2, value3, rule):
    index = 4 * value1 + 2 * value2 + value3
    return rule[index]

# Run the automaton algorithm
def algorithm(matrix, rule):
    new_matrix = np.zeros((SIZE, SIZE), dtype=int)
    for row in range(SIZE):
        for col in range(SIZE):
            left = matrix[row][(col - 1) % SIZE]
            center = matrix[row][col]
            right = matrix[row][(col + 1) % SIZE]
            new_matrix[row][col] = determine_value(left, center, right, rule)
    return new_matrix

# Update the pygame display
def update_display(screen, matrix):
    for row in range(SIZE):
        for col in range(SIZE):
            color = (255, 255, 255) if matrix[row][col] == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()

# Main function
def main():
    # Load initial state from file
    matrix = np.zeros((SIZE, SIZE), dtype=int)
    with open(FILE_PATH, 'r') as file:
        data = file.read().strip()
        for i in range(min(SIZE, len(data))):
            matrix[0][i] = int(data[i])

    rule_number = int(input("Insert rule: "))
    rule = [(rule_number >> i) & 1 for i in range(8)][::-1]

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Cellular Automata")

    running = True
    pause = True  # Flag to control the iteration of the automaton
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Press space to iterate the automaton
                    pause = not pause

        if not pause:
            update_display(screen, matrix)
            matrix = algorithm(matrix, rule)

    pygame.quit()

if __name__ == "__main__":
    main()
