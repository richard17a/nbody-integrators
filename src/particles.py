"""
Add module docstring...
"""

import numpy as np
from src.particle import Particle


class Particles(object):
	"""
	Class docstring
	"""
	def __init__(
		self
	):
		self.__particles = []
		self.__N = 0

	@property
	def N(self):
		return self.__N

	@property
	def particles(self):
		return self

	def add_particle(self, particle: Particle):

		if isinstance(particle, Particle) and (particle not in self.__particles):

			self.__particles.append(particle)
			self.__N += 1

		else:

			raise TypeError("Unable to add particle.")

	def remove_particle(self, particle: Particle):

		if isinstance(particle, Particle) and (particle in self.__particles):

			self.__particles.remove(particle)
			self.__N -= 1

		else:

			raise TypeError("Unable to remove particle.")
