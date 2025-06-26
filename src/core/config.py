import os
from typing import Final

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY: Final[str] = os.getenv('OPENAI_API_KEY')
TELEGRAM_BOT_TOKEN: Final[str] = os.getenv('TELEGRAM_BOT_TOKEN')
