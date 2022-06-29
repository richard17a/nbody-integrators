from nbody.integrate_gauss_radau import Gauss_Radau
from nbody.particle import Particle
from nbody.particles import Particles
import numpy as np


def test_runge_kutta():
    particle_1 = Particle(
        mass=1.0,
        position=np.array([1.0, 0.0, 0.0]),
        velocity=np.array([0.0, 0.5, 0.0]),
    )

    particle_2 = Particle(
        mass=1.0,
        position=np.array([-1.0, 0.0, 0.0]),
        velocity=np.array([0.0, -0.5, 0.0]),
    )

    particles = Particles()
    particles.add_particle(particle_1)
    particles.add_particle(particle_2)

    integrator = Gauss_Radau(particles=particles, dt=0.01)
    integrator.integrate(10.0)
    energy = list(integrator.calculate_energy())
    energy_diff = list(np.abs((energy[0] - energy) / energy[0]))

    assert energy_diff and max(energy_diff) < 1e-14
