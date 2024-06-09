# Cellular automata

## Requirements

The library `pygame` is required for this script.

To install it, execute in a terminal the following command:

    pip install pygame

## Execution instructions

To execute this program, open a terminal and execute the following command:

    python cellular_automata.py

Then, the terminal will show:

    pygame 2.5.1 (SDL 2.28.2, Python 3.11.9)
    Hello from the pygame community. https://www.pygame.org/contribute.html
    To read the initial state from a file, type 1: 

By typing `1` the initial state will be read from `./data.txt`. Otherwise, the default initial state will be used.

After that, a screen will pop and show the automata.

When the screen is closed, the terminal will print the quantity of finished iterations:

    Completed iterations:  4599


**Important notes:**
1. To change the rule, modify the line:

        set_rule(90)

2. To change the file path, modify the line:

        file_path = "./data.txt"


## Authors
Luis David Solano Santamaría

Angie Sofía Solís Manzano

Emilia María Víquez Mora