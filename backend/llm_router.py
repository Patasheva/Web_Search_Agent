from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel
import config

def get_llm() -> BaseChatModel:
    if config.USE_LOCAL_MODEL:
        return ChatOllama(model=config.LOCAL_MODEL_NAME)
    else:
        return ChatOpenAI(
            model=config.QWEN_2_5_72B,
            api_key=config.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
        )