from src.constants.messages import (ABOUT_COMMAND, API, BUILDER_HELPER_BOT, DESCRIPTION, HELLO, HELP_COMMAND,
                                    INVALID_ANSWER, START_COMMAND)


def get_invalid_message_with_last_message(last_message: str, invalid_text: str = INVALID_ANSWER) -> str:
    return f'{invalid_text}\n\n{last_message}'


def get_about_message() -> str:
    return f'*About {BUILDER_HELPER_BOT}* 🦁\n\n{DESCRIPTION}!\n\n{API}'


def get_help_message() -> str:
    return f'The following commands are available:\n\n' \
           f'{START_COMMAND}\n' \
           f'{ABOUT_COMMAND}\n' \
           f'{HELP_COMMAND}'


def get_start_message() -> str:
    return f'{HELLO}\n\n{DESCRIPTION}'
