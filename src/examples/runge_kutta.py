from nbody.integrate_runge_kutta import Runge_Kutta
from nbody.particles import Particles
from nbody.particle import Particle
import numpy as np


mass_1 = Particle(
    mass=1.0,
    position=np.array([0.9700436, -0.24308753, 0.0]),
    velocity=np.array([0.466203685, 0.43236573, 0.0]),
)

mass_2 = Particle(
    mass=1.0,
    position=np.array([-0.9700436, 0.24308753, 0.0]),
    velocity=np.array([0.466203685, 0.43236573, 0.0]),
)

mass_3 = Particle(
    mass=1.0,
    position=np.array([0.0, 0.0, 0.0]),
    velocity=np.array([-0.93240737, -0.86473146, 0.0]),
)

particles = Particles()
particles.add_particle(mass_1)
particles.add_particle(mass_2)
particles.add_particle(mass_3)

integrator = Runge_Kutta(particles=particles, dt=0.001)

integrator.integrate(end_time=100.0)

integrator.plot_state(title="3-body Runge Kutta")
integrator.plot_state(category="energy")
