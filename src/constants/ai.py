from typing import Final

GPT_MODEL: Final[str] = 'gpt-4.1-mini'

BASE_SYSTEM_PROMPT: Final[str] = (f'You are assisting users in creating or updating NBA players in NBA 2K using the '
                                  f'most up-to-date data as of today. You will return information on a specific '
                                  f'player based on the chosen department, using only verified sources '
                                  f'(e.g., 2kratings.com, NBA official pages, etc.).\n\nPlease keep your language '
                                  f'clear, fun (include emojis 🎮🏀🔥), and structure your answers in a clean, '
                                  f'professional, and helpful format')

READABLE_DATE_FORMAT: Final[str] = '%B %d, %Y'
