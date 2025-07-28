# Playlist-Downloader
# 🎵 YouTube Playlist Downloader

This is a Python-based GUI tool that allows you to download all videos from a YouTube playlist and convert them into MP3 audio files. It's fast, easy to use, and perfect for offline listening or archiving.

## 🚀 Features

- ✅ Paste a playlist URL and download all songs at once
- 🎶 Converts videos to high-quality MP3s
- 🧼 Clean, minimal user interface (built with Tkinter)
- 📁 Automatically organizes downloaded files
- 🔊 Shows basic metadata (title, artist, etc.)
- 📦 No ads, no bloat – just your music



## 🛠️ How It Works

1. Paste a valid YouTube playlist URL.
2. Click the "Download" button.
3. Each video will be downloaded and converted to MP3.
4. Files are saved in a `Downloads` folder locally.

## 💻 Technologies Used

- Python 3
- Tkinter (GUI)
- pytube / yt-dlp
- pydub (for MP3 conversion)

## 📦 Installation

```bash
git clone https://github.com/yourusername/youtube-playlist-downloader.git
cd youtube-playlist-downloader
pip install -r requirements.txt
python app.py
