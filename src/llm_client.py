import time

import google.api_core.exceptions
import google.generativeai as genai

from src.config import (
    GOOGLE_API_KEY,
    MODEL_NAME
)

genai.configure(api_key=GOOGLE_API_KEY)


MODELS = [
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
    "gemini-1.5-flash",
    "gemini-1.5-pro",
]

MAX_RETRIES = 5
INITIAL_BACKOFF = 2.0


def _call_model(model_name, prompt):

    model = genai.GenerativeModel(model_name)

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0
        }
    )

    return response.text.strip()


def ask_llm(prompt):

    tried = set()

    for model_name in MODELS:

        if model_name in tried:
            continue

        tried.add(model_name)

        backoff = INITIAL_BACKOFF

        for attempt in range(1, MAX_RETRIES + 1):

            try:

                return _call_model(
                    model_name,
                    prompt
                )

            except google.api_core.exceptions.ResourceExhausted:

                wait = backoff * attempt

                print(
                    "Rate limit hit for "
                    f"{model_name!r} (attempt "
                    f"{attempt}/{MAX_RETRIES}). "
                    f"Retrying in {wait}s..."
                )

                time.sleep(wait)

            except Exception as exc:

                print(
                    f"Error with {model_name!r}: "
                    f"{exc}. Trying next model."
                )

                break

    raise RuntimeError(
        "All Gemini models exhausted. "
        "Quota has been exceeded. "
        "Check your plan at "
        "https://ai.google.dev/gemini-api/docs/rate-limits"
    )