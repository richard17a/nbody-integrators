"""
Add module docstring...
"""

import numpy as np


class Particle(object):
    def __init__(self, mass, position, velocity, radius=0.0):
        self.mass = mass
        self.radius = radius
        self.__position = position
        self.__velocity = velocity

        # split up position
        self.x_pos = position[0]
        self.y_pos = position[1]
        self.z_pos = position[2]

        # split up velocity
        self.x_vel = velocity[0]
        self.y_vel = velocity[1]
        self.z_vel = velocity[2]

    def __hash__(self):
        pos_str = ",".join([str(pos) for pos in self.position])
        vel_str = ",".join([str(vel) for vel in self.velocity])

        return hash(".".join([str(self.mass), pos_str, vel_str]))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position).__module__ == np.__name__:

            if len(position) == 3:

                self.x_pos = position[0]
                self.y_pos = position[1]
                self.z_pos = position[2]
                self.__position = position

            else:
                raise TypeError(
                    "The position vector must be a numpy array of length 3."
                )

        else:
            raise TypeError("The position vector must be a numpy array of length 3.")

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        if type(velocity).__module__ == np.__name__:

            if len(velocity) == 3:

                self.x_vel = velocity[0]
                self.y_vel = velocity[1]
                self.z_vel = velocity[2]
                self.__velocity = velocity

            else:
                raise TypeError(
                    "The velocity vector must be a numpy array of length 3."
                )

        else:
            raise TypeError("The velocity vector must be a numpy array of length 3.")
