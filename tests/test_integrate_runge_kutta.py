from nbody.integrate_runge_kutta import Runge_Kutta
from nbody.particle import Particle
from nbody.particles import Particles
import numpy as np


def test_runge_kutta():
    particle_1 = Particle(
        mass=1.0,
        position=np.array([0.9700436, -0.24308753, 0.0]),
        velocity=np.array([0.466203685, 0.43236573, 0.0]),
    )

    particle_2 = Particle(
        mass=1.0,
        position=np.array([-0.9700436, 0.24308753, 0.0]),
        velocity=np.array([0.466203685, 0.43236573, 0.0]),
    )

    particle_3 = Particle(
        mass=1.0,
        position=np.array([0.0, 0.0, 0.0]),
        velocity=np.array([-0.93240737, -0.86473146, 0.0]),
    )

    particles = Particles()
    particles.add_particle(particle_1)
    particles.add_particle(particle_2)
    particles.add_particle(particle_3)

    integrator = Runge_Kutta(particles=particles, dt=0.01)
    integrator.integrate(100.0)
    energy = list(integrator.calculate_energy())
    energy_diff = list(np.abs((energy[0] - energy) / energy[0]))

    assert energy_diff and max(energy_diff) < 1e-7
