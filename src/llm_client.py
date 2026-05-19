from openai import OpenAI

from src.config import (
    GROK_API_KEY,
    MODEL_NAME,
    BASE_URL
)

client = OpenAI(
    api_key=GROK_API_KEY,
    base_url=BASE_URL
)

def ask_llm(prompt):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    answer = (
        response
        .choices[0]
        .message
        .content
    )

    return answer.strip()