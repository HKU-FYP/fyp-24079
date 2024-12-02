from src.core.embedding.embedding_model import EmbeddingModel
from src.core.llm.utils import load_prompt_messages, fill_message_placeholders
from src.core.llm.openai_llm import OpenAIChatLLM
from src.config import load_config
from pprint import pprint


def main():
    cfg = load_config()

    STOCK_NAME = "Coca COla"

    msg = load_prompt_messages(prompt_path="src/core/llm/prompts/generate_example_prompt.txt")
    messages = fill_message_placeholders(msg, placeholders={'user_input': STOCK_NAME})

    openai = OpenAIChatLLM(
        api_key=cfg.openai.api_key,
        model=cfg.openai.chat_model,
        temperature=0.5
    )

    resp = openai.predict_json(messages)
    pprint(resp)
    
    # embedding_model = EmbeddingModel(
    #     api_key=cfg.openai.api_key,
    #     model=cfg.openai.embedding_model
    # )

    # sim = embedding_model.get_similarity_score(
    #     "hellow how are you",
    #     "hi how are you doing?"
    #     )
    # print(sim)


if __name__ == '__main__':
    main()