import os
import asyncio

import speech_recognition as sr

from aiogram import Bot, Dispatcher, executor, types

from loguru import logger



API_TOKEN = os.getenv("SPIKE_API_KEY")

logger.add(
        "debug.log", format='{time} {level} {message}',
        level='DEBUG', serialize=True
        )

bot = Bot(token=(str(API_TOKEN)))
dp = Dispatcher(bot)

@logger.catch
async def audio_convert(
        program: str, flag1: str, file_out: str, flag2: str) -> None:
    await asyncio.create_subprocess_exec(program, flag1, file_out, flag2)


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
    """get audio from user and download to server .ogg file"""
    r = sr.Recognizer()
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, "voice.ogg")
    # get audio file from telegram 
    await audio_convert(
            program='ffmpeg', 
            flag1='-i', 
            file_out='voice.wav',
            flag2='-y')
    # start new function
    user_audio_file = sr.AudioFile("voice.wav")
    with user_audio_file as source:
        user_audio = r.record(source, duration=6)
    text = r.recognize_google(user_audio, language='ru-RU')
    print(text)
    await message.answer(message.text)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
