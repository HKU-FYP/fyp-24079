import os
from dataclasses import dataclass
from dotenv import load_dotenv

@dataclass
class OpenAIConfig:
    api_key: str
    embedding_model: str
    chat_model: str


@dataclass
class AppConfig:
    openai: OpenAIConfig


def load_config() -> AppConfig:
    load_dotenv(".env")

    openai_config = OpenAIConfig(
        api_key=os.environ['OPENAI_API_KEY'],
        embedding_model='text-embedding-ada-002',
        chat_model='gpt-4o-mini'
    )

    app_config = AppConfig(
        openai=openai_config
    )
    return app_config