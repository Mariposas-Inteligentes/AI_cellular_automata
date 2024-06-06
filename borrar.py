# Luis Solano, Angie Solís y Emilia Víquez

import argparse
import pygame
import numpy

# Global variables

size = 200
matrix = [[0 for _ in range(size)] for _ in range(size)]
new_vector = [0 for _ in range(size)]
neighborhood = 1
file_path = "./data.txt"

def determine_value(value1, value2, value3, rule):
    new_value = 0
    if (value1 == 1):
        if (value2 == 1):
            if (value3 == 1):
                new_value = rule[0] # 111
            else: # value3 == 0
                new_value = rule[1] # 110
        else: # value2 == 0
            if (value3 == 1):
                new_value = rule[2] # 101
            else: # value3 == 0
                new_value = rule[3] # 100
    else:
        if (value2 == 1):
            if (value3 == 1):
                new_value = rule[4] # 011
            else: # value3 == 0
                new_value = rule[5] # 010
        else: # value2 == 0
            if (value3 == 1):
                new_value = rule[6] # 001
            else: # value3 == 0
                new_value = rule[7] # 000
    return new_value

def algorithm(neighborhood, row, rule):
    global matrix
    global new_vector
    global size
    for i in range(0, size):
        # value2 value1 value3
        value1 = matrix[row][i]
        if (i - neighborhood < 0):
            value2 = matrix[row][size-1]  # last value
            value3 = matrix[row][i+neighborhood]
        elif (i + neighborhood >= size):
            value2 = matrix[row][i-neighborhood]
            value3 = matrix[row][0]  # first value
        else: # no special case
            value2 = matrix[row][i-neighborhood]
            value3 = matrix[row][i+neighborhood]
        new_value = determine_value(value2, value1, value3, rule)

        print("new_value = ", new_value, " values: ", value2, ",", value1, ",", value3)

        new_vector[i] = new_value
        color_pixel(new_value, row, i)
        
def color_pixel(new_value, row, column):
    color = (255, 255, 255)
    if (new_value == 1):
        color = (1, 1, 1)
    pygame.draw.rect(screen, color, pygame.Rect(row + 5, column + 5, 5, 5))
    pygame.display.update()

def main():
    global matrix
    global new_vector
    global screen
    global size

    with open(file_path, 'r') as file:
        data = file.read()
        counter = len(data) -1
        for i in range(0,counter):
            matrix[0][i] = int(data[i])
            
        print(matrix[0])
    
    

    # Regla (de 0 a 255): pasar a binario
    rule_number = int(input("Insert rule: "))

    # Convert the integer to a binary string and remove the '0b' prefix
    binary_representation = bin(rule_number)[2:]

    # Ensure the binary string has exactly 8 digits by padding with leading zeros if necessary
    binary_representation = binary_representation.zfill(8)

    # Convert the binary string to an array of digits
    rule = [int(digit) for digit in binary_representation]
    print("Rule ", rule)


    # Screen configuration
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Cellular automata")
    screen.fill((255, 255, 255))

    can_continue = True

    while(can_continue):
        for i in range(0, size):
            for event in pygame.event.get():
            # Event to quit found, then quit
                if event.type == pygame.QUIT:
                    can_continue = False
                    break

            algorithm(neighborhood, i, rule)
            if i + 1 < size:
                matrix[i+1] = new_vector  # TODO: reescribir
                print(matrix[i+1])
    
    


main()
