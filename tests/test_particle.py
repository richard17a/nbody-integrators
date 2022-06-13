from nbody.particle import Particle
import numpy as np


def test_particle():
    particle_1 = Particle(
        mass=1.0,
        position=np.array([1, 2, 3]),
        velocity=np.array([1, 2, 3]),
    )

    particle_1_copy = Particle(
        mass=1.0,
        position=np.array([1, 2, 3]),
        velocity=np.array([1, 2, 3]),
    )

    assert particle_1 and particle_1_copy
    assert hash(particle_1) == hash(particle_1_copy)
    assert list(particle_1.position) == [1, 2, 3]
    assert (
        particle_1_copy.x_pos == 1
        and particle_1_copy.y_pos == 2
        and particle_1_copy.z_pos == 3
    )
    assert list(particle_1.velocity) == [1, 2, 3]
