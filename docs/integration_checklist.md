# Integration Checklist

## Setup
- Create and activate a virtual environment.
- Install backend dependencies from `backend/requirements.txt`.
- Run the backend once and observe the expected `503` error for missing model configuration.

## Model Acquisition
- Choose a quantized Mistral 7B artifact suitable for CPU-only inference.
- Verify the file path and format (for example, GGUF).

## Configuration
- Update `configs/model_config.py` with the correct `MODEL_PATH` and generation settings.
- Confirm the path exists on disk before running tests.

## Model Loader Implementation
- Implement `load_model()` in `backend/models/model_loader.py`.
- Initialize the quantized runtime once and cache it.
- Return an object that exposes `generate(prompt) -> str`.
- Keep the API contract unchanged.

## Inference Validation
- Call `POST /generate` with a sample prompt and confirm a non-empty response.
- Verify the response changes when prompts change.

## Testing
- Run `./scripts/run_tests.sh` and confirm all tests pass.
- Fix failures by improving integration, not by weakening tests.

## Deployment
- Deploy the backend to a free-tier hosting provider.
- Confirm the public URL responds to `POST /generate` with a non-empty response.
- Export `DEPLOYED_API_URL` before running tests locally.

## Deliverables
- A short write-up describing your integration decisions and tradeoffs.
- A demo or screenshots showing end-to-end operation.
