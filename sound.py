import pygame
def error():
    pygame.init()
    pygame.mixer.music.load("effect/den.mp3")
    pygame.mixer.music.play()

    # Add a delay to ensure the audio plays completely
    pygame.time.wait(2000)  # Wait for 3 seconds

    pygame.mixer.music.stop()
    pygame.quit()

def accpet():
    pygame.init()
    pygame.mixer.music.load("effect/app.mp3")
    pygame.mixer.music.play()

    # Add a delay to ensure the audio plays completely
    pygame.time.wait(1000)  # Wait for 3 seconds

    pygame.mixer.music.stop()
    pygame.quit()

# i = int(input("interi number "))
# if i == 1:
#     accpet()
# else:
#     error()