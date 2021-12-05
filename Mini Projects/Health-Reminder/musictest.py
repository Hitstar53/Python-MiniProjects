from pygame import mixer
  
# Starting the mixer
mixer.init()
  
# Loading the song
mixer.music.load("water.mp3")
  
# Setting the volume
mixer.music.set_volume(0.7)
  
# Start playing the song
mixer.music.play(-1)
  
# infinite loop
while True:
    query = input("  ")
      
    if query == 'p':
  
        # Pausing the music
        mixer.music.pause()     
    elif query == 'r':
  
        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':
  
        # Stop the mixer
        mixer.music.stop()
        break
