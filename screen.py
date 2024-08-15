import numpy as np
import pygame

class Screen:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        pygame.init()
        self.screen = pygame.display.set_mode([width, height])

    def ratio(self):
        return self.width / self.height

    def draw(self, buf: np.ndarray):
        """Takes a buffer of 8-bit RGB pixels and puts them on the canvas.
        buf should be a ndarray of shape (height, width, 3)"""
        # Make sure that the buffer is HxWx3
        if buf.shape != (self.height, self.width, 3):
            raise Exception("buffer and screen not the same size")

        # Flip buffer to account for 0,0 in bottom left while plotting, but 0,0 in top left in pygame
        buf = np.fliplr(buf)

        # The prefered way to accomplish this
        pygame.pixelcopy.array_to_surface(self.screen, buf)

        # An alternative (slower) way, but still valid
        # Iterate over the pixels and paint them
        # for x, row in enumerate(buf):
            # for y, pix in enumerate(row):
                # self.screen.set_at((x, y), pix.tolist())

        # Update the display
        pygame.display.flip()

    def draw_line(self,a,b, color, buf: np.ndarray):
        """Implement line drawing from point(s) a to b."""

        pass

    #extra credit function
    def draw_polygon(self,a,b, color, buf: np.ndarray):
        """Implement line drawing from point(s) a to b, then color the pixels within the defined polygon. 
        Assumes the input points define a single, closed polygon."""

        pass

    def show(self):
        """Shows the canvas"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        from datetime import datetime
                        pygame.image.save(self.screen, datetime.now().strftime("./%m-%d-%Y_%H--%M--%S.png"))


        pygame.quit()