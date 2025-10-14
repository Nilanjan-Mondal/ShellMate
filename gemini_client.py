# gemini_client.py
from google import genai

def call_gemini_generate(client, prompt: str, model: str = "gemini-2.5-flash") -> str:
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt
        )
        return getattr(response, "text", str(response))
    except Exception as exc:
        raise RuntimeError(f"Gemini API call failed: {exc}")