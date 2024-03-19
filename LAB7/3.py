import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
is_red = True
x = 30
y = 30
radius = 25
screen_width, screen_height = 800, 600 

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_red = not is_red
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y - radius > 0: y -= 20
        if pressed[pygame.K_DOWN] and y + radius < screen_height: y += 20
        if pressed[pygame.K_LEFT] and x - radius > 0: x -= 20
        if pressed[pygame.K_RIGHT] and x + radius < screen_width: x += 20
        
        screen.fill((255, 255, 255))
        if is_red: color = (255, 0, 0)
        else: color = (0, 0, 0)
        pygame.draw.circle(screen, color, (x, y), 25)

        pygame.display.flip()
        clock.tick(60)