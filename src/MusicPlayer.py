import vlc
from Spotty import ExtractPlaylist
from LinkGrabber import LinkGrabber

class MusicPlayer:
    """ A class for the music player.

        Args:
            playlist_ID (str): The Spotify playlist ID.
    """
    def __init__(self, playlist_ID):
        
        if not playlist_ID:
            raise ValueError("Please provide a playlist ID!")
        
        self.extract_playlist = ExtractPlaylist(playlist_ID)
        self.link_grabber = LinkGrabber()
        self.node = self.extract_playlist.playlist.head
        self.url = self.link_grabber.get_music_url(self.node.data)
        self.player = vlc.Instance('--no-video', '--quiet').media_player_new()
        self.volume = 38
        self.player.audio_set_volume(self.volume)
        self.listening = True
        self.playing = False
        self.paused = False
        self.volume_up = False
        self.volume_down = False
        self.next_track = False
        self.previous_track = False
        self.current_track = "Press Play to play music!"
        self.state = vlc.State.NothingSpecial
    
    def update_state(self):
        """ Update the state of the player. If the song has ended go to the next song.
        """
        self.state = self.player.get_state()
        if self.state == vlc.State.Ended:
            self.next_or_previous()

    def play(self):
        """ Play the song depending on the state of the player.
        """
        if self.state == vlc.State.Playing:
            return
        if self.state == vlc.State.NothingSpecial:
            media = vlc.Media(self.url)
            self.player.set_media(media)
            self.current_track = self.node.data
        if self.state == vlc.State.Paused:
            self.player.pause()
        self.player.play()

    def next_or_previous(self, previous=False):
        """ Play the next or previous track based on what button is clicked.

            Args:
                previous (bool): If we want to go to the previous track. Default is False.
        """
        self.next_track = True
        if self.state == vlc.State.Playing:
            self.player.stop()
        if previous:
            if self.node.previous:
                self.node = self.node.previous
            self.node = self.node
        else:
            if not self.node.next:
                self.node = self.extract_playlist.playlist.head
            self.node = self.node.next
        self.url = self.link_grabber.get_music_url(self.node.data) if self.node else self.url
        media = vlc.Media(self.url)
        self.player.set_media(media)
        self.current_track = self.node.data if self.node else self.current_track
        self.state = vlc.State.NothingSpecial
        self.play()        

    def pause(self):
        """ Pause the player.
        """
        self.player.pause() 
