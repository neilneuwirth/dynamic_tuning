from typing import List
import os

import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")


def get_embedding(text: str, engine="text-embedding-ada-002", **kwargs) -> List[float]:
    return openai.Embedding.create(input=[text], engine=engine, **kwargs)["data"][0][
        "embedding"
    ]


def get_chat(messages, model: str = "gpt-3.5-turbo", temperature=0, **kwargs):
    response = openai.ChatCompletion.create(
        messages=messages, model=model, temperature=temperature, **kwargs
    )
    return response["choices"][0]["message"]["content"]
