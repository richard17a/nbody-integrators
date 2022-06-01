"""
Add module docstring...
"""

import numpy as np 


class Particle(object):

	def __init__(
		self,
		mass,
		position,
		velocity
	):
		self.mass = mass
		self.position = position
		self.velocity = velocity

		# split up position
		self.x_pos = position[0]
		self.y_pos = position[1]
		self.z_pos = position[2]

		# split up velocity
		self.x_vel = velocity[0]
		self.y_vel = velocity[1]
		self.z_vel = velocity[2]

	@property
	def position(self):
		return self._position

	@position.setter
	def position(
		self,
		position
	):
		if type(position).__module__ == np.__name__:
			
			if len(position) == 3:
				
				self.x = position[0]
				self.y = position[1]
				self.z = position[2]
				self.position = position

			else:
				raise TypeError("The position vector must be a numpy array with length 3.")

		else:
			raise TypeError("The position vector must be a numpy array with length 3.")

	@property
	def velocity(self):
		return self._velocity

	@velocity.setter
	def velocity(
		self,
		velocity
	):
		if type(velocity).__module__ == np.__name__:
			
			if len(velocity) == 3:
				
				self.x = velocity[0]
				self.y = velocity[1]
				self.z = velocity[2]
				self.velocity = velocity

			else:
				raise TypeError("The velocity vector must be a numpy array with length 3.")

		else:
			raise TypeError("The velocity vector must be a numpy array with length 3.")
	