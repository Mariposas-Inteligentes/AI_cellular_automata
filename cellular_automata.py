# Luis Solano, Angie Solís y Emilia Víquez

import argparse
import pygame
import numpy

can_continue = True
file_or_fixed = input("Digite 1 si desea leer del archivo el estado inicial: ")

# Screen configuration
pygame.init()
size_pygame = 4
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Cellular automata")

clock = pygame.time.Clock()

size = 200
rule = [int(digit) for digit in range(0,8)]


# Variables
matrix = [[0 for _ in range(size)] for _ in range(size)]
file_path = "./data.txt"

def set_rule(rule_number): 
  global rule
  # Calculate rule actual value
  # Convert the integer to a binary string and remove the '0b' prefix
  binary_representation = bin(rule_number)[2:]
  # Ensure the binary string has exactly 8 digits by padding with leading zeros if necessary
  binary_representation = binary_representation.zfill(8)
  # Convert the binary string to an array of digits
  rule = [int(digit) for digit in binary_representation]


def draw_row(row):
  global matrix, size_pygame, screen
  for pixel in range(len(matrix[row])):
    if matrix[row][pixel] == 1:
      pygame.draw.rect(screen,
                       (255, 255, 255),
                      (pixel * size_pygame,
                      row * size_pygame,
                      size_pygame,
                      size_pygame))
    else:
      pygame.draw.rect(screen,
                      (0, 0, 0),
                      (pixel * size_pygame,
                      row * size_pygame,
                      size_pygame,
                      size_pygame))
  pygame.display.flip()


def calculate_value(left, center, right):
  global rule
  index = 4 * left + 2 * center + right
  return rule[index]

def algorithm(to_row):
  global size, rule, matrix, screen
  # Select the row that needs to be taken as reference
  draw_row(to_row)
  from_row = to_row-1
  if to_row == 0:
    from_row = size-1
  
  for col in range(0, size):
    left = matrix[from_row][(col - 1) % size]
    center = matrix[from_row][col]
    right = matrix[from_row][(col + 1) % size]
    matrix[to_row][col] = calculate_value(left, center, right)



set_rule(78)

if (file_or_fixed == '1'):
  # Read the file
  with open(file_path, 'r') as file:
    data = file.read()
    counter = len(data)
    for i in range(0, counter):
      matrix[0][i] = int(data[i])
else:
  # Fijo (no estoy segura si es fijo o periódico): rule 45
  # matrix[0][int(size/2)] = 1
 
  ##  Pruebas que no sé qué son: 
  # Rule 187
  # matrix[0][int(size/4)] = 1

  # Rule 176
  # matrix[0][int(size/3)] = 1

  # Rule 55 (mi compu se murió corriéndola)
  # matrix[0][50] = 1
  matrix[0][100] = 1



first_time = True
screen.fill((0,0,0))

# Calculate results
while(can_continue):
  start = 0
  if first_time:
    start = 1
    first_time = False
  for i in range(start, size):
    clock.tick(60)
    algorithm(i)
    for event in pygame.event.get():
      # Event to quit found, then quit
      if event.type == pygame.QUIT:
        can_continue = False
        break

clock.tick(60)
draw_row(len(matrix[0])-1)
pygame.quit()
  

   

