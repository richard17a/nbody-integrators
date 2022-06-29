import numpy as np


def ode_n_body_second_order(x, const_g, masses):
    """
    This needs going over!
    """
    nbodies = int(x.size / 3)

    # Allocate
    acc = x * 0.0

    # Position
    for j in range(0, nbodies):
        Rj = x[j * 3:3 + j * 3]
        aj = Rj * 0
        for k in range(0, nbodies):
            if j == k:
                continue
            Rk = x[k * 3:3 + k * 3]
            rel_sep = Rj - Rk
            aj += -const_g * masses[k] * rel_sep / np.linalg.norm(rel_sep) ** 3
        acc[j * 3:3 + j * 3] = aj

    return acc
