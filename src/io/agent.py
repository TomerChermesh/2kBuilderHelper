from typing import Optional

from openai import OpenAI
from openai.types.chat import ChatCompletion

from src.constants.ai import GPT_MODEL
from src.core.config import OPENAI_API_KEY
from src.core.custom_exceptions import InvalidVersion
from src.core.version_manager import VersionManager
from src.utils.instructions import get_instructions_versions_list, load_instructions

client = OpenAI(api_key=OPENAI_API_KEY)


class GPTAgent:
    client: OpenAI
    version_manager: VersionManager

    def __init__(self):
        self.model = GPT_MODEL
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.version_manager = VersionManager()
        self.versions = get_instructions_versions_list()

    def is_player_exists(self, player_name: str) -> bool:
        pass

    def get_player_data(self, player_name: str, departments) -> str:
        pass

    def chat(self, prompt: str) -> str:
        response: ChatCompletion = client.chat.completions.create(
            model=self.model,
            messages=[
                {'role': 'system', 'content': 'You are a 2k players stats helper.'
                                              'use https://www.2kratings.com/ as your source for attributes, stats,'
                                              'hot zones, and badges. Badges must be mentioned with their color.'
                                              'For the General Info and Vitals - use wikipedia if needed.'},
                {'role': 'user', 'content': prompt}
            ]
        )

        return response.choices[0].message.content.strip()
