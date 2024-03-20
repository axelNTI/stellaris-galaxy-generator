import pygame as pg
import pygame_gui as gui
import os
import pytest

#  Class for a solar system with position


class SolarSystem:
    def __init__(self, position: tuple[int, int]):
        self.position = position
        self.posx, self.posy = position

    def setID(self, id: int):
        self.id = str(id)

        


# Class for hyperlanes with endpoint and startpoint being solar systems
class Hyperlane:
    def __init__(self, starting_system, ending_system):
        self.starting_system = starting_system
        self.ending_system = ending_system


def main():
    pg.init()
    #  get native screen resolution
    info = pg.display.Info()
    screen_size = (info.current_w, info.current_h)
    screen = pg.display.set_mode(screen_size)
    hyperlanes = []
    solar_systems = []
    running(screen, hyperlanes, solar_systems)


def running(screen, hyperlanes, solar_systems):
    while True:
        [
            pg.draw.circle(screen, (255, 255, 255), system.position, 10)
            for system in solar_systems
        ]
        [
            pg.draw.line(
                screen,
                (255, 255, 255),
                hyperlane.starting_system.position,
                hyperlane.ending_system.position,
                2,
            )
            for hyperlane in hyperlanes
        ]
        pg.display.update()


def save(
    hyperlanes: list[Hyperlane],
    solar_systems: list[SolarSystem],
    name: str,
    core_radius: int,
):
    
    for iterator, system in enumerate(solar_systems):
        system.setID(iterator)

    with open("galaxy_shapes.txt", "w") as file:
        file.write("static_galaxy_scenario={\n")
        file.write(f'    name = "{name}"\n')
        file.write("    priority = 15\n")
        file.write("    radius = 450\n")
        file.write("    num_empires = {min = 0 max = 30}\n")
        file.write("    num_empire_default = 10\n")
        file.write("    fallen_empire_default = 0\n")
        file.write("    fallen_empire_max = 0\n")
        file.write("    marauder_empire_default = 0\n")
        file.write("    marauder_empire_max = 0\n")
        file.write("    advanced_empire_default = 0\n")
        file.write("    colonizable_planet_odds = 1.0\n")
        file.write("    primitive_species_odds = 1.0\n")
        file.write("    crisis_strength = 0.75\n")
        file.write("    extra_crisis_strength = { 10 25 }\n")
        file.write("    num_wormhole_pairs = {min = 0 max = 5}\n")
        file.write("    num_wormhole_pairs_default = 1\n")
        file.write("    num_gateways = {min = 0 max = 5}\n")
        file.write("    num_gateways_default = 1\n")
        file.write("    random_hyperlanes = no\n")
        file.write(f"    core_radius = {core_radius}\n")
        [
            file.write(
                f'    system = {{ id = "{system.id}" name = "" position = {{ x = {system.posx} y = {system.posy} }} }}\n'
            )
            for iterator, system in enumerate(solar_systems)
        ]
        [
            file.write(
                f'    add_hyperlane = {{ from = "{hyperlane.starting_system.id}" to = "{hyperlane.ending_system.id}" }}\n'
            )
            for hyperlane in hyperlanes
        ]
        file.write("}")


if __name__ == "__main__":

    # main()

    solar_systems = [
        SolarSystem((100, 100), "1"),
        SolarSystem((100, 200), "2"),
        SolarSystem((200, 100), "3"),
        SolarSystem((200, 200), "4"),
    ]
    hyperlanes = [
        Hyperlane(solar_systems[0], solar_systems[1]),
        Hyperlane(solar_systems[0], solar_systems[2]),
        Hyperlane(solar_systems[1], solar_systems[3]),
        Hyperlane(solar_systems[2], solar_systems[3]),
    ]
    save(hyperlanes, solar_systems, "test", 100)


# for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 return
#             if event.type == pg.KEYDOWN:
#                 if event.key == pg.K_q:
#                     return
#                 if event.type == pg.K_b:
#                     for system in solar_systems:
#                         if (
#                             np.linalg.norm(
#                                 np.array(system.position) - np.array(pg.mouse.get_pos())
#                             )
#                             < 10
#                         ):
#                             start_system = system
#                             break
#                     else:
#                         start_system = None
#                     print(start_system)

#                 # Select endpoint solar system for hyperlane and create hyperlane

#                 if event.type == pg.K_a:
#                     for system in solar_systems:
#                         if (
#                             np.linalg.norm(
#                                 np.array(system.position) - np.array(pg.mouse.get_pos())
#                             )
#                             < 10
#                         ):
#                             end_system = system
#                             break
#                     else:
#                         end_system = None
#                     print(end_system)
#                     if start_system is not None and end_system is not None:
#                         hyperlanes.append(Hyperlane(start_system, end_system))
#                     start_system = None
#                     end_system = None

#         # Add solar systems with mouse click
#         if pg.mouse.get_pressed()[0]:
#             solar_systems.append(SolarSystem(pg.mouse.get_pos()))

#         # Remove solar systems with right mouse click
#         if pg.mouse.get_pressed()[2]:
#             for system in solar_systems:
#                 if (
#                     np.linalg.norm(
#                         np.array(system.position) - np.array(pg.mouse.get_pos())
#                     )
#                     < 10
#                 ):
#                     solar_systems.remove(system)
#                     break

#         # Draws all solar systems
#         screen.fill((0, 0, 0))
#         for system in solar_systems:
#             pg.draw.circle(screen, (255, 255, 255), system.position, 10)

#         # Draws all hyperlanes
#         for hyperlane in hyperlanes:
#             if hyperlane.startpoint is not None and hyperlane.endpoint is not None:
#                 pg.draw.line(
#                     screen,
#                     (255, 255, 255),
#                     hyperlane.startpoint.position,
#                     hyperlane.endpoint.position,
#                     2,
#                 )
