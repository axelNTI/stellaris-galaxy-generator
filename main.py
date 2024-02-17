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
    hyperlanes = []
    solar_systems = []
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    return

                # Select starting solar system for hyperlane

                if event.type == pg.K_b:
                    for system in solar_systems:
                        if (
                            np.linalg.norm(
                                np.array(system.position) - np.array(pg.mouse.get_pos())
                            )
                            < 10
                        ):
                            start_system = system
                            break
                    else:
                        start_system = None
                    print(start_system)

                # Select endpoint solar system for hyperlane and create hyperlane

                if event.type == pg.K_a:
                    for system in solar_systems:
                        if (
                            np.linalg.norm(
                                np.array(system.position) - np.array(pg.mouse.get_pos())
                            )
                            < 10
                        ):
                            end_system = system
                            break
                    else:
                        end_system = None
                    print(end_system)
                    if start_system is not None and end_system is not None:
                        hyperlanes.append(Hyperlane(start_system, end_system))
                    start_system = None
                    end_system = None

        # Add solar systems with mouse click
        if pg.mouse.get_pressed()[0]:
            solar_systems.append(SolarSystem(pg.mouse.get_pos()))

        # Remove solar systems with right mouse click
        if pg.mouse.get_pressed()[2]:
            for system in solar_systems:
                if (
                    np.linalg.norm(
                        np.array(system.position) - np.array(pg.mouse.get_pos())
                    )
                    < 10
                ):
                    solar_systems.remove(system)
                    break

        # Draws all solar systems
        screen.fill((0, 0, 0))
        for system in solar_systems:
            pg.draw.circle(screen, (255, 255, 255), system.position, 10)

        # Draws all hyperlanes
        for hyperlane in hyperlanes:
            if hyperlane.startpoint is not None and hyperlane.endpoint is not None:
                pg.draw.line(
                    screen,
                    (255, 255, 255),
                    hyperlane.startpoint.position,
                    hyperlane.endpoint.position,
                    2,
                )
        pg.display.update()
        clock.tick(30)


main()
