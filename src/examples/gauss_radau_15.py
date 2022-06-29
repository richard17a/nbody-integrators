from nbody.integrate_gauss_radau import Gauss_Radau
from nbody.particles import Particles
from nbody.particle import Particle
import numpy as np

mass_1 = Particle(
    mass=3.0, position=np.array([1.0, 3.0, 0.0]), velocity=np.array([0.0, 0.0, 0.0])
)
mass_2 = Particle(
    mass=4.0, position=np.array([-2.0, -1.0, 0.0]), velocity=np.array([0.0, 0.0, 0.0])
)
mass_3 = Particle(
    mass=5.0, position=np.array([1.0, -1.0, 0.0]), velocity=np.array([0.0, 0.0, 0.0])
)

particles = Particles()
particles.add_particle(mass_1)
particles.add_particle(mass_2)
particles.add_particle(mass_3)

integrator = Gauss_Radau(particles=particles)
integrator.integrate(end_time=3.0)

integrator.plot_state(title="3 Body Gauss-Radau")
integrator.plot_state(category="energy")
