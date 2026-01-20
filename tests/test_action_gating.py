from mission_state import MissionState
from action_gating import is_quantum_operation_allowed

def test_quantum_ops_allowed_in_nominal():
    assert is_quantum_operation_allowed(MissionState.NOMINAL) is True

def test_quantum_ops_allowed_in_constrained():
    assert is_quantum_operation_allowed(MissionState.CONSTRAINED) is True

def test_quantum_ops_not_allowed_in_degraded():
    assert is_quantum_operation_allowed(MissionState.DEGRADED) is False

def test_quantum_ops_not_allowed_in_safe():
    assert is_quantum_operation_allowed(MissionState.SAFE) is False
