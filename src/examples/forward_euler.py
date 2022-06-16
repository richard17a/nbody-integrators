from nbody.integrate_forwardeuler import Forward_Euler
from nbody.particles import Particles
from nbody.particle import Particle
import numpy as np
import matplotlib.pyplot as plt

mass_1 = Particle(
    mass=1.0, position=np.array([1.0, 0.0, 0.0]), velocity=np.array([0.0, 0.5, 0.0])
)
mass_2 = Particle(
    mass=1.0, position=np.array([-1.0, 0.0, 0.0]), velocity=np.array([0.0, -0.5, 0.0])
)

particles = Particles()
particles.add_particle(mass_1)
particles.add_particle(mass_2)

integrator = Forward_Euler(particles=particles, dt=0.0001)
integrator.integrate(end_time=10.0)
integrator.plot_trajectory(title="2 body")

energy = integrator.calculate_energy()
time = integrator.sol_time

plt.semilogy(time, np.abs((energy[0] - energy) / energy[0]))
plt.xlabel("Time")
plt.ylabel(r"$\Delta E$")
plt.show()
