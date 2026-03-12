const API_URL = "http://localhost:8000/generate";

const form = document.getElementById("prompt-form");
const promptInput = document.getElementById("prompt");
const generateBtn = document.getElementById("generate-btn");
const statusEl = document.getElementById("status");
const responseText = document.getElementById("response-text");
const responseBadge = document.getElementById("response-badge");
const errorText = document.getElementById("error-text");

function setState({ status, badge, message, error }) {
  statusEl.textContent = message || "";
  responseBadge.textContent = badge;
  responseBadge.dataset.state = status;
  errorText.textContent = error || "";
}

async function handleSubmit(event) {
  event.preventDefault();

  const prompt = promptInput.value.trim();
  if (!prompt) {
    setState({
      status: "error",
      badge: "Error",
      message: "Please enter a prompt.",
      error: "Prompt cannot be empty.",
    });
    return;
  }

  setState({ status: "loading", badge: "Loading", message: "Generating response..." });
  generateBtn.disabled = true;
  responseText.textContent = "";

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: prompt }),
    });

    const payload = await response.json().catch(() => null);

    if (!response.ok) {
      const detail = payload?.detail || "Unexpected server error.";
      throw new Error(detail);
    }

    responseText.textContent = payload.response;
    setState({ status: "success", badge: "Success", message: "Response generated." });
  } catch (error) {
    responseText.textContent = "";
    setState({
      status: "error",
      badge: "Error",
      message: "Generation failed.",
      error: error.message,
    });
  } finally {
    generateBtn.disabled = false;
  }
}

form.addEventListener("submit", handleSubmit);
