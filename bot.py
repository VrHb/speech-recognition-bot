import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from loguru import logger

from audio_file_operations import audio_convert, audio_recognition, FFmpeg 


logger.add(
        "debug.log", format='{time} {level} {message}',
        level='DEBUG', serialize=True
        )

load_dotenv()
API_TOKEN = os.getenv("TGBOT_TOKEN")
bot = Bot(token=(str(API_TOKEN)))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message) -> None:
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer(
        f"* Привет\! Я Спайк*\! \nЧеловеческие бобы много говорят?\n"
        f"Я тебе с этим помогу, буду переводить голосовые сообщения в текст\n"
        f"[Спайк](https://en.wikipedia.org/wiki/List_of_The_Land_Before_Time_characters#Spike)",
        parse_mode="MarkdownV2"
    )


@dp.message_handler(content_types=['voice', 'audio'])
async def get_audio_messages(message: types.Message) -> None:
    """handle audio from user, transcribe and dend text answer"""
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    logger.info(file_path)
    await bot.download_file(file_path, FFmpeg.FILE_IN)
    await audio_convert()
    message_text = await audio_recognition()
    await message.answer(message_text)
     

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

