import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not os.getenv("GEMINI_API_KEY"):
    raise Exception("GEMINI_API_KEY is not set")
gemini_api_url = os.getenv("GEMINI_API_URL")
if not os.getenv("GEMINI_API_URL"):
    raise Exception("GEMINI_API_URL is not set")
gemini_api_model=os.getenv("GEMINI_API_MODEL")
if not os.getenv("GEMINI_API_MODEL"):
    raise Exception("GEMINI_API_MODEL is not set")

class Secrets:
    def __init__(self):
        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        self.GEMINI_API_URL = os.getenv("GEMINI_API_URL")
        self.GEMINI_API_MODEL = os.getenv("GEMINI_API_MODEL")

