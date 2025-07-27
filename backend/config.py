from dotenv import load_dotenv
import os

load_dotenv() 

# API KEYS
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# LOCAL MODELS 
USE_LOCAL_MODEL = False  # ← change à False pour utiliser OpenRouter
LOCAL_MODEL_NAME = "mistral:7b"

# OPENROUTER MODELS
QWEN_2_5_72B = "qwen/qwen-2.5-72b-instruct:free"