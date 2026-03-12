import os
import time
from typing import Optional

import httpx
import pytest

BASE_URL = os.getenv("DEPLOYED_API_URL") or os.getenv("API_BASE_URL")

if not BASE_URL:
    pytest.fail(
        "DEPLOYED_API_URL is not set. Deploy your backend and export the URL, "
        "for example: export DEPLOYED_API_URL=https://your-host"
    )

BASE_URL = BASE_URL.rstrip("/")
GENERATE_URL = f"{BASE_URL}/generate"


def request_with_retries(method: str, url: str, **kwargs) -> httpx.Response:
    last_error: Optional[Exception] = None
    for attempt in range(3):
        try:
            return httpx.request(method, url, timeout=30.0, **kwargs)
        except httpx.RequestError as exc:
            last_error = exc
            time.sleep(2 * (attempt + 1))

    pytest.fail(f"Could not reach deployed endpoint: {last_error}")


def test_generate_route_contract():
    response = request_with_retries(
        "POST",
        GENERATE_URL,
        json={"text": "Explain quantization in simple terms."},
    )

    assert response.headers.get("content-type", "").startswith("application/json")
    assert response.status_code == 200, (
        "Expected 200 from /generate after model integration. "
        f"Got {response.status_code} with payload: {response.json()}"
    )

    payload = response.json()
    assert "response" in payload
    assert isinstance(payload["response"], str)
    assert payload["response"].strip() != ""


def test_generate_missing_text():
    response = request_with_retries("POST", GENERATE_URL, json={})
    assert response.status_code == 422


def test_generate_empty_text():
    response = request_with_retries("POST", GENERATE_URL, json={"text": ""})
    assert response.status_code == 422


def test_generate_get_not_allowed():
    response = request_with_retries("GET", GENERATE_URL)
    assert response.status_code == 405
