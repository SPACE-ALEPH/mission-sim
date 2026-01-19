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

def evaluate_with_trace(env):
    """
    Evaluate mission state and return a traceable explanation.
    """

    reasons = []

    if env["thermal_margin"] < 0:
        reasons.append("Thermal margin violated")
    if env["radiation_level"] > 1.0:
        reasons.append("Radiation level exceeds limit")
    if env["vibration_level"] > 0.7:
        reasons.append("High vibration detected")

    state = evaluate_mission_state(env)

    return {
        "mission_state": state,
        "reasons": reasons if reasons else ["All parameters nominal"]
    }
