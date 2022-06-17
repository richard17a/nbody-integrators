from nbody.particle import Particle
from nbody.particles import Particles
import numpy as np
import pytest


def test_particles():

    particle_1 = Particle(
        mass=1.0,
        position=np.array([1, 2, 3]),
        velocity=np.array([1, 2, 3]),
    )

    particle_2 = Particle(
        mass=2.0,
        position=np.array([-1, -2, -3]),
        velocity=np.array([-1, -2, -3]),
    )

    assert particle_1 and particle_2

    particles_container = Particles()
    assert particles_container

    particles_container.add_particle(particle_1)
    assert particles_container.N == 1
    assert list(particles_container.positions) == [1, 2, 3]
    assert list(particles_container.masses) == [1.0]

    particles_container.add_particle(particle_2)
    assert particles_container.N == 2
    assert list(particles_container.positions) == [1, 2, 3, -1, -2, -3]
    assert list(particles_container.masses) == [1.0, 2.0]

    particles_container.add_particle(particle_1)
    assert particles_container.N == 2

    with pytest.raises(TypeError):
        particles_container.add_particle("Not a Particle")


def test_remove_particle():

    particle_1 = Particle(
        mass=1.0,
        position=np.array([1, 2, 3]),
        velocity=np.array([1, 2, 3]),
    )

    particle_2 = Particle(
        mass=2.0,
        position=np.array([-1, -2, -3]),
        velocity=np.array([-1, -2, -3]),
    )

    particles = Particles()
    particles.add_particle(particle_1)
    particles.add_particle(particle_2)

    particles.remove_particle(particle_1)
    assert particles.N == 1

    with pytest.raises(TypeError):
        particles.remove_particle(particle_1)


def test_particles_positions_setter():
    particle_1 = Particle(
        mass=1.0,
        position=np.array([1, 2, 3]),
        velocity=np.array([1, 2, 3]),
    )

    particle_2 = Particle(
        mass=2.0,
        position=np.array([-1, -2, -3]),
        velocity=np.array([-1, -2, -3]),
    )

    particles = Particles()
    particles.add_particle(particle_1)
    particles.add_particle(particle_2)

    with pytest.raises(TypeError):
        particles.positions = [1, 2, 3, -1, -2, -3]

    with pytest.raises(ValueError):
        particles.positions = np.array([1, 2, 3])


def test_particles_velocities_setter():
    particle_1 = Particle(
        mass=1.0,
        position=np.array([1, 2, 3]),
        velocity=np.array([1, 2, 3]),
    )

    particle_2 = Particle(
        mass=2.0,
        position=np.array([-1, -2, -3]),
        velocity=np.array([-1, -2, -3]),
    )

    particles = Particles()
    particles.add_particle(particle_1)
    particles.add_particle(particle_2)

    with pytest.raises(TypeError):
        particles.velocities = [1, 2, 3, -1, -2, -3]

    with pytest.raises(ValueError):
        particles.velocities = np.array([1, 2, 3])
