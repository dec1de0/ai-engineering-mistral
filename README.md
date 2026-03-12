# AI Engineering Mistral Project

This repository is a starter full-stack codebase for a university AI Engineering portfolio exercise. It provides a clean, production-style skeleton with a prebuilt frontend, backend API, tests, and configuration. The model integration is intentionally missing.

Your job is to integrate a **quantized Mistral 7B** model into the existing architecture, deploy the backend, make tests pass, and explain your engineering decisions.

## Learning Objectives
- Work with a real-world codebase and layered architecture.
- Integrate a quantized LLM under CPU-only constraints.
- Preserve a strict API contract while evolving internals.
- Debug interactions across frontend, API, and model layers.
- Communicate tradeoffs clearly and professionally.

## What You Are Expected To Do
- Understand the existing architecture and API contract.
- Integrate a quantized Mistral 7B runtime in `backend/models/model_loader.py`.
- Configure model paths and runtime settings in `configs/model_config.py`.
- Preserve the `/generate` API contract.
- Deploy the backend on a free-tier hosting provider.
- Run and pass the automated tests (they target the deployed endpoint).
- Present your final architecture, code changes, and results.

## Core Rules
- Use Mistral 7B in a quantized format.
- Do not change the `/generate` API contract.
- Do not bypass the model loader layer.
- Keep changes focused and readable.
- The deployed backend must be publicly reachable over HTTPS.

## API Contract (Must Not Change)
Request JSON:
```json
{
  "text": "Explain quantization in simple terms."
}
```

Response JSON:
```json
{
  "response": "..."
}
```

Endpoint:
- `POST /generate`

## Repository Structure
- `backend/` FastAPI backend and tests.
- `frontend/` Minimal UI for interacting with `/generate`.
- `configs/` Centralized model/runtime configuration.
- `scripts/` Convenience scripts for running the backend and tests.
- `docs/` Architecture and assignment context.

## Key Files
- `backend/api/routes.py` API routes and request validation.
- `backend/services/inference_service.py` Inference service layer.
- `backend/models/model_loader.py` **Your primary integration point**.
- `configs/model_config.py` **Your primary configuration point**.
- `backend/tests/test_api.py` Contract and behavior tests (call the deployed endpoint).

## Running the Backend Locally
1. Create a virtual environment and install dependencies: `python -m venv .venv`, `source .venv/bin/activate`, `pip install -r backend/requirements.txt`.
2. Start the backend: `./scripts/run_backend.sh`.

The local API will be available at `http://localhost:8000`.

## Frontend Usage
Open `frontend/index.html` in your browser and enter a prompt. The frontend calls `POST /generate` on `http://localhost:8000`.

## Deployment Requirement
You must deploy the backend so it is publicly reachable and uses a quantized Mistral 7B runtime. The grading tests will call your deployed `/generate` endpoint directly. A local-only server will not be sufficient. Use a free-tier hosting provider of your choice.

See `docs/deployment_requirements.md` for expectations.

## Running Tests (Deployed Endpoint)
1. Deploy your backend and confirm it responds to `POST /generate`.
2. Export your public URL: `export DEPLOYED_API_URL=https://your-host`.
3. Run tests: `./scripts/run_tests.sh`.

Note: Tests call the deployed endpoint. They will fail until your remote backend is live and the model is integrated.

## Expected Initial Failure
When you run the backend or tests for the first time, you should see a `503` error such as:
- `Model path not configured. Update MODEL_PATH in configs/model_config.py.`
- `Quantized runtime not connected. Implement load_model() to initialize a Mistral 7B model.`

This is intentional and signals the missing integration work. If you run tests without setting `DEPLOYED_API_URL`, they will fail fast with a message telling you to deploy and export the URL.

## Definition of Done
- `/generate` returns `200` with a non-empty `response` for realistic prompts.
- All tests pass without modifying their assertions or API contract.
- Your model loader uses configuration from `configs/model_config.py`.
- Your deployed endpoint is reachable and stable.
- You can explain your architecture decisions and constraints.

## Integration Checklist
See `docs/integration_checklist.md` for a step-by-step path to completion.

## Common Pitfalls
- Editing the API contract or schemas to “make tests pass.”
- Bypassing the model loader in `backend/models/model_loader.py`.
- Forgetting to update `MODEL_PATH` or using a non-existent file path.
- Returning a hardcoded string instead of running real inference.
- Deploying without verifying the public endpoint.

## Branch Strategy (Recommended)
Use branches to document your progress and reasoning:
- `main` Baseline starter repository.
- `setup` Environment setup and first run.
- `model-integration` Quantized Mistral 7B runtime integration.
- `api-validation` Verifying API contract and request handling.
- `testing-debug` Test failures, fixes, and validation work.
- `presentation-final` Final polish and presentation materials.

## How This Is Graded
You are evaluated on how well you integrate the model, respect contracts, deploy reliably, and communicate your engineering decisions. See `docs/assignment_overview.md` for details.
