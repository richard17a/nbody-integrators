"""
Add module docstring here...
"""

from nbody.integrator import Integrator
from nbody.ode_n_body_first_order import ode_n_body_first_order


class Forward_Euler(Integrator):
    def __init__(self, particles=None, dt=0.01):
        super(Forward_Euler, self).__init__(particles=particles, dt=dt)
        self.__initialised = False

    def integrate(self, end_time):

        if not self.__initialised:
            x = self.initialise(end_time)

        count = 1
        for t in self.sol_time[count:]:

            dxdt = ode_n_body_first_order(x, self.CONST_G, self._particles.masses)
            x = x + dxdt * self.dt

            self._particles.positions = x[0: self._particles.N * 3]
            self._particles.velocities = x[self._particles.N * 3:]

            self.sol_state[count, :] = x

            count += 1
            self._t = t
