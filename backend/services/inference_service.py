from backend.models.model_loader import load_model


class InferenceServiceError(RuntimeError):
    """Raised when inference fails for reasons other than configuration."""


def generate_response(prompt: str) -> str:
    """Generate a response from the loaded model.

    This function intentionally assumes the model implements a `generate` method.
    Students will wire up the actual quantized runtime in `model_loader.py`.
    """
    model = load_model()

    try:
        return model.generate(prompt)
    except Exception as exc:  # pragma: no cover - depends on student implementation
        raise InferenceServiceError("Model inference failed.") from exc
