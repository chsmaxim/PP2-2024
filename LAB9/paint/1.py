import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((255, 255, 255))  # Filling the base layer with white color

colorRED = (255, 0, 0)
colorORANGE = (255, 127, 0)
colorYELLOW = (255, 255, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorINDIGO = (75, 0, 130)
colorVIOLET = (148, 0, 211)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

current_color = colorRED

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

currX = 0
currY = 0

prevX = 0
prevY = 0

#A variable to store the current tool
current_tool = 'brush'

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def draw_square(x1, y1, x2, y2):
    side_length = min(abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(screen, current_color, (x1, y1, side_length, side_length), THICKNESS)

def draw_right_triangle(x1, y1, x2, y2):
    pygame.draw.polygon(screen, current_color, [(x1, y1), (x1, y2), (x2, y2)], THICKNESS)

def draw_equilateral_triangle(x, y, side_length):
    height = side_length * math.sqrt(3) / 2
    pygame.draw.polygon(screen, current_color, [(x, y), (x + side_length / 2, y + height), (x + side_length, y)], THICKNESS)

def draw_rhombus(x, y, diagonal_length_1, diagonal_length_2):
    half_diag_1 = diagonal_length_1 / 2
    half_diag_2 = diagonal_length_2 / 2
    pygame.draw.polygon(screen, current_color, [(x - half_diag_1, y), (x, y - half_diag_2), (x + half_diag_1, y), (x, y + half_diag_2)], THICKNESS)

done = False

while not done:

    if not LMBpressed:
        screen.blit(base_layer, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
            
        if event.type == pygame.MOUSEMOTION:
            print("Position of the mouse:", event.pos)
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                if current_tool == 'brush':
                    pygame.draw.line(screen, current_color, (prevX, prevY), (currX, currY), THICKNESS)
                    prevX, prevY = currX, currY  # Update the previous position
                elif current_tool == 'rectangle':
                    screen.blit(base_layer, (0, 0))  # Clear the previous rectangle
                    pygame.draw.rect(screen, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif current_tool == 'circle':
                    screen.blit(base_layer, (0, 0))  # Clear the previous circle
                    radius = calculate_distance(prevX, prevY, currX, currY)
                    pygame.draw.circle(screen, current_color, (prevX, prevY), int(radius), THICKNESS)
                elif current_tool == 'eraser':
                    pygame.draw.line(screen, colorWHITE, (prevX, prevY), (currX, currY), THICKNESS)
                    prevX, prevY = currX, currY  # Update the previous position
                elif current_tool == 'square':
                    screen.blit(base_layer, (0, 0))  # Clear the previous square
                    draw_square(prevX, prevY, currX, currY)
                elif current_tool == 'right_triangle':
                    screen.blit(base_layer, (0, 0))  # Clear the previous right triangle
                    draw_right_triangle(prevX, prevY, currX, currY)
                elif current_tool == 'equilateral_triangle':
                    screen.blit(base_layer, (0, 0))  # Clear the previous equilateral triangle
                    side_length = calculate_distance(prevX, prevY, currX, currY)
                    draw_equilateral_triangle(prevX, prevY, side_length)
                elif current_tool == 'rhombus':
                    screen.blit(base_layer, (0, 0))  # Clear the previous rhombus
                    diagonal_length_1 = calculate_distance(prevX, prevY, currX, prevY)  # Distance between two points on X-axis
                    diagonal_length_2 = calculate_distance(prevX, prevY, prevX, currY)  # Distance between two points on Y-axis
                    draw_rhombus(prevX, prevY, diagonal_length_1, diagonal_length_2)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            if current_tool == 'brush':
                pygame.draw.line(screen, current_color, (prevX, prevY), (currX, currY), THICKNESS)
            elif current_tool == 'rectangle':
                pygame.draw.rect(screen, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            elif current_tool == 'circle':
                radius = calculate_distance(prevX, prevY, currX, currY)
                pygame.draw.circle(screen, current_color, (prevX, prevY), int(radius), THICKNESS)
            base_layer.blit(screen, (0, 0))

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1
            if event.key == pygame.K_r:
                print("Switched to rectangle tool")
                current_tool = 'rectangle'
            if event.key == pygame.K_b:
                print("Switched to brush tool")
                current_tool = 'brush'
            if event.key == pygame.K_c:
                print("Switched to circle tool")
                current_tool = 'circle'
            if event.key == pygame.K_e:
                print("Switched to eraser tool")
                current_tool = 'eraser'
            if event.key == pygame.K_s:
                print("Switched to square tool")
                current_tool = 'square'
            if event.key == pygame.K_t:
                print("Switched to right triangle tool")
                current_tool = 'right_triangle'
            if event.key == pygame.K_q:
                print("Switched to equilateral triangle tool")
                current_tool = 'equilateral_triangle'
            if event.key == pygame.K_h:
                print("Switched to rhombus tool")
                current_tool = 'rhombus'
            # Implement color selection
            if event.key == pygame.K_1:
                current_color = colorRED
            if event.key == pygame.K_2:
                current_color = colorORANGE
            if event.key == pygame.K_3:
                current_color = colorYELLOW
            if event.key == pygame.K_4:
                current_color = colorGREEN
            if event.key == pygame.K_5:
                current_color = colorBLUE
            if event.key == pygame.K_6:
                current_color = colorINDIGO
            if event.key == pygame.K_7:
                current_color = colorVIOLET
            if event.key == pygame.K_8:
                current_color = colorBLACK

    pygame.display.flip()
    clock.tick(60)

 # 'b', 'r', 'c', 's', 't', 'q', 'h'