from mission_state import MissionState, evaluate_mission_state, autonomy_decision

def test_nominal_state():
    env = {"thermal_margin": 0.3, "radiation_level": 0.2, "vibration_level": 0.1}
    assert evaluate_mission_state(env) == MissionState.NOMINAL

def test_constrained_state_by_vibration():
    env = {"thermal_margin": 0.3, "radiation_level": 0.2, "vibration_level": 0.5}
    assert evaluate_mission_state(env) == MissionState.CONSTRAINED

def test_degraded_state_by_vibration():
    env = {"thermal_margin": 0.3, "radiation_level": 0.2, "vibration_level": 0.8}
    assert evaluate_mission_state(env) == MissionState.DEGRADED

def test_safe_state_by_thermal_violation():
    env = {"thermal_margin": -0.01, "radiation_level": 0.2, "vibration_level": 0.1}
    assert evaluate_mission_state(env) == MissionState.SAFE

def test_autonomy_decision_contains_trace_and_gate():
    env = {"thermal_margin": -0.01, "radiation_level": 0.2, "vibration_level": 0.1}
    decision = autonomy_decision(env)
    assert "mission_state" in decision
    assert "quantum_ops_allowed" in decision
    assert "trace" in decision
    assert decision["mission_state"] == MissionState.SAFE
    assert decision["quantum_ops_allowed"] is False
    assert len(decision["trace"]) >= 1
