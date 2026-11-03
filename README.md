# Spotify Playlist Player

A Python-based music player that integrates with the Spotify API to retrieve playlist tracks and provide a custom playlist experience.

## Features

- **Spotify API Integration:** Retrieves playlist information and track data using the Spotify Web API.
- **Playlist Extraction:** Fetches playlist tracks, including support for paginated API responses.
- **Custom Data Structure:** Uses a custom implementation of a linked list to store and manage playlist tracks.
- **Playlist Shuffling:** Randomizes track order using the linked list implementation.
- **Graphical User Interface:** Provides an interface for interacting with the application.

## Technologies Used

- Python
- Spotipy
- Spotify Web API
- Python-vlc
- PyQt6
- yt-dlp

## Project Structure

```text
spotify-playlist-player/
├── src/
│   ├── LinkGrabber.py
│   ├── LinkedList.py
│   ├── MusicGUI.py
│   ├── MusicPlayer.py
│   ├── Spotty.py
│   └── main.py
├── README.md
├── requirements.txt
└── stylesheet.qss
```

## Requirements

- Python 3.10 or later
- Spotify Developer account
- Spotify API credentials

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bpctf/ShufflePlayer   
   cd ShufflePlayer
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   **Linux/macOS**
   ```bash
   source venv/bin/activate
   ```

   **Windows**
   ```bash
   venv\Scripts\activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create an application through the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).

Configure the following environment variables using your Spotify application credentials:

```text
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
```

Do not commit your credentials to version control.

## Usage

Run the application from the project root:

```bash
python src.main
```

Provide a Spotify playlist ID or URL when prompted.

