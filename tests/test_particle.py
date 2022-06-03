import pytest


def test_particle(particle_1, particle_1_copy):

    assert hash(particle_1) == hash(particle_1_copy)
    assert particle_1.mass == 1.0


def test_particle_index_error(particle_3):

    with pytest.raises(Exception) as exception_info:

        particle_3

    assert (
        exception_info.value.args[0]
        == "The position vector must be a numpy array of length 3."
    )
    assert not particle_3
