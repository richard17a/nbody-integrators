from nbody.integrator import Integrator
from nbody.integrate_forwardeuler import Forward_Euler
from nbody.particle import Particle
from nbody.particles import Particles
import numpy as np
from unittest import mock


def test_integrator():

    integrator_empty = Integrator()

    assert not integrator_empty.initialised
    assert integrator_empty.t == 0.0
    assert integrator_empty.t_start == integrator_empty.t_finish

    particle_1 = Particle(
        mass=1.0,
        position=np.array([1, 2, 3]),
        velocity=np.array([1, 2, 3]),
    )

    particles = Particles()
    particles.add_particle(particle_1)

    integrator_not_empty = Integrator(particles=particles)
    assert integrator_not_empty.particles == particles

    integrator_not_empty.initialise(10.0)
    assert integrator_not_empty.t_end == 10.0
    assert integrator_not_empty.initialised


@mock.patch("nbody.integrator.plt")
def test_plot_trajectory(mock_plt):
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

    integrator = Forward_Euler(particles=particles)
    integrator.integrate(10.0)
    integrator.plot_trajectory(title="my title")

    mock_plt.title.assert_called_once_with("my title")
    assert mock_plt.figure.called
