import pygame as pg
import pygame_gui as gui

#  Class for a solar system with position


class SolarSystem:
    def __init__(self, position: tuple[int, int]):
        self.position = position
        self.posx, self.posy = position
        self.hyperlanes = []

    def setID(self, id: int):
        self.id = str(id + 1)

    def add_hyperlane(self, hyperlane):
        self.hyperlanes.append(hyperlane)


# Class for hyperlanes with endpoint and startpoint being solar systems
class Hyperlane:
    def __init__(self, starting_system: SolarSystem, ending_system: SolarSystem):
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
    star_mode = True
    drawing = False
    while True:
        screen.fill((0, 0, 0))
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
        pg.draw.circle(
            screen,
            (255, 255, 255),
            (screen.get_width() // 2, screen.get_height() // 2),
            30,
            1,
        )
        pg.draw.circle(
            screen,
            (255, 255, 255),
            (screen.get_width() // 2, screen.get_height() // 2),
            450,
            1,
        )

        # Event handling
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    return
                if event.key == pg.K_s and not drawing:
                    star_mode = not star_mode
                if event.key == pg.K_RETURN:
                    save(hyperlanes, solar_systems, "SSGALAXY")
            if star_mode:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if (
                            30
                            < (
                                (event.pos[0] - screen.get_width() / 2) ** 2
                                + (event.pos[1] - screen.get_height() / 2) ** 2
                            )
                            ** 0.5
                            < 450
                        ):
                            solar_systems.append(SolarSystem(event.pos))
                    if event.button == 3:
                        for system in solar_systems:
                            if (
                                system.position[0] - 10
                                < event.pos[0]
                                < system.position[0] + 10
                            ):
                                if (
                                    system.position[1] - 10
                                    < event.pos[1]
                                    < system.position[1] + 10
                                ):
                                    solar_systems.remove(system)
                                    for hyperlane in system.hyperlanes:
                                        if hyperlane in hyperlanes:
                                            hyperlanes.remove(hyperlane)
            if not star_mode:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Check if the mouse is over a star
                        for system in solar_systems:
                            if (
                                system.position[0] - 10
                                < event.pos[0]
                                < system.position[0] + 10
                            ):
                                if (
                                    system.position[1] - 10
                                    < event.pos[1]
                                    < system.position[1] + 10
                                ):
                                    starting_system = system
                                    drawing = True
                    if event.button == 3:
                        for hyperlane in hyperlanes:
                            if (
                                hyperlane.starting_system.position[0] - 10
                                < event.pos[0]
                                < hyperlane.starting_system.position[0] + 10
                            ):
                                if (
                                    hyperlane.starting_system.position[1] - 10
                                    < event.pos[1]
                                    < hyperlane.starting_system.position[1] + 10
                                ):
                                    hyperlanes.remove(hyperlane)
                if event.type == pg.MOUSEBUTTONUP:
                    drawing = False
                    for system in solar_systems:
                        if (
                            system.position[0] - 10
                            < event.pos[0]
                            < system.position[0] + 10
                        ):
                            if (
                                system.position[1] - 10
                                < event.pos[1]
                                < system.position[1] + 10
                            ):
                                new_hyperlane = Hyperlane(starting_system, system)
                                hyperlanes.append(new_hyperlane)
                                starting_system.add_hyperlane(new_hyperlane)
                                system.add_hyperlane(new_hyperlane)
        if drawing:
            pg.draw.line(
                screen, (255, 255, 255), starting_system.position, pg.mouse.get_pos(), 2
            )

        pg.display.update()


def save(
    hyperlanes: list[Hyperlane],
    solar_systems: list[SolarSystem],
    name: str,
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
        file.write("    core_radius = 30\n")
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

    main()
