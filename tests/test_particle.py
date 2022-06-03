from src.particle import Particle
import numpy as np
import pytest


def test_particle():

    particle_1 = Particle(
        mass=1.0, position=np.array([1, 2, 3]), velocity=np.array([2, 3, 4])
    )

    particle_1_copy = Particle(
        mass=1.0, position=np.array([1, 2, 3]), velocity=np.array([2, 3, 4])
    )

    assert hash(particle_1) == hash(particle_1_copy)
    assert particle_1.mass == 1.0


def test_particle_index_error():

    with pytest.raises(Exception) as exception_info:

        particle_3 = Particle(
            mass=1.0, position=np.array([1, 2]), velocity=np.array([1, 2, 3])
        )

    assert (
        exception_info.value.args[0]
        == "The position vector must be a numpy array of length 3."
    )
    assert not particle_3
