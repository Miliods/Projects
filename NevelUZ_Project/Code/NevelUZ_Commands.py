from aiogram.types import BotCommand

commands = [
    BotCommand(command='menu', description='Главное меню'),
    BotCommand(command='catalog', description="Каталог товаров 🗂"),
    BotCommand(command='basket', description='Корзина 🛍'),
    BotCommand(command='favorites', description='Избранные ❤️'),
    BotCommand(command='settings', description='Настройки ⚙️')
]
