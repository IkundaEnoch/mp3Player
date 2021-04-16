# imports
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # hides the annoying welcome message from pygame
from pygame import mixer, time # mixer is for audio playback, time monitors time (duh)
song = "01 Feel Like I Do.mp3" # the name of the test song (Artist: Vin Diesel)
mixer.init()                   # initializes the mixer
mixer.music.load(song)         # loads a song for playback
mixer.music.play()             # plays the song
print("Now Playing: " + song)
# this loop monitors the playback. Otherwise, the play() function will only play the buffer size.
while mixer.music.get_busy():
    time.Clock().tick(10)
    mp3_command = input("Type a command to stop,pause,unpause: ")
    if mp3_command == "stop":
        mixer.music.stop()
    elif mp3_command == "pause":
        mixer.music.pause()
        mp3_command = input("Type a command to stop,pause,unpause:")
        if mp3_command == "unpause":
            mixer.music.unpause()
    
    
    
    

# TODO: please god make it stop