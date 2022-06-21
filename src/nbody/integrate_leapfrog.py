"""
Add module docstring here...
"""
from nbody.integrator import Integrator
from nbody.ode_n_body_first_order import ode_n_body_first_order


class Leapfrog(Integrator):
    def __init__(self, particles=None, CONST_G=1.0, dt=0.01):
        super(Leapfrog, self).__init__(particles=particles, CONST_G=CONST_G, dt=dt)
        self.__initialised = False

    def integrate(self, end_time):

        if not self.__initialised:
            x = self.initialise(end_time)

        dxdt0 = ode_n_body_first_order(x, self.CONST_G, self.particles.masses)
        self.sol_state[0, :] = x

        for count, t in enumerate(self.sol_time[1:], 1):

            for ibody in range(0, self.particles.N):
                x[ibody * 3:(ibody + 1) * 3] = (
                    x[ibody * 3:(ibody + 1) * 3]
                    + x[(ibody + 2) * 3:(ibody + 3) * 3] * self.dt
                    + 0.5 * dxdt0[(ibody + 2) * 3:(ibody + 3) * 3] * self.dt**2
                )

            dxdt = ode_n_body_first_order(x, self.CONST_G, self.particles.masses)
            for ibody in range(0, self.particles.N):
                x[(ibody + 2) * 3:(ibody + 3) * 3] = (
                    x[(ibody + 2) * 3:(ibody + 3) * 3]
                    + 0.5
                    * (
                        dxdt0[(ibody + 2) * 3:(ibody + 3) * 3]
                        + dxdt[(ibody + 2) * 3:(ibody + 3) * 3]
                    )
                    * self.dt
                )

            dxdt0 = dxdt

            self.sol_state[count, :] = x
            self._t = t
