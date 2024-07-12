from aiogram import Bot
from config import settings
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode



# bot_tocken = '7015654889:AAGfqITjIMdqddzVmdCUy6TPM7vdMByfpRY'


bot = Bot(token=settings.BOT_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))