"""
Mission-Sim
Foundational orbit propagation module for
quantum computing satellite mission concepts.
"""

import numpy as np

MU_EARTH = 3.986e14  # Earth's gravitational parameter (m^3/s^2)

def propagate_orbit(r, v, dt):
    r_norm = np.linalg.norm(r)
    a = -MU_EARTH * r / r_norm**3
    v_new = v + a * dt
    r_new = r + v_new * dt
    return r_new, v_new
