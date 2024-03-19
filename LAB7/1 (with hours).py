import pygame
import time
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600

leftarm = pygame.image.load("rightarm.png").convert_alpha()
rightarm = pygame.image.load("leftarm.png").convert_alpha()
mainclock = pygame.transform.scale(pygame.image.load("mainclock.png").convert_alpha(), (780, 600))

leftarmrect = leftarm.get_rect(center=(screen_width // 2, screen_height // 2))
rightarmrect = rightarm.get_rect(center=(screen_width // 2, screen_height // 2))

x = 10
y = 10

image_library = dict()
def load_image(path):
    global image_library
    image = image_library.get(path)
    if image is None:
        image = pygame.image.load(path)
        image_library[path] = image
    return image

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    
    current_time = time.localtime()
    hour = (current_time.tm_hour + 1.5) % 24
    minute = current_time.tm_min
    second = current_time.tm_sec
    

    hour_angle = (hour % 12) * 30 + (minute / 60) * 30 
    minute_angle = minute * 6 + (second / 60) * 6   
    second_angle = second * 6  
    

    screen.fill((0, 0, 0))
    
    screen.blit(mainclock, (x, y))
    
    
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(leftarm, (800, 600)), -hour_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(screen_width // 2, screen_height // 2 + 10))
    screen.blit(rotated_leftarm, leftarmrect)
    
    
    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(rightarm, (40.95, 682.5)), -minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(screen_width // 2, screen_height // 2 + 10))
    screen.blit(rotated_rightarm, rightarmrect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
