"""
Add module docstring...
"""

import numpy as np 
from particle import Particle 


class Particles(object):
	"""
	Class docstring
	"""
	def __init__(
		self
	):
		self.particles = []
		self.N = 0

	@property
	def N(self):
		return self._N

	@property
	def particles(self):
		return self._particles
	
	def add_particle(self, particle: Particle):
		pass

	def remove_particle(self, particle: Particle):
		pass
	