import asyncio

import speech_recognition as sr

class ffmpeg():
    PROGRAM = "ffmpeg"
    FLAG1 = '-i'
    FILE_IN = 'voice.ogg'
    FILE_OUT = 'voice.wav'
    FLAG2 = '-y'


async def audio_convert() -> None:
    """Run the convert process by ffmpeg converter with asyncio subprocess"""
    process = await asyncio.create_subprocess_exec(
            ffmpeg.PROGRAM, ffmpeg.FLAG1, 
            ffmpeg.FILE_IN, ffmpeg.FILE_OUT, ffmpeg.FLAG2
            )
    await process.wait()


async def audio_recognition(file: str=ffmpeg.FILE_OUT) -> str:
    """Process recognize speech from audio file"""
    r = sr.Recognizer()
    user_audio_file = sr.AudioFile(file)
    with user_audio_file as source:
        user_audio = r.record(source)
    try:
        message_text = r.recognize_google(user_audio, language='ru-RU')
        return str(message_text)
    except sr.UnknownValueError:
        return "РРРРррр!\nЧто-то невнятное! Еще разок ..."

