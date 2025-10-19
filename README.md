# Alpha.Ai — Multi‑Agent Trading System (Full Package)

**License:** Apache-2.0

## Overview
Alpha.Ai is a full-stack multi-agent trading system (prototype). It includes:
- Agent templates (Market, Strategy, Decision, Execution, Risk, Reflect)
- Event-driven pipelines (Kafka-compatible patterns)
- Wallet manager for multi-wallet support
- Frontend scaffold (React) and backend API (FastAPI) stubs
- Backtesting & replay utilities (vectorbt-ready)
- CI/CD and deployment scripts (Helm/Kubernetes placeholders)
- Voice assistant integration points (STT/TTS + LLM hooks)

## Quick start (dev)
1. Extract the repo and review `env.example` for required env variables.
2. Use Docker Compose (provided) to spin up local services for development and testing.
3. Use `scripts/setup_alphaai_repo.sh` to create a GitHub repo and push (requires `gh` CLI).

## Structure
See `/src`, `/charts`, `/docs` for detailed components.

## Contact
This repo was prepared for DD505818 by the Alpha.Ai engineering assistant.
