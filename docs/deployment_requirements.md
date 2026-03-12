# Deployment Requirements

## Summary
You must deploy the backend so it is publicly reachable over HTTPS. The grading tests call your deployed `/generate` endpoint directly.

## Minimum Requirements
- Public HTTPS URL (no VPN or local tunneling).
- Backend exposes `POST /generate` with the required JSON contract.
- Quantized Mistral 7B runtime is loaded in the deployed environment.
- The service remains reachable long enough for automated tests.

## Testing Against Deployment
Set the environment variable before running tests:
- `export DEPLOYED_API_URL=https://your-host`

The test suite uses this value to call your deployed API.
