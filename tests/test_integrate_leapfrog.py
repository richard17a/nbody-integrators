from nbody.integrate_leapfrog import Leapfrog
from nbody.particle import Particle
from nbody.particles import Particles
import numpy as np


def test_leapfrog():
    particle_1 = Particle(
        mass=1.0,
        position=np.array([1, 0, 0]),
        velocity=np.array([0, 0.5, 0]),
    )
    particle_2 = Particle(
        mass=1.0,
        position=np.array([-1, 0, 0]),
        velocity=np.array([0, -0.5, 0]),
    )

    particles = Particles()
    particles.add_particle(particle_1)
    particles.add_particle(particle_2)

    integrator = Leapfrog(particles=particles)
    integrator.integrate(10.0)
    energy = list(integrator.calculate_energy())
    energy_diff = list(np.abs((energy[0] - energy) / energy[0]))

    assert energy_diff and max(energy_diff) < 1e-9
