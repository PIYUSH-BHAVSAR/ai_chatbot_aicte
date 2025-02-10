import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch API Key from .env
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

if not HUGGINGFACE_API_KEY:
    raise ValueError("🚨 API Key not found! Please add it to the .env file.")
