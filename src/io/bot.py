from telegram import Update, ReplyKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

from src.constants import actions
from src.constants import messages
from src.constants.messages import INVALID_PLAYER, INVALID_ANSWER
from src.core.config import TELEGRAM_BOT_TOKEN
from src.core.custom_exceptions import InvalidVersion
from src.io.agent import GPTAgent
from src.utils.buttons import create_buttons_list
from src.utils.messages import get_about_message, get_help_message, get_start_message, \
    get_invalid_message_with_last_message


class Bot:
    gpt_agent: GPTAgent
    selected_version: str
    selected_player: str

    def __init__(self):
        self.updater = Updater(token=TELEGRAM_BOT_TOKEN)
        self.dispatcher = self.updater.dispatcher
        self.gpt_agent = GPTAgent()
        self.selected_version = ''
        self.selected_player = ''
        self.dispatcher.add_handler(CommandHandler("about", self.about_command))
        self.dispatcher.add_handler(CommandHandler("help", self.help_command))
        self.dispatcher.add_handler(CommandHandler("start", self.start_command))
        self.dispatcher.add_handler(MessageHandler(Filters.text, self.message_handler))
        self.last_message: str = ''
        self.last_buttons: list[list[str]] = []

    @staticmethod
    def about_command(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=get_about_message(),
                                 parse_mode=ParseMode.MARKDOWN)

    @staticmethod
    def help_command(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=get_help_message(),
                                 parse_mode=ParseMode.MARKDOWN)

    @staticmethod
    def start_command(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=get_start_message(),
                                 parse_mode=ParseMode.MARKDOWN)

    @staticmethod
    def exit(update: Update, context: CallbackContext) -> None:
        print('Bot exited.')
        start_button: list[str] = create_buttons_list([actions.START])
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=messages.GOODBYE,
                                 reply_markup=ReplyKeyboardMarkup(
                                     start_button,
                                     one_time_keyboard=True,
                                     resize_keyboard=True))

    def run(self):
        print('Bot is now running...')
        self.updater.start_polling()

    def message_handler(self, update: Update, context: CallbackContext) -> None:
        answer: str = update.message.text
        self.handle_answer(update, context, answer)

    def handle_answer(self, update: Update, context: CallbackContext, answer: str) -> None:
        if answer == actions.START:
            self.start_command(update, context)
        elif answer == actions.EXIT:
            self.exit(update, context)
        elif answer in self.gpt_agent.version_manager.versions and self.last_message == messages.CHOOSE_2K_VERSION:
            self.handle_version_selection(update, context, answer)
        elif answer in self.gpt_agent.version_manager.departments and self.last_message == messages.SELECT_DEPARTMENT:
            self.get_player_department_data(update, context, answer)
        elif self.last_message == messages.ENTER_PLAYER_NAME:
            self.handle_player_selection(update, context, answer)
        else:
            self.send_error_message(update, context)

    def show_versions_menu(self, update: Update, context: CallbackContext) -> None:
        self.last_message = messages.CHOOSE_2K_VERSION
        self.last_buttons = create_buttons_list(self.gpt_agent.version_manager.versions)
        self.send_current_action_message(update, context)

    def handle_version_selection(self, update: Update, context: CallbackContext, answer: str) -> None:
        try:
            self.gpt_agent.version_manager.load_version(answer)
        except InvalidVersion as e:
            self.send_error_message(update, context, str(e))

        self.selected_version = answer
        self.last_message = messages.ENTER_PLAYER_NAME
        self.send_current_text_message(update, context, self.last_message)

    def handle_player_selection(self, update: Update, context: CallbackContext, answer: str) -> None:
        if self.gpt_agent.is_player_exists(answer):
            self.last_message = messages.SELECT_DEPARTMENT
            self.last_buttons = create_buttons_list(self.gpt_agent.version_manager.departments)
            self.send_current_action_message(update, context)
        else:
            self.send_error_message(update, context, INVALID_PLAYER)

    def get_player_department_data(self, update: Update, context: CallbackContext, department: str):
        data: str = self.gpt_agent.get_player_data(self.selected_player, department)
        self.send_current_text_message(update, context, data)
        self.show_return_to_menus_menu(update, context)

    def show_return_to_menus_menu(self, update: Update, context: CallbackContext) -> None:
        self.last_message = messages.RETURN_TO_MENUS
        self.last_buttons = create_buttons_list(actions.MENUS)
        self.send_current_action_message(update, context)

    def send_current_action_message(self, update: Update, context: CallbackContext):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=self.last_message,
            reply_markup=ReplyKeyboardMarkup(self.last_buttons, one_time_keyboard=True, resize_keyboard=True)
        )

    @staticmethod
    def send_current_text_message(update: Update, context: CallbackContext, message: str) -> None:
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.MARKDOWN)

    def send_error_message(self, update: Update, context: CallbackContext, err_message: str = INVALID_ANSWER) -> None:
        full_message: str = f'{err_message}\n\n{self.last_message}'
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=get_invalid_message_with_last_message(full_message)
        )
