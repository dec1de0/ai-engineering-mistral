from llama_cpp import Llama
from huggingface_hub import hf_hub_download
from configs.model_config import (
    MAX_NEW_TOKENS,
    TEMPERATURE,
    TOP_P,
)

REPO_ID = "TheBloke/Mistral-7B-v0.1-GGUF"
MODEL_FILE = "mistral-7b-v0.1.Q4_K_M.gguf"

class ModelNotConfiguredError(RuntimeError):
    pass

_model = None

class MistralModel:
    def __init__(self, llm):
        self.llm = llm

    def generate(self, prompt: str) -> str:
        output = self.llm(
            prompt,
            max_tokens=MAX_NEW_TOKENS,
            temperature=TEMPERATURE,
            top_p=TOP_P,
        )
        return output["choices"][0]["text"].strip()

def load_model():
    global _model
    if _model is None:
        model_path = hf_hub_download(repo_id=REPO_ID, filename=MODEL_FILE)
        llm = Llama(
            model_path=model_path,
            n_ctx=256,
            n_threads=2,
            n_gpu_layers=-1,
            n_batch=8,
        )
        _model = MistralModel(llm)
    return _model