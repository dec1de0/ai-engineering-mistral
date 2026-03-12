# Assignment Overview

## Course Context
This project is part of an AI Engineering portfolio exercise focused on practical model integration under real-world constraints.

## Objective
Integrate a quantized Mistral 7B model into a prebuilt full-stack system while preserving the API contract and passing automated tests.
The automated tests will call your deployed endpoint, not your local machine.

## Required Deliverables
- A working integration of a quantized Mistral 7B runtime.
- A publicly reachable deployment URL for the backend.
- Passing test suite output.
- A short engineering write-up covering architecture decisions and tradeoffs.
- A demo walkthrough showing the end-to-end system.
Include the deployment URL in your write-up or submission notes.

## Constraints
- **Do not change** the `/generate` API contract.
- **Do not bypass** the model loader layer.
- Assume **CPU-only inference** and limited memory.
- The backend must be deployed on a free-tier hosting provider and reachable over HTTPS.
- The grading tests will call the deployed endpoint, not your local machine.
- Keep changes focused, readable, and justified.

## Evaluation Mindset
Strong submissions demonstrate:
- Clear understanding of the codebase and its layers.
- Thoughtful, minimal changes that respect existing contracts.
- Correct, stable model inference with quantized artifacts.
- Evidence of debugging and verification (tests, logs, or profiling).
 - A reliable public deployment that matches the API contract.

## Evaluation Rubric (Suggested)
- **Integration correctness**: model loads, generates, and respects constraints.
- **API contract stability**: `/generate` remains unchanged and reliable.
- **Engineering clarity**: readable code and focused changes.
- **Verification**: tests pass and failures are explained.
- **Communication**: clear write-up of decisions and tradeoffs.

## What Makes a Strong Submission
- A reliable model loader with caching and error handling.
- Transparent configuration changes in `configs/model_config.py`.
- Tests passing without weakening or deleting them.
- A professional explanation of tradeoffs and limitations.

The goal is not to build an app from scratch, but to integrate a real model into a realistic system.
