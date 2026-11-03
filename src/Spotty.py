from requests import exceptions
from concurrent.futures import ThreadPoolExecutor
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.exceptions import SpotifyException, SpotifyOauthError
from LinkedList import LinkedList

class ExtractPlaylist:
    """ Class to extract the song and artist name from the Spotify playlist.

        Args:
            playlist_ID (str): The Spotify playlist ID to use.
    """
    def __init__(self, playlistID):
        self.playlist = LinkedList()
        self._create_playlist(playlistID)

    def _create_playlist(self, playlist_ID):
        """ Create and shuffle a LinkedList of "track - artist" combinations using a Spotify playlist ID.

            Args:
                playlist_ID (str): The Spotify playlist ID to use.
        """
        # Set environment variables for SPOTIPY_CLIENT_ID & SPOTIPY_CLIENT_SECRET
        spotify = Spotify(client_credentials_manager=SpotifyClientCredentials())
        
        try:
            spotify.playlist(playlist_ID, fields="id")
        
        except SpotifyOauthError as e:
            raise RuntimeError(f"Spotify authentication failed.") from e

        except exceptions.Timeout as e:
            raise RuntimeError("The spotify request timed out.") from e

        except exceptions.ConnectionError as e:
            raise RuntimeError("Unable to connect to Spotify.") from e

        except SpotifyException as e:
            if e.http_status == 429:
                raise RuntimeError("Spotify rate limit exceeded.") from e
            elif e.http_status == 404:
                raise RuntimeError("Playlist not found. Check the ID.") from e
            elif e.http_status == 400:
                raise RuntimeError("Invalid Playlist ID") from e
            else:
                raise RuntimeError(f"Spotify API Error: {e.http_status} - {e.msg}") from e

        limit = 100 # There is a limit of 100 songs per batch that we can grab.

        playlist_info = spotify.playlist_items(playlist_ID, offset=0, limit=limit)

        max_tracks = playlist_info['total']
        
        offsets = range(limit, max_tracks, limit)

        if max_tracks == 0:
            raise ValueError("Playlist is empty. Please provide a populated playlist!")
        
        with ThreadPoolExecutor(max_workers=4) as tpe:
            results = tpe.map(lambda offset: spotify.playlist_items(playlist_ID, offset=offset, limit=limit), offsets)
            for page in results:
                for x in page['items']:
                    track_name_artist = x['track']['name'] + " - " + x['track']['artists'][0]['name']
                    self.playlist.append(track_name_artist)

        self.playlist.shuffle()
