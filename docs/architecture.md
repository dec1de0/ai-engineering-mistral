# Architecture

## Overview
The repository is a deliberately layered system: a minimal frontend calls a FastAPI backend, which delegates generation to a service layer and a model loader. The model loader is intentionally incomplete so students integrate a quantized Mistral 7B runtime.

## Data Flow
1. **Frontend** sends `POST /generate` with `{ "text": "..." }`.
2. **API route** validates the request and forwards the prompt to the inference service.
3. **Inference service** requests a model instance from the model loader and calls `generate()`.
4. **Model loader** should initialize and cache the quantized Mistral 7B runtime (student work).
5. **Response** is returned as `{ "response": "..." }`.

## Model Loader Contract
- Load the quantized Mistral 7B runtime once and cache it.
- Return a concrete object that implements `generate(prompt) -> str`.
- Pull runtime settings from `configs/model_config.py`.
- Raise clear configuration errors when the model path is missing or invalid.

## Deployment and Validation
The grading tests exercise your **deployed** API endpoint. Ensure the backend is publicly reachable and that the hosted service uses the same layered architecture. Local-only changes that bypass the model loader will not pass evaluation.

## Why This Layered Design
- **Separation of concerns**: routing, inference logic, and model loading are isolated.
- **Testability**: each layer can be tested or swapped without breaking the API contract.
- **Maintainability**: model integrations are localized to one module, preventing sprawl.

## Where Students Should Work
- `backend/models/model_loader.py`: integrate the quantized Mistral 7B runtime.
- `configs/model_config.py`: configure model path and runtime settings.
- Optional: update `backend/services/inference_service.py` to match your runtime API.

## What to Avoid Changing
- The `/generate` API contract.
- The request/response schemas in `backend/schemas/request_response.py`.
- The test expectations in `backend/tests/test_api.py`.

The architecture is designed so students must wire a real model runtime without bypassing the loader or rewriting the API.
