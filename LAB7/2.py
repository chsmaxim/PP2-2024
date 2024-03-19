import pygame

pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Audio Player")


audio_files = ["bonk.mp3", "pipe.mp3", "bruh.mp3"]
current_audio_index = 0
sound = pygame.mixer.Sound(audio_files[current_audio_index])

is_playing = False

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    sound.stop()
                    is_playing = False
                else:
                    sound.play()
                    is_playing = True
            elif event.key == pygame.K_LEFT:
                current_audio_index = (current_audio_index - 1) % len(audio_files)
                sound = pygame.mixer.Sound(audio_files[current_audio_index])
                if is_playing:
                    sound.play()
            elif event.key == pygame.K_RIGHT:
                current_audio_index = (current_audio_index + 1) % len(audio_files)
                sound = pygame.mixer.Sound(audio_files[current_audio_index])
                if is_playing:
                    sound.play()
            elif event.key == pygame.K_s:
                sound.stop()
                is_playing = False

    pressed = pygame.key.get_pressed()

pygame.mixer.quit()
pygame.quit()
