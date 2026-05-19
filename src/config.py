import os
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.getenv(
    "GROK_API_KEY"
)

MODEL_NAME = "grok-3-mini"

BASE_URL = "https://api.x.ai/v1"

MAX_NEIGHBORS = 5