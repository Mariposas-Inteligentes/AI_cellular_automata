# Luis Solano, Angie Solís y Emilia Víquez

import argparse
import pygame
import numpy

can_continue = True

# Screen configuration
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Cellular automata")
screen.fill((255, 255, 255))
size = 200
rule_number = 40


# Variables
matrix = [[0 for _ in range(size)] for _ in range(size)]
file_path = "./data.txt"
rule = 0


def calculate_value(left, center, right):
  value = 0
  return value

def algorithm(to_row):
  global size, rule, matrix, screen
  # Select the row that needs to be taken as reference
  from_row = to_row-1
  if to_row == 0:
    from_row = size-1
  
  for col in range(0, size):
    left = matrix[from_row][(col - 1) % size]
    center = matrix[from_row][col]
    right = matrix[from_row][(col + 1) % size]
    matrix[to_row][col] = calculate_value(left, center, right)




# Read the file
with open(file_path, 'r') as file:
  data = file.read()
  counter = len(data)
  for i in range(0, counter):
    matrix[0][i] = int(data[i])



# Convert the integer to a binary string and remove the '0b' prefix
binary_representation = bin(rule_number)[2:]
# Ensure the binary string has exactly 8 digits by padding with leading zeros if necessary
binary_representation = binary_representation.zfill(8)
# Convert the binary string to an array of digits
rule = [int(digit) for digit in binary_representation]

while(can_continue):
  for i in range(0, size):
    for event in pygame.event.get():
      # Event to quit found, then quit
      if event.type == pygame.QUIT:
        can_continue = False
        break
   

