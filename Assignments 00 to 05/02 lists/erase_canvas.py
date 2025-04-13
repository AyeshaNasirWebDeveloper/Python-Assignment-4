from graphics import Canvas
import time

# Canvas settings
WIDTH = 400
HEIGHT = 400

# Sizes for grid cells and the eraser
BOX_SIZE = 40
ERASER_WIDTH = 20

def erase_colored_boxes(canvas, eraser_rect):
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()

    # Define the area the eraser currently covers
    x1 = mouse_x
    y1 = mouse_y
    x2 = x1 + ERASER_WIDTH
    y2 = y1 + ERASER_WIDTH

    # Find all items overlapping the eraser
    touched_items = canvas.find_overlapping(x1, y1, x2, y2)

    for item in touched_items:
        if item != eraser_rect:  # Don't erase the eraser itself
            canvas.set_color(item, 'white')


def main():
    # Setup the canvas
    canvas = Canvas(WIDTH, HEIGHT)

    # Create grid of blue boxes
    for row in range(HEIGHT // BOX_SIZE):
        for col in range(WIDTH // BOX_SIZE):
            x1 = col * BOX_SIZE
            y1 = row * BOX_SIZE
            x2 = x1 + BOX_SIZE
            y2 = y1 + BOX_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, 'blue')

    # Wait for user to click to place the eraser
    canvas.wait_for_click()
    click_x, click_y = canvas.get_last_click()

    # Create a pink eraser at click position
    eraser = canvas.create_rectangle(
        click_x, click_y,
        click_x + ERASER_WIDTH, click_y + ERASER_WIDTH,
        'pink'
    )

    # Move eraser around with the mouse and erase blue boxes
    while True:
        current_x = canvas.get_mouse_x()
        current_y = canvas.get_mouse_y()
        canvas.moveto(eraser, current_x, current_y)

        erase_colored_boxes(canvas, eraser)

        time.sleep(0.05)


if __name__ == '__main__':
    main()
