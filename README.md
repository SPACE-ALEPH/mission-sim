# Mission-Sim

![Build Status](https://img.shields.io/badge/build-research-lightgrey)
![License: MIT](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-phase--0-orange)

Mission-Sim is a research-stage mission simulation framework
supporting the development and validation of mission-level autonomy
for space systems.

It serves as a conceptual and experimental foundation for ℵ – SYSTEMS,
providing minimal, explainable building blocks for autonomy logic,
mission-state evaluation, and scenario-based validation.

---

## Scope & Intent

Mission-Sim is intentionally limited in scope.

It is designed to:
- support mission-level decision logic
- model environmental and system constraints
- validate autonomy behavior through simulation
- provide traceable, testable autonomy decisions

It is **not** a flight simulator, control system, or hardware model.

---

## Relationship to ℵ – SYSTEMS

Mission-Sim supports ℵ – SYSTEMS’ Phase 0 work on:

- mission-state evaluation
- autonomy decision explainability
- action gating for fragile payloads
- scenario-based validation

Mission-Sim does **not** implement:
- low-level control loops
- hardware drivers
- quantum payload control
- performance-optimized orbital dynamics

---

## Current Status

**Phase 0 - Research & Capability Grounding**

- Research prototype
- API stability is *not* guaranteed
- Focused on clarity, traceability, and correctness
- All behavior is simulation-only

---

## Core Concepts

Mission-Sim currently centers on:

- **Mission states**  
  (`NOMINAL`, `CONSTRAINED`, `DEGRADED`, `SAFE`)

- **Autonomy decisions**  
  Deterministic evaluation of system and environment indicators

- **Action gating**  
  Explicit permission or prohibition of quantum operations

- **Decision traceability**  
  Every autonomy decision produces an explainable trace

---

## Quick Start (Research Use)

### Requirements
- Python 3.10+
- No external services
- No hardware dependencies

### Install (local)

```bash
git clone https://github.com/SPACE-ALEPH/mission-sim.git
cd mission-sim
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
