# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet, SpaceObject
from solar_vis import DrawableObject


def read_space_objects_data_from_file(input_filename):
    """Считывает данные123.find о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return [DrawableObject(obj) for obj in objects]


def parse_object_parameters(line: str, obj: SpaceObject):
    """Считывает данные о объекте из строки.

    Входная строка должна иметь слеюущий формат:

    <object> <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.

    Пример строки:

    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.

    **obj** — объект.
    """
    _, r, c, m, x, y, vx, vy = line.split()
    r, m, x, y, vx, vy = tuple(map(float, (r, m, x, y, vx, vy)))  # Convert star data to int if nes
    print(f'{vx=}, {vy=}')
    obj.update_params(r=r,
                      m=m,
                      Vx=vx,
                      Vy=vy,
                      color=c,
                      x=x,
                      y=y
                      )
    return obj


parse_star_parameters = parse_object_parameters
parse_planet_parameters = parse_object_parameters


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.

    Строки должны иметь следующий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, f"{obj.type} {obj.R} {obj.color} {obj.m} {obj.x} {obj.y} {obj.Vx} {obj.Vy}")


if __name__ == "__main__":
    print("This module is not for direct call!")
