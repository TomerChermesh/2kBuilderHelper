from typing import Final

from src.constants.ai import GPT_MODEL
from src.constants.sources import SRC_2K_RATINGS

DESCRIPTION: Final[str] = ("🏀 Here you can get the latest NBA player details for update them inside the game or create "
                           "to them from scratch using an AI agent to make it quick and without missing any parameter."
                           f"\n\n🏀 Current AI model: {GPT_MODEL}\n\n🏀 I'm currently working only with 2k24 builder.")
BUILDER_HELPER_BOT: Final[str] = '2k Builder Helper bot'
HELLO: Final[str] = f"*Hello! It's {BUILDER_HELPER_BOT}* 🎮🤖"
API: Final[str] = (f"🏀 Most of the data is taken from {SRC_2K_RATINGS}. I'm also using the Wikipedia, Google and "
                   f"more sources all aggregated by our ChatGPT exclusive agent.")
START_COMMAND: Final[str] = f"/start -> Start using {BUILDER_HELPER_BOT}"
HELP_COMMAND: Final[str] = "/help -> This message"
ABOUT_COMMAND: Final[str] = f"/about -> Read about {BUILDER_HELPER_BOT}"

CHOOSE_2K_VERSION: Final[str] = 'Please choose 2k builder version'
ENTER_PLAYER_NAME: Final[str] = "Please enter a NBA player's full name 🙏🏼"
GOODBYE: Final[str] = "Thank you! Hope to see you next time 👋🏼"
INVALID_ANSWER: Final[str] = "Invalid answer 😣"
INVALID_PLAYER: Final[str] = "Player do not exist 😣"
RETURN_TO_MENUS: Final[str] = "Please select a menu to return to or exit 🙏🏼"
SELECT_DEPARTMENT: Final[str] = "Please select one of the following build departments 🎯"
