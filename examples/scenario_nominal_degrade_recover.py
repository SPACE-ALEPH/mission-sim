from mission_state import autonomy_decision

def run_scenario():
    timeline = [
        # time, thermal_margin, radiation_level, vibration_level
        ("T+0",  0.30, 0.20, 0.10),  # nominal
        ("T+1",  0.15, 0.20, 0.50),  # constrained (vibration)
        ("T+2",  0.05, 0.30, 0.80),  # degraded (high vibration)
        ("T+3", -0.02, 0.40, 0.30),  # safe (thermal violation)
        ("T+4",  0.12, 0.20, 0.20),  # constrained recovery
        ("T+5",  0.25, 0.15, 0.10),  # nominal recovery
    ]

    print("=== ℵ - SYSTEMS Autonomy Scenario: Nominal -> Degrade -> Safe -> Recover ===\n")

    for t, thermal_margin, radiation_level, vibration_level in timeline:
        env = {
            "thermal_margin": thermal_margin,
            "radiation_level": radiation_level,
            "vibration_level": vibration_level,
        }

        decision = autonomy_decision(env)

        print(f"{t}")
        print(f"  env: thermal_margin={thermal_margin:.2f}, radiation={radiation_level:.2f}, vibration={vibration_level:.2f}")
        print(f"  mission_state: {decision['mission_state'].name}")
        print(f"  quantum_ops_allowed: {decision['quantum_ops_allowed']}")
        print(f"  trace: {', '.join(decision['trace'])}")
        print("")

if __name__ == "__main__":
    run_scenario()
