# coding: utf-8
# license: GPLv3
from solar_objects import SpaceObject
import numpy as np
from numpy import sin, cos, arctan2

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    force = np.array([0., 0.])
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя
        dr = np.array([body.x - obj.x, body.y - obj.y])
        force -= gravitational_constant * body.m * obj.m * dr / max(np.linalg.norm(dr), 1.0e9) ** 3
    body.update_params(Fx=force[0], Fy=force[1])


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    magic_acceleration_const = dt
    ax = body.Fx / body.m
    ay = body.Fy / body.m

    body.Vx += magic_acceleration_const * ax
    body.Vy += magic_acceleration_const * ay

    body.x += body.Vx * magic_acceleration_const
    body.y += body.Vy * magic_acceleration_const

    return body


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
