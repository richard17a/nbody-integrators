from nbody.integrate_runge_kutta import Runge_Kutta
from nbody.particles import Particles
from nbody.particle import Particle
import numpy as np

Sun = Particle(
    mass=1.0,
    position=np.array([0.0, 0.0, 0.0]),
    velocity=np.array([0.0, 0.0, 0.0]),
)

Mercury = Particle(
    mass=1.66051140935277e-07,
    position=np.array([-1.202266214811173E-02, 3.129738317339329E-01, 2.637608427362013E-02]),
    velocity=np.array([-3.374999571504927E-02, -3.223139133573000E-04, 3.069097338939302E-03]),
)

Venus = Particle(
    mass=2.44827371182131e-06,
    position=np.array([6.036656393784035E-01, -4.041148416177896E-01, -4.043024664738540E-02]),
    velocity=np.array([1.125511509001221E-02, 1.664344623604423E-02, -4.214323452340928E-04])
)

Earth = Particle(
    mass=3.00329789031573e-06,
    position=np.array([1.241238601620544E-02, -1.011219129247450E+00, -9.819526634120970E-05]),
    velocity=np.array([1.692619974976791E-02, 1.014868174374918E-04, -6.047160617924358E-08])
)

Mars = Particle(
    mass=.22773848604808e-07,
    position=np.array([-4.926800380968982E-01, 1.537007440322637E+00, 4.411949077995760E-02]),
    velocity=np.array([-1.278895103122624E-02, -3.109871472361932E-03, 2.485576543075108E-04])
)

Jupiter = Particle(
    mass=0.000954532562518104,
    position=np.array([-4.989446787630805E+00, -2.184763688656508E+00, 1.206579440062781E-01]),
    velocity=np.array([2.938669025252137E-03, -6.553859846840747E-03, -3.848907559519295E-05])
)

particles = Particles()
particles.add_particle(Sun)
particles.add_particle(Mercury)
particles.add_particle(Venus)
particles.add_particle(Earth)
particles.add_particle(Mars)
particles.add_particle(Jupiter)

integrator = Runge_Kutta(particles=particles, CONST_G=0.00029591220828559, dt=0.01)

integrator.integrate(end_time=365.25*1.0)

integrator.plot_state(title="3-body Runge Kutta")
integrator.plot_state(category="energy")
