# YouTube Video Downloader

A simple Flask-based web application that allows users to download YouTube videos. The app uses `yt-dlp` to download videos in different qualities, preview thumbnails, and automatically deletes downloaded videos after 1 minute to keep the server clean.

![Powered by yt-dlp](https://raw.githubusercontent.com/yt-dlp/yt-dlp/master/.github/banner.svg)

## Features
- **Download YouTube videos**: Users can download videos in low, medium, or best quality.
- **Preview thumbnails**: Shows a preview thumbnail of the video before downloading.
- **Automatic cleanup**: Downloaded videos are automatically deleted after 1 minute to prevent server clutter.

## Tech Stack
- **Backend**: Flask (Python web framework)
- **Video Downloading**: yt-dlp (for downloading videos)
- **Web UI**: HTML, CSS, and JavaScript
- **Temporary storage**: Downloads are stored temporarily in a folder and auto-deleted.

## Prerequisites
- Python 3.x
- `yt-dlp`
- `Flask`

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/yt-video-downloader.git
   cd yt-video-downloader
   
