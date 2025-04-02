import pygame

'''
Initialize game
'''
pygame.init()

# Set video mode FIRST
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

'''
Load Sprite Sheet
'''
sprite_sheet = pygame.image.load('Assets/UIassetsDemo(3x).png').convert_alpha()

'''
Function to pull a sprite from the sheet
'''


def get_sprite(sheet, col, row, width, height):
    """
    Extracts a specific sprite from a sprite sheet.

    :param sheet: The loaded sprite sheet.
    :param col: The column index of the sprite (starting from 0).
    :param row: The row index of the sprite (starting from 0).
    :param width: The width of each sprite.
    :param height: The height of each sprite.
    :return: The extracted sprite as a pygame.Surface.
    """
    # Create a new transparent surface
    sprite = pygame.Surface((width, height), pygame.SRCALPHA)

    # Calculate the position of the sprite in the sheet
    x = col * width
    y = row * height

    # Blit the sprite from the sheet onto the new surface
    sprite.blit(sheet, (0, 0), (x, y, width, height))

    return sprite


'''
Pull a sprite and store it in a list
'''
sprite_width = 48  # Width of each sprite
sprite_height = 48  # Height of each sprite
num_sprites = 9  # Number of sprites in the sheet

'''
List of all window sprites
'''
# make a list of all windows
window = [[get_sprite(sprite_sheet, i, j, sprite_width, sprite_height)
            for i in range(num_sprites)] for j in range(num_sprites)]
# lay them from 2D to 1D for ease of use
window1 = [item for sublist in window for item in sublist]

'''
Display sprites in game loop window
'''
running = True
current_sprite = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # set a pixel size (Length/Height)
    l, h = 48, 48

    # Display window 1
    [screen.blit(window1[i], (l * i, h)) for i in range(3)]
    [screen.blit(window1[i + 9], (l * i, h*2)) for i in range(3)]
    [screen.blit(window1[i + 18], (l * i, h*3)) for i in range(3)]
    # Display window 2
    [screen.blit(window1[i + 3], ((l * 3) + (l * i), h)) for i in range(3)]
    [screen.blit(window1[i + 12], ((l * 3) + (l * i), h * 2)) for i in range(3)]
    [screen.blit(window1[i + 21], ((l * 3) + (l * i), h * 3)) for i in range(3)]
    # Display window 3
    [screen.blit(window1[i + 6], ((l * 6) + (l * i), h)) for i in range(3)]
    [screen.blit(window1[i + 15], ((l * 6) + (l * i), h * 2)) for i in range(3)]
    [screen.blit(window1[i + 24], ((l * 6) + (l * i), h * 3)) for i in range(3)]

    '''
    Displaying a modular window:
    Adjusting the length and height can stretch the window as needed
    '''
    # Display a long window left edge
    screen.blit(window1[0], (0, h * 4))
    screen.blit(window1[9], (0, h * 5))
    screen.blit(window1[18], (0, h * 6))
    # Display long window center
    [screen.blit(window1[1], (l * i, h * 4)) for i in range(1, 8)]
    [screen.blit(window1[10], (l * i, h * 5)) for i in range(1, 8)]
    [screen.blit(window1[19], (l * i, h * 6)) for i in range(1, 8)]
    # Display long window right edge
    screen.blit(window1[2], (l * 8, h * 4))
    screen.blit(window1[11], (l * 8, h * 5))
    screen.blit(window1[20], (l * 8, h * 6))



    # Update the sprite (simple animation)
    # current_sprite = (current_sprite + 1) % num_sprites

    pygame.display.flip()
    clock.tick(2)  # Control the frame rate

'''
Exit game
'''
pygame.quit()
