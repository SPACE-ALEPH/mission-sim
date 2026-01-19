from mission_state import MissionState

def is_quantum_operation_allowed(mission_state):
    """
    Determine whether quantum operations are permitted
    based on the current mission state.
    """

    if mission_state == MissionState.NOMINAL:
        return True

    if mission_state == MissionState.CONSTRAINED:
        return True  # with limitations

    return False
