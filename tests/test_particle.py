def test_particle(particle_1, particle_1_copy):

    assert hash(particle_1) == hash(particle_1_copy)
    assert particle_1.mass == 1.0
