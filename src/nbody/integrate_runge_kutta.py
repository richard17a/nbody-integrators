"""
Add module docstring here...
"""
from nbody.integrator import Integrator
from nbody.ode_n_body_first_order import ode_n_body_first_order


class Runge_Kutta(Integrator):
    def __init__(self, particles=None, CONST_G=1.0, dt=0.01):
        super(Runge_Kutta, self).__init__(particles=particles, CONST_G=CONST_G, dt=dt)
        self.__initialised = False

    def integrate(self, end_time):

        if not self.__initialised:
            x = self.initialise(end_time)

        self.sol_state[0, :] = x

        for count, t in enumerate(self.sol_time[1:], 1):

            k1 = ode_n_body_first_order(x, self.CONST_G, self.particles.masses)
            k2 = ode_n_body_first_order(
                x + 0.5 * self.dt * k1, self.CONST_G, self.particles.masses
            )
            k3 = ode_n_body_first_order(
                x + 0.5 * self.dt * k2, self.CONST_G, self.particles.masses
            )
            k4 = ode_n_body_first_order(
                x + self.dt * k3, self.CONST_G, self.particles.masses
            )

            x += self.dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0

            self.sol_state[count, :] = x
            self._t = t
