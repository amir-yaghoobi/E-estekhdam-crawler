from telegram import Bot
from telegram import ParseMode


class NotificationBot:

    def __init__(self, bot_token, channel_id):
        if not isinstance(bot_token, str) or not isinstance(channel_id, int):
            raise ValueError('invalid arguments.')

        self.bot_token = bot_token
        self.channel_id = channel_id
        self.telegram = Bot(bot_token)

    def send_message(self, msg):
        self.telegram.send_message(self.channel_id, msg, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
