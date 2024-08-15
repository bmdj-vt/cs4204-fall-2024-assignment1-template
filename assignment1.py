from screen import Screen

import numpy as np

def line_1():
    WIDTH =  500
    HEIGHT = 500

    COLOR1 = (255, 0, 0)
    COLOR2 = (0, 0, 0)

    screen = Screen(WIDTH, HEIGHT)

    image_buffer = np.full((HEIGHT, WIDTH, 3), COLOR2)

    a = np.array([(25,40)])
    b = np.array([(400,120)])

    screen.draw_line(a,b,COLOR1,image_buffer)

    screen.show()

def line_2():
    WIDTH  = 500
    HEIGHT = 500

    COLOR1 = (255, 0, 0)
    COLOR2 = (0, 0, 0)

    screen = Screen(WIDTH, HEIGHT)

    image_buffer = np.full((HEIGHT, WIDTH, 3), COLOR2)

    a = np.array([(25,40)])
    b = np.array([(75,400)])

    screen.draw_line(a,b,COLOR1,image_buffer)

    screen.show()

def lines_1():
    WIDTH  = 500
    HEIGHT = 500

    COLOR1 = (255, 0, 0)
    COLOR2 = (0, 0, 0)

    screen = Screen(WIDTH, HEIGHT)

    image_buffer = np.full((HEIGHT, WIDTH, 3), COLOR2)

    a = np.array([(25,100),(225,230),(120,30)])
    b = np.array([(225,230),(120,30),(25,100)])

    screen.draw_line(a,b,COLOR1,image_buffer)

    screen.show()

def lines_2():
    WIDTH  = 500
    HEIGHT = 500

    COLOR1 = (255, 0, 0)
    COLOR2 = (0, 0, 0)

    screen = Screen(WIDTH, HEIGHT)

    image_buffer = np.full((HEIGHT, WIDTH, 3), COLOR2)

    a = np.array([(225,40),(225,160),(480,165),(270,125),(270,80)])
    b = np.array([(225,160),(480,165),(270,125),(270,80),(225,40)])

    screen.draw_line(a,b,COLOR1,image_buffer)

    screen.show()

def draw_checker():
    WIDTH = 500
    HEIGHT = 500
    CHECKER_SIZE = 125

    COLOR1 = (255, 0, 0)
    COLOR2 = (0, 0, 0)
    DEFAULT_COLOR = (255, 0, 255)

    screen = Screen(WIDTH, HEIGHT)

    image_buffer = np.full((HEIGHT, WIDTH, 3), DEFAULT_COLOR)

    # checker algorithm fills buffer in terms of (HEIGHT, WIDTH) 
    for row in range(HEIGHT):
        for col in range(WIDTH):
            color = COLOR1
            if (int(row / CHECKER_SIZE) % 2) ^ (int(col / CHECKER_SIZE) % 2):
                color = COLOR2

            image_buffer[col, row] = color
            
    screen.draw(image_buffer)

    screen.show()

if __name__ == '__main__':
    draw_checker()

    line_1()
    line_2()

    lines_1()
    lines_2()