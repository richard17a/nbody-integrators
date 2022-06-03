import pytest
import numpy as np


@pytest.fixture(scope="session")
def particle_1():
    from src.particle import Particle

    particle_1 = Particle(
        mass=1.0, position=np.array([1, 2, 3]), velocity=np.array([2, 3, 4])
    )

    return particle_1


@pytest.fixture(scope="session")
def particle_1_copy():
    from src.particle import Particle

    particle_1_copy = Particle(
        mass=1.0, position=np.array([1, 2, 3]), velocity=np.array([2, 3, 4])
    )

    return particle_1_copy


@pytest.fixture(scope="session")
def particle_3():
    from src.particle import Particle

    particle_3 = Particle(
        mass=1.0, position=np.array([1, 2]), velocity=np.array([1, 2, 3])
    )

    return particle_3
