import asyncio
import logging
import re
import tempfile

from pathlib import Path
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, Message
from yt_dlp import YoutubeDL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "YOUR_TOKEN"

dp = Dispatcher()

YOUTUBE_URL_PATTERN = re.compile(r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+")


async def download_youtube_audio(url: str, temp_dir: Path) -> Path:
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(temp_dir / "%(title)s.%(ext)s"),
        "ffmpeg_location": "C:/FFmpeg/bin",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
    }
    logger.info(f"Starting to download the audio from the link: {url}")
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        downloaded_file_path = Path(ydl.prepare_filename(info)).with_suffix(".mp3")
        logger.info(f"File downloaded: {downloaded_file_path}")
        return downloaded_file_path


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Hello, {message.from_user.full_name}! Send me the YouTube link and I'll try to get the audio back in the best quality possible."
    )


@dp.message()
async def yt_handler(message: Message) -> None:
    yt_url = message.text.strip()
    if not YOUTUBE_URL_PATTERN.match(yt_url):
        await message.answer("It doesn't look like a valid YouTube link.")
        return
    with tempfile.TemporaryDirectory() as temp_dir_name:
        temp_dir = Path(temp_dir_name)
        try:
            mp3_file_path = await download_youtube_audio(yt_url, temp_dir)
            title = mp3_file_path.stem
        except Exception:
            logger.exception("Error downloading audio")
            await message.answer(
                "An error occurred while processing the link. Please make sure the link is correct and try again."
            )
            return
        audio_file = FSInputFile(mp3_file_path)
        await message.answer_audio(audio_file, caption=f"Here's your audio: {title}")


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
