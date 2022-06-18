"""
An abstract integrator object.
"""
import numpy as np
import matplotlib.pyplot as plt
from nbody.particles import Particles


class Integrator(object):
    def __init__(self, particles=None, CONST_G=1.0, dt=0.01):
        self.CONST_G = CONST_G
        self._particles = particles
        self.dt = dt
        self._t = 0.0
        self.t_start = 0.0
        self.t_finish = 0.0
        self.__energy = 0.0
        self.__initialised = False
        self.sol_time = np.zeros(0)
        self.sol_state = np.zeros(0)

    @property
    def particles(self):
        if self._particles is None:
            self._particles = Particles()
        return self._particles

    @property
    def t(self):
        return self._t

    @property
    def initialised(self):
        return self.__initialised

    def calculate_energy(self):
        if not self.__initialised:
            raise TypeError(
                "The solution must be integrated before calculating energy."
            )
        energy = self.sol_state[:, 0] * 0

        masses = self.particles.masses
        G = self.CONST_G
        nbodies = self.particles.N

        count = 0
        for x in self.sol_state:
            energy[count] = 0
            for i in range(0, nbodies):
                energy[count] += (
                    0.5
                    * masses[i]
                    * np.linalg.norm(x[(nbodies + i) * 3:(nbodies + 1 + i) * 3]) ** 2
                )
                for j in range(0, nbodies):
                    if i == j:
                        continue
                    energy[count] -= (
                        0.5
                        * G
                        * masses[i]
                        * masses[j]
                        / np.linalg.norm(
                            x[i * 3:(i + 1) * 3] - x[j * 3:(j + 1) * 3]
                        )
                    )
            count += 1

        return energy

    def __plot_trajectory(self, title="N-Body Simulation"):
        if not self.__initialised:
            raise TypeError(
                "The solution must be integrated before plotting the trajectory."
            )
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect="equal")

        for ibody in range(0, self.particles.N):
            traj = ax.plot(
                self.sol_state[:, ibody * 3], self.sol_state[:, 1 + ibody * 3]
            )
            ax.plot(
                self.sol_state[0, ibody * 3],
                self.sol_state[0, 1 + ibody * 3],
                "o",
                color=traj[0].get_color(),
            )

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        plt.title(title)
        plt.show()

    def __plot_energy(self, title="Relative Energy Error"):
        if not self.__initialised:
            raise TypeError(
                "The solution must be integrated before plotting the relative energy error."
            )

        energy = self.calculate_energy()
        time = self.sol_time

        plt.semilogy(time, np.abs((energy[0] - energy) / energy[0]))
        plt.xlabel("Time")
        plt.ylabel(r"Relative energy error $\Delta E/E_0$")
        plt.title(title)
        plt.show()

    def plot_state(self, category="trajectory", title=None):
        if category == "trajectory":
            if title:
                self.__plot_trajectory(title)
            else:
                self.__plot_trajectory()
        elif category == "energy":
            if title:
                self.__plot_energy(title)
            else:
                self.__plot_energy()
        else:
            raise ValueError(
                "Incorrect category choice, please choose from: [trajectory, energy]."
            )

    def initialise(self, to_time=None):
        self.__initialised = True

        if to_time is not None:
            self.t_end = to_time

        npts = int(np.floor((self.t_end - self.t_start) / self.dt) + 1)
        x = np.concatenate((self.particles.positions, self.particles.velocities))

        self.sol_time = np.linspace(
            self.t_start, self.t_start + self.dt * (npts - 1), npts
        )
        self.sol_state = np.zeros((npts, len(x)))
        self.sol_state[0, :] = x

        return x
