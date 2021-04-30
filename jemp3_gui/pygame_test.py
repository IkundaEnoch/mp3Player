import pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # used to hide the annoying welcome message from pygame

WIDTH, HEIGHT = 390, 200 # This is the width and height of the main window
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # WIN is the main window 

# The buttons on the window. They are located in a subfolder
# Each button icon is 50 X 50 pixels
play_button    = pygame.image.load("Icons/play.png")
pause_button   = pygame.image.load("Icons/pause.png")
stop_button    = pygame.image.load("Icons/stop.png")
forward_button = pygame.image.load("Icons/forward.png")
back_button    = pygame.image.load("Icons/back.png")

pygame.display.set_caption("JEMP3") # The name of the window, as displayed at the top of the window


def song_import(): # This is the same import function we've been using
    song_list = []
    for filename in os.listdir("Songs/"):
        if filename.endswith(".mp3"):
            song_list.append("Songs/" + filename)
    song_list.sort()
    return song_list

def mp3_command(x, y, song, playlist, p):
    # This function determines which playback function to run
    # x and y are the coordinates on the window where the mouse clicked.
    # song is the song currently playing/loaded
    # playlist is the list of songs
    # p is a boolean that tracks whether playback is paused

    # since each icon is 50 pixels tall, they all have a y range of 50 - 100.
    # If someone clicks antwhere other than the above range, then the function does nothing
    if y < 50 or y > 100:
        return song, p
    # BACK
    if x >= 50 and x <= 100: 
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        index = playlist.index(song)
        song = playlist[index - 1]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
    # PAUSE
    elif x >= 130 and x <= 180 and pygame.mixer.music.get_busy() and not p:
        pygame.mixer.music.pause()
        p = True
    # UNPAUSE
    elif x >= 130 and x <= 180 and p:
        pygame.mixer.music.unpause()
        p = False
    # PLAY
    elif x >= 130 and x <= 180 and not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        p = False
    # STOP
    elif x >= 210 and x <= 260 and pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        p = False
    # SKIP
    elif x >= 290 and x <= 340:
        index = playlist.index(song)
        if index == (len(playlist) - 1):
            index = -1
        song = playlist[index + 1]
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load(song)
    return song, p


def draw_window():
    WIN.fill((255, 255, 255)) # Draws the window

    # The .blit() function draws the icons on the window
    WIN.blit(back_button, (50, 50))
    if(pygame.mixer.music.get_busy()):
        WIN.blit(pause_button, (130, 50))
    else:
        WIN.blit(play_button, (130, 50))
    WIN.blit(stop_button, (210, 50))
    WIN.blit(forward_button, (290, 50))
    pygame.display.update() # This updates the window
# ----------------------------------------------------------
def main():
    pygame.mixer.init() # initialize the player
    songs = song_import() # The song playlist
    current_song = songs[0] # defaults current song to the first song in the playlist
    running = True # Boolean used to keep the main loop running
    mousex = 0     # The X position of the mouse
    mousey = 0     # The Y position of the mouse
    paused = False # Used to determine if the player is paused
    while running: # Handles events, updates the game state, and draws the game state to the screen
        mouseClicked = False # Used to track mouse-click events. Must be reset to False every loop
        for event in pygame.event.get(): #Executes code for every event that has happened since the last iteration of the game loop.
            if event.type == pygame.QUIT: # If the program is closed, exit the loop
                running = False
            elif event.type == pygame.MOUSEBUTTONUP: # Checks to see if the mouse button was clicked
                mousex, mousey = event.pos # The XY coordinates where the mouse was clicked
                mouseClicked = True
                current_song, paused = mp3_command(mousex, mousey, current_song, songs, paused) # Determine function to execute
                
        draw_window()
    pygame.quit()
    SystemExit()

if __name__ == "__main__": main()