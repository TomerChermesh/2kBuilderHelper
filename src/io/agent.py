from datetime import datetime

from openai import OpenAI
from openai.types.chat import ChatCompletion

from src.constants.ai import GPT_MODEL, BASE_SYSTEM_PROMPT, READABLE_DATE_FORMAT
from src.core.config import OPENAI_API_KEY
from src.core.version_manager import VersionManager

client = OpenAI(api_key=OPENAI_API_KEY)


class GPTAgent:
    client: OpenAI
    version_manager: VersionManager
    base_system_prompt: str

    def __init__(self):
        self.model = GPT_MODEL
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.version_manager = VersionManager()
        self.base_system_prompt = BASE_SYSTEM_PROMPT

    def is_player_exists(self, player_name: str) -> bool:
        prompt: str = (
            f'Does an active NBA player named "{player_name}" currently exist, and is he listed on trusted 2K stats '
            f'websites like 2kratings.com?\n\nPlease answer only with "yes" or "no".'
        )

        response: str = self.chat(self.base_system_prompt, prompt).lower()
        return 'yes' in response

    def get_player_data(self, player_name: str, department: str) -> str:
        if department not in self.version_manager.departments:
            return f'❌ "{department}" is not a valid build department.'

        department_instruction = self.version_manager.instructions[department]

        user_prompt = (
            f'Provide full and detailed data for NBA player "{player_name}" under the "{department}" category.\n'
            f'Follow these instructions:\n\n{department_instruction} and return it to the user by the parameters'
            f'in the order they mentioned in the instructions.'
        )

        return self.chat(self.base_system_prompt, user_prompt)

    def chat(self, system_prompt: str, user_prompt: str) -> str:
        today: str = datetime.now().strftime(READABLE_DATE_FORMAT)
        date_system_prompt_addition: str = f'\n\nAll have to be the most updated until today {today}'
        response: ChatCompletion = client.chat.completions.create(
            model=self.model,
            messages=[
                {'role': 'system', 'content': system_prompt + date_system_prompt_addition},
                {'role': 'user', 'content': user_prompt}
            ]
        )

        return response.choices[0].message.content.strip()
