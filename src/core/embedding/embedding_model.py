from openai import OpenAI
import numpy as np

class EmbeddingModel:
    def __init__(
        self,
        api_key: str,
        model: str = 'text-embedding-ada-002'
    ):
        self.model = model
        self.client = OpenAI(api_key=api_key)
    
    def get_embedding(self, text: str) -> list[float]:
        text = text.replace("\n", " ")
        return self.client.embeddings.create(input = [text], model=self.model).data[0].embedding

    def cosine_similarity(self, emb1: list[float], emb2: list[float]) -> float:
        return np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))

    def get_similarity_score(self, text1: str, text2: str) -> float:
        emb1 = self.get_embedding(text1)
        emb2 = self.get_embedding(text2)
        return self.cosine_similarity(emb1, emb2)
