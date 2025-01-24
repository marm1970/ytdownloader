# YouTube Downloader Bot 🎵

A Telegram bot for downloading high-quality content (audio and, in the future, more) from YouTube using **yt-dlp** and **aiogram**.

## 🚀 Features

- Download high-quality MP3 audio from YouTube links.
- Simple and intuitive Telegram bot interface.
- Temporary file handling for efficient processing.

## 🛠 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/marm1970/ytdownloader.git
   cd ytdownloader
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Linux/MacOS
   venv\Scripts\Activate.ps1     # On Windows
   ```

3. **Install the dependencies**:
   ```bash
   python -m pip install aiogram yt-dlp
   ```

4. **Install FFmpeg**:
   - Download and install FFmpeg from [FFmpeg.org](https://ffmpeg.org/).
   - Ensure the `ffmpeg` executable is added to your system's PATH or set its location in the code (e.g., `C:/FFmpeg/bin`).

5. **Set your bot token**:
   - Replace `YOUR_TOKEN` in the code with your Telegram Bot Token from [BotFather](https://core.telegram.org/bots#botfather).

## 📖 Usage

1. **Start the bot**:
   ```bash
   python main.py
   ```

2. **Interact with the bot**:
   - Open Telegram and send the `/start` command to the bot.
   - Send a valid YouTube link to receive the audio file in high quality.

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.

## 📝 License

This project is licensed under the [MIT License](LICENSE).
