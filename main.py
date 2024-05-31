from environs import Env

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, BotCommand

env = Env()
env.read_env()

# bot_token = env("BOT_TOKEN")

bot = Bot(token=env("BOT_TOKEN"))
dp = Dispatcher()

@dp.startup.register
async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/start', description='Start'),
        BotCommand(command='/help',  description='Help'),
    ]

    await bot.set_my_commands(main_menu_commands)

@dp.message(Command(commands=["start"]))
async def start_command(message: Message):
    await message.answer("Hello! Bot is working! :)")

@dp.message(Command(commands=["help"]))
async def help_command(message: Message):
    await message.answer(
        "Send me something.\n"
        "I\'ll repeat your message!"
    )

@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            "Can\'t reply to this message :("
        )

if __name__ == "__main__":
    dp.run_polling(bot)
