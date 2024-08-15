from screen import Screen

import numpy as np

def polygon_fill():
    WIDTH  = 500
    HEIGHT = 500

    COLOR1 = (255, 0, 0)
    COLOR2 = (0, 0, 0)

    screen = Screen(WIDTH, HEIGHT)

    image_buffer = np.full((HEIGHT, WIDTH, 3), COLOR2)

    a = np.array([(25,100),(225,230),(120,30)])
    b = np.array([(225,230),(120,30),(25,100)])

    screen.draw_polygon(a,b,COLOR1,image_buffer)

    screen.show()

if __name__ == '__main__':
    polygon_fill()