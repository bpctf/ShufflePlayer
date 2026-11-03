import argparse
import sys
from MusicGUI import MusicPlayerGUI

def extract_playlist_id(playlist):
    """ Parse the CLI argument.

        Args:
            playlist (str): The playlist from Spotify.

        Returns:
            str: The playlist id from Spotify.
    """
    if "http" in playlist or "spotify" in playlist or "spot" in playlist:
        if playlist.endswith("/"):
            return playlist[:-1].split("/")[-1]
        return playlist.split("/")[-1]
    return playlist

def parse_args():
    """ Parse the args of the command line.
    
        Returns:
            argparse.Namespace: An object containing the parsed arguments as attributes.
    """
    parser = argparse.ArgumentParser(description="Music player that extracts songs from a Spotify playlist and uses yt_dlp and VLC to play them")
    parser.add_argument("playlistID", help="The playlist ID or the spotify playlist link")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    playlistID = extract_playlist_id(args.playlistID)
    mplayer = MusicPlayerGUI(playlistID)
    mplayer.draw()
    sys.exit(mplayer.app.exec())

