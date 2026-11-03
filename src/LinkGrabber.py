import yt_dlp as yt

class LinkGrabber:
    """ Class to setup the yt_dlp options and fetch the url for the requested song.
    """
    def __init__(self):
        self.opts = {
            "format": "bestaudio/best",
            "noplaylist": True,
            "quiet": True,
            "no_warnings": True,
            "extract_flat": False,
            "skip_download": True
        }

    def get_music_url(self, artist_song_name):
        """ Get the yt_dlp url with the supplied artist + song name.

            Args:
                artist_song_name (str): The artist song name to search for.

            Returns:
                str: The url for the song that was searched.
        """
        search_YT = f"ytsearch1:{artist_song_name}"
        with yt.YoutubeDL(self.opts) as yst:
            yt_results = yst.extract_info(search_YT, download=False)
        entries = yt_results.get('entries')
        if not entries:
            raise ValueError(f"No song found for {artist_song_name}")
        return entries[0]['url']
