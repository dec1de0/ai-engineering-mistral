"""Model and runtime configuration.

Students should update these values when integrating the quantized Mistral 7B runtime.
"""

# Path to the quantized model file (e.g., GGUF). Replace with a real path.
MODEL_PATH = "backend/models/mistral-7b-v0.1.Q4_K_M.gguf"

# A short label used for logging and reporting.
MODEL_NAME = "mistral-7b-quantized"

# Quantization format or runtime hint (e.g., GGUF, GPTQ, AWQ).
QUANTIZATION_FORMAT = "GGUF"

# Generation settings.
MAX_NEW_TOKENS = 256
TEMPERATURE = 0.7
TOP_P = 0.95

# Runtime limits.
TIMEOUT_SECONDS = 30

# Backend server settings.
BACKEND_HOST = "0.0.0.0"
BACKEND_PORT = 8000
