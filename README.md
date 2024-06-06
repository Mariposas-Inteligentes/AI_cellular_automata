# *Pygame Tutorial for Beginners - Python Game Development Course*

Code produced whilst following the following [freeCodeCamp tutorial](https://www.youtube.com/watch?v=FfWpgLFMI7w&ab_channel=freeCodeCamp.org)

*Notes taken by:* Luis Solano

## *Summary*

### *Creating a window*

To create a game utilizing pygame functions, the module must be imported and initialized with the following code

    import pygame
    pygame.init()

Once imported, to create a window you must write the following code

    screen = pygame.display.set_mode((WIDTH_VALUE, HEIGHT_VALUE))

Where HEIGHT_VALUE represents the height of the window and WIDTH_VALUE represents the width of the window.

### *Window title*

To change the name of the window is as simple as executing

    pygame.display.set_caption(WINDOW_NAME)

Where WINDOW_NAME represents the title of the window as a string. For example, "Space Invaders"

### *Window icon*

A window icon can be set using a 32x32 image. The image first must be loaded and then set, to do so the following code can be executed

    icon = pygame.image.load(IMAGE_DIR)
    pygame.display.set_icon(icon)

Where IMAGE_DIR represents the direction where the image is stored in your computer. For example 'img/ufo.png'

### *Initial game loop*

For the game not to end instantly, there must be a game loop in the code. To do so, a while True loop can be utilized, ending once the quit event is received.

    # Game loop
    # Variable needed for while true loop
    continue_running = True
    while continue_running:
    # For loop to go through all events in pygame
    for event in pygame.event.get():
      # Event to quit found, then quit
      if event.type == pygame.QUIT:
        continue_running = False

Inside the while loop, a for loop is placed to go through al pygame events. Once pygame.QUIT is reached by the loop, the while true loop must be broken.

### *Screen color and display update*

To set the window a certain color, inside the game loop (while true) the following code must be executed

    screen.fill((FIRST_VALUE, SECOND_VALUE, THIRD_VALUE))
    pygame.display.update()

Where FIRST_VALUE, SECOND_VALUE and THIRD_VALUE represent an integer RGB value to choose the color. After this the screen must be updated.

### *Adding images to the game*

The image must be loaded onto a variable and it also requires and x and y value. To do so you can use the following code as an example

    # Player image
    player_image = pygame.image.load('img/ship.png')
    # Player coordinates
    player_x = 370
    player_y = 480

After it is loaded you will want the game to show the image every frame, to do so you use the function screen.blit() which requires the loaded image, the x value and the y value

    # Player function to draw a ship
    def player():
    screen.blit(player_image, (player_x, player_y))

Inside the game loop the player loop should be called AFTER the screen.fill at the end of the function and BEFORE the display update.

### *Movement and keyboard presses*

To handle movement of a player, you need to alter the value of the x and y values each time a key is pressed, and once the key is released the value must be changed to 0.

1. To go left, you substract from the x value

2. To go right you add to it.

3. To go up you substract from the y value.

4. To go down you add to it.

To find which key was pressed, in the *event for* you can check

    if event.type == pygame.KEYDOWN:

and then go to the respective key to input the desired result by checking the event key with the desired key. For example, if there was a KEYDOWN and you want to check the left arrow you will check

    if event.key == pygame.K_LEFT:

### *Screen borders for characters*

To avoid characters leaving the screen, once either the x or y values reach 0 a condition must be met to reset the value. For the opposite case, the x and y values must be less than

    COORDINATE_SIZE - CHARACTER_SIZE

Otherwise, the coordinate value must be changed to the COORDINATE_SIZE

For example, with a spaceship that has a 64x64 size and an x coordinate with a max value of 800

    # If condition to check borders
    if player_x <= 0:
        player_x = 0
    # 800 - 674 = 736 to avoid any part of the spaceship leaving
    elif player_x >= 736:
        player_x = 736