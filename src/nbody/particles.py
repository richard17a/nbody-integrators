"""
Add module docstring...
"""

from nbody.particle import Particle
import numpy as np
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


class Particles(object):
    """
    Class docstring
    """

    def __init__(self):
        self.__particles = []
        self.__positions = np.array([])
        self.__velocities = np.array([])
        self.__masses = np.array([])
        self.__radii = np.array([])
        self.__N = 0

    @property
    def N(self):
        return self.__N

    @property
    def particles(self):
        return self.__particles

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

    @property
    def radii(self):
        return self.__radii

    def add_particle(self, particle: Particle):

        if isinstance(particle, Particle):
            if particle not in self.__particles:
                self.__positions = np.append(self.__positions, particle.position)
                self.__velocities = np.append(self.__velocities, particle.velocity)
                self.__masses = np.append(self.__masses, np.array([particle.mass]))
                self.__radii = np.append(self.__radii, np.array([particle.radius]))

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

    def merge_particles(self, particle_1: Particle, particle_2: Particle):
        try:
            id_1 = self.__particles.index(particle_1)
            id_2 = self.__particles.index(particle_2)
        except ValueError:
            raise ValueError("Ensure both particles are defined in the Particles() object.")

        if id_1 is not None and id_2 is not None:

            if self.__particles[id_1].mass >= self.__particles[id_2].mass:
                primary = self.__particles[id_1]
                secondary = self.__particles[id_2]
            else:
                primary = self.__particles[id_2]
                secondary = self.__particles[id_1]

            primary.velocity = (primary.mass * primary.velocity + secondary.mass * secondary.velocity) / (primary.mass + secondary.mass)
            primary.mass = primary.mass + secondary.mass
            primary.radius = np.power(np.power(primary.radius, 3.0) + np.power(secondary.radius, 3.0), 1.0 / 3)

            self.__velocities[3*self.__particles.index(primary):3*self.__particles.index(primary)+3] = primary.velocity
            self.__masses[self.__particles.index(primary)] = primary.mass
            self.__radii[self.__particles.index(primary)] = primary.radius

            self.remove_particle(secondary)
            logging.info(f"Merging particles {id_1} and {id_2} into {id_1}.")
