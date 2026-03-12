from backend.services import inference_service


def test_inference_service_calls_model_loader(monkeypatch):
    calls = {"count": 0, "prompt": None}

    class DummyModel:
        def generate(self, prompt: str) -> str:
            calls["prompt"] = prompt
            return f"echo: {prompt}"

    def fake_load_model():
        calls["count"] += 1
        return DummyModel()

    monkeypatch.setattr(inference_service, "load_model", fake_load_model)

    output = inference_service.generate_response("hello")

    assert output == "echo: hello"
    assert calls["count"] == 1
    assert calls["prompt"] == "hello"
