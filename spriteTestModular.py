import pygame

# Load Sprite Sheet
sprite_sheet = pygame.image.load('Assets/UIassetsDemo(3x).png').convert_alpha()

# Font settings
pygame.font.init()
font = pygame.font.Font(None, 32)  # Default font, size 32

# Function to extract sprite from sheet
def get_sprite(sheet, col, row, width, height):
    """ Extracts a specific sprite from the sheet. """
    sprite = pygame.Surface((width, height), pygame.SRCALPHA)
    x, y = col * width, row * height
    sprite.blit(sheet, (0, 0), (x, y, width, height))
    return sprite

# Function to get window UI elements
def get_window_sprites(window_type):
    sprite_width, sprite_height = 48, 48
    col_offset = window_type * 3

    return {
        "corner_tl": get_sprite(sprite_sheet, col_offset + 0, 0, sprite_width, sprite_height),
        "edge_top": get_sprite(sprite_sheet, col_offset + 1, 0, sprite_width, sprite_height),
        "corner_tr": get_sprite(sprite_sheet, col_offset + 2, 0, sprite_width, sprite_height),

        "edge_left": get_sprite(sprite_sheet, col_offset + 0, 1, sprite_width, sprite_height),
        "center": get_sprite(sprite_sheet, col_offset + 1, 1, sprite_width, sprite_height),
        "edge_right": get_sprite(sprite_sheet, col_offset + 2, 1, sprite_width, sprite_height),

        "corner_bl": get_sprite(sprite_sheet, col_offset + 0, 2, sprite_width, sprite_height),
        "edge_bottom": get_sprite(sprite_sheet, col_offset + 1, 2, sprite_width, sprite_height),
        "corner_br": get_sprite(sprite_sheet, col_offset + 2, 2, sprite_width, sprite_height),
    }

# Function to wrap text
def wrap_text(text, max_width):
    """ Splits text into multiple lines so it fits within max_width. """
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines

# Function to draw a text window
def draw_text_window(surface, x, y, cols, rows, window_type=0, text=""):
    sprite_width, sprite_height = 48, 48
    sprites = get_window_sprites(window_type)

    # Draw top row
    surface.blit(sprites["corner_tl"], (x, y))
    for i in range(1, cols - 1):
        surface.blit(sprites["edge_top"], (x + i * sprite_width, y))
    surface.blit(sprites["corner_tr"], (x + (cols - 1) * sprite_width, y))

    # Draw middle rows
    for j in range(1, rows - 1):
        surface.blit(sprites["edge_left"], (x, y + j * sprite_height))
        for i in range(1, cols - 1):
            surface.blit(sprites["center"], (x + i * sprite_width, y + j * sprite_height))
        surface.blit(sprites["edge_right"], (x + (cols - 1) * sprite_width, y + j * sprite_height))

    # Draw bottom row
    surface.blit(sprites["corner_bl"], (x, y + (rows - 1) * sprite_height))
    for i in range(1, cols - 1):
        surface.blit(sprites["edge_bottom"], (x + i * sprite_width, y + (rows - 1) * sprite_height))
    surface.blit(sprites["corner_br"], (x + (cols - 1) * sprite_width, y + (rows - 1) * sprite_height))

    # Define text area
    text_x = x + sprite_width  # Left padding
    text_y = y + sprite_height  # Top padding
    text_width = (cols - 2) * sprite_width  # Width for text
    text_height = (rows - 2) * sprite_height  # Height for text

    # Wrap text to fit inside the window
    wrapped_lines = wrap_text(text, text_width)

    # Render each line inside the text area
    for i, line in enumerate(wrapped_lines):
        text_surface = font.render(line, True, (255, 255, 255))  # White text
        line_height = font.get_height()
        text_position = (text_x, text_y + i * line_height)
        if text_y + i * line_height < y + (rows - 1) * sprite_height:  # Ensure it stays inside
            surface.blit(text_surface, text_position)


if __name__ == "__main__":
    pygame.init()


    def set_window_size(width, height):
        """ Sets the game window to the specified width and height. """
        return pygame.display.set_mode((width, height))


    # Define modular window size
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    screen = set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)
    clock = pygame.time.Clock()
    # Game Loop
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill((0, 0, 0))

        # Draw text windows with text
        draw_text_window(screen, 100, 100, 5, 4, window_type=0, text="Hello! This is a sample text window.")
        draw_text_window(screen, 150, 300, 7, 5, window_type=1, text="Different window type, more text inside.")
        draw_text_window(screen, 500, 100, 4, 6, window_type=2, text="A tall text box that can fit more.")

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
