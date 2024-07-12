from aiogram.types import BotCommand


# Функция для настройки кнопки Menu бота
async def set_main_menu(bot):
    # Создаем список с командами и их описанием для кнопки menu

    main_menu_commands = [
        BotCommand(command='/back',
                   description='Kommen zurück zum Menu'),

        BotCommand(command='/slide_show',
                   description='Schauen Sleiden'),

        BotCommand(command='/bookmarks',
                   description='Bookmarks'),

        BotCommand(command='/help',
                   description='Bot commands')]

    await bot.set_my_commands(main_menu_commands)

