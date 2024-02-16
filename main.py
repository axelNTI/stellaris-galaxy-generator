import pygame as pg
import numpy as np

#  Class for a solar system with position


class SolarSystem:
    def __init__(self, position):
        self.position = position
        
        
# Class for hyperlanes with endpoint and startpoint being solar systems
class Hyperlane:
    def __init__(self, startpoint, endpoint):
        self.startpoint = startpoint
        self.endpoint = endpoint

def main():
    pg.init()
    #  get native screen resolution
    info = pg.display.Info()
    screen_size = (info.current_w, info.current_h)
    screen = pg.display.set_mode(screen_size)

    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.q:
                    return
        clock.tick(30)


main()
