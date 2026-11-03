from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
from MusicPlayer import MusicPlayer 

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 100
BUTTON_WIDTH = 20
BUTTON_HEIGHT = 20

class MusicPlayerGUI(QWidget):
    """ Class for the gui of the music player.

        Args:
            playlistID (str): The spotify ID of the playlist to extract the songs from.
    """
    def __init__(self, playlistID: str):
        self.app = QApplication([])
        self.mp = MusicPlayer(playlistID)
        super().__init__()
        
        # Layout initializations.
        self.main_layout = QVBoxLayout()
        self.btn_layout = QHBoxLayout()
        self.txt_layout = QHBoxLayout()
        self.main_layout.addLayout(self.btn_layout)
        self.main_layout.addLayout(self.txt_layout)

        # Window initialization and settings.
        self.window = QWidget()
        self.window.setWindowTitle("Music Player")
        self.window.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.style_sheet()
        self.create_and_add_button()

        # This uses QTimer to update with interval every half a second.
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.update)
        self.timer.start()

    def draw(self):
        """ Draw the window.
        """
        self.window.show()
    
    def style_sheet(self):
        """ Apply the stylesheet to our application.
        """
        with open('stylesheet.qss', 'r') as f:
            _style = f.read()
            self.app.setStyleSheet(_style)

    def create_and_add_button(self):
        """ Create and add buttons to the GUI.
        """
        # Previous button creation and addition.
        previous_button = QPushButton("<<")
        previous_button.setGeometry(60, WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
        previous_button.clicked.connect(self.prev_pressed)
        self.btn_layout.addWidget(previous_button)

        # Next button creation and addition.
        next_button = QPushButton(">>")
        next_button.setGeometry(80, WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
        next_button.clicked.connect(self.next_pressed)
        self.btn_layout.addWidget(next_button)

        # Play button creation and addition.
        play_button = QPushButton(">")
        play_button.setGeometry(40, WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
        play_button.clicked.connect(self.play_pressed)
        self.btn_layout.addWidget(play_button)

        # Pause button creation and addition.
        pause_button = QPushButton("||")
        pause_button.setGeometry(20, WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
        pause_button.clicked.connect(self.pause_pressed)
        self.btn_layout.addWidget(pause_button)
        
        # Set the track and artist name on the player.
        self.song_name = QLabel(self.mp.current_track)
        self.song_name.setGeometry(300, WINDOW_HEIGHT, 100, 100)
        self.txt_layout.addWidget(self.song_name, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Set the main layout to the window.
        self.window.setLayout(self.main_layout)
        
    def update(self):
        """ Update the GUI to display the current track.
        """
        self.mp.update_state()
        if self.song_name.text() != self.mp.current_track:
            self.song_name.setText(self.mp.current_track)

    def play_pressed(self):
        """ Play button pressed event.
        """
        self.mp.play()

    def next_pressed(self):
        """ Next button pressed event.
        """
        self.mp.next_or_previous()
    
    def prev_pressed(self):
        """ Previous button pressed event.
        """
        self.mp.next_or_previous(previous=True)
    
    def pause_pressed(self):
        """ Paused button pressed event.
        """
        self.mp.pause()
