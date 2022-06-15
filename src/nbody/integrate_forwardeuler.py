"""
Add module docstring here...
"""

from nbody.integrator import Integrator
import numpy as np
from nbody.ode_n_body_first_order import ode_n_body_first_order


class Forward_Euler(Integrator):
    def __init__(self, particles=None, dt=0.01):
        super(Forward_Euler, self).__init__(particles=particles, dt=dt)
        self.__initialised = False

    def integrate(self, end_time):

        if not self.__initialised:
            x, sol_time, npts = self.initialise(end_time)
            self.__initialized = True

        sol_state = np.zeros((npts, len(x)))
        sol_state[0, :] = x

        count = 1
        for t in sol_time[count:]:

            dxdt = ode_n_body_first_order(x, self.CONST_G, self._particles.masses)
            x = x + dxdt * self.dt

            self._particles.positions = x[0:self._particles.N * 3]
            self._particles.velocities = x[self._particles.N * 3:]

            sol_state[count, :] = x

            count += 1
            self._t = t

        return sol_time, sol_state
