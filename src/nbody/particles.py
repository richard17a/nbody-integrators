"""
Add module docstring...
"""

from nbody.particle import Particle
import numpy as np


class Particles(object):
    """
    Class docstring
    """

    def __init__(self):
        self.__particles = []
        self.__positions = np.array([])
        self.__velocities = np.array([])
        self.__masses = np.array([])
        self.__N = 0

    @property
    def N(self):
        return self.__N

    @property
    def particles(self):
        return self

    @property
    def positions(self):
        return self.__positions

    @positions.setter
    def positions(self, pos_vec):

        if type(pos_vec).__module__ == np.__name__:
            if pos_vec.size == 3 * self.__N:
                for p_id in range(self.__N):
                    self.__particles[p_id].pos = pos_vec[3 * p_id:3 * p_id + 3]
                self.__positions = pos_vec
            else:
                raise ValueError("Position vector must be len=3 vector.")
        else:
            raise TypeError("Position vector must be a numpy vector with len=3*N.")

    @property
    def velocities(self):
        return self.__velocities

    @velocities.setter
    def velocities(self, vel_vec):

        if type(vel_vec).__module__ == np.__name__:
            if vel_vec.size == 3 * self.__N:
                for p_id in range(self.__N):
                    self.__particles[p_id].vel = vel_vec[3 * p_id:3 * p_id + 3]
                self.__velocities = vel_vec
            else:
                raise ValueError("Velocity vector must be len=3*N vector.")
        else:
            raise TypeError("Position vector must be a numpy vector with len=3.")

    @property
    def masses(self):
        return self.__masses

    def add_particle(self, particle: Particle):

        if isinstance(particle, Particle):
            if particle not in self.__particles:
                self.__positions = np.append(self.__positions, particle.position)
                self.__velocities = np.append(self.__velocities, particle.velocity)
                self.__masses = np.append(self.__masses, np.array([particle.mass]))

                self.__particles.append(particle)
                self.__N += 1

        else:

            raise TypeError("Unable to add particle.")

    def remove_particle(self, particle: Particle):

        if isinstance(particle, Particle) and (particle in self.__particles):
            pid = self.__particles.index(particle)
            self.__positions = np.delete(self.__positions, range(3 * pid, 3 * pid + 3))
            self.__velocities = np.delete(
                self.__velocities, range(3 * pid, 3 * pid + 3)
            )
            self.__masses = np.delete(self.__masses, pid)

            self.__particles.remove(particle)
            self.__N -= 1

        else:

            raise TypeError("Unable to remove particle.")
