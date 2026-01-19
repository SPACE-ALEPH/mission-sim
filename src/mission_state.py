from enum import Enum

class MissionState(Enum):
    NOMINAL = 1
    CONSTRAINED = 2
    DEGRADED = 3
    SAFE = 4


def evaluate_mission_state(env):
    """
    Evaluate mission state based on abstract environmental indicators.

    env: dict with keys such as:
        - thermal_margin
        - radiation_level
        - vibration_level
    """

    if env["thermal_margin"] < 0 or env["radiation_level"] > 1.0:
        return MissionState.SAFE

    if env["thermal_margin"] < 0.1 or env["vibration_level"] > 0.7:
        return MissionState.DEGRADED

    if env["vibration_level"] > 0.4:
        return MissionState.CONSTRAINED

    return MissionState.NOMINAL
