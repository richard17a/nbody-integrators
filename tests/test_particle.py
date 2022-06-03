# import numpy as np
# from src.particle import Particle
# from src.particles import Particles

# particles = Particles()

# print(particles.__dict__)

# particles.add_particle(
# 	Particle(
# 		mass=1,
# 		position=np.array([1,2,3]),
# 		velocity=np.array([2,3,4])
# 	)
# )

# print(particles.__dict__)

# particles.add_particle(
# 	Particle(
# 		mass=1.5,
# 		position=np.array([-1,2,3]),
# 		velocity=np.array([-2,3,4])
# 	)
# )

# print(particles.__dict__)

# particle1 = Particle(
# 		mass=1.5,
# 		position=np.array([-1,2,3]),
# 		velocity=np.array([-2,3,4])
# )

# particle2 = Particle(
# 	mass=1.5,
# 	position=np.array([-1,2.01,3]),
# 	velocity=np.array([-2,3,4])
# )

# print(hash(particle1) == hash(particle2))


def test_particle():
	assert True
