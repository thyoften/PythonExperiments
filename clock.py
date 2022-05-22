import pygame
import math
import datetime

geometry = [640, 480]
center = (geometry[0] / 2, geometry[1] / 2)


# Colours
BACKGROUND = (127, 164, 227)
HOUR_HAND_COL = (0, 0, 255)
MINUTE_HAND_COL = HOUR_HAND_COL
SECOND_HAND_COL = (255, 0, 0)
CLOCK_FRAME_COL = (0, 0, 0)
CLOCK_INNER_COL = (255, 255, 255)


# Hand length
CLOCK_RADIUS = 200
FRAME_WIDTH = 4
H = 98
M = H * 1.85
S = M

pygame.init()

screen = pygame.display.set_mode(geometry)
pygame.display.set_caption('Pygame Clock - Press ESC to close')

clk = pygame.time.Clock()

terminate = False


def draw_clock_base():
    # Clock frame & inner
    pygame.draw.circle(screen, CLOCK_INNER_COL, center, CLOCK_RADIUS)
    pygame.draw.circle(screen, CLOCK_FRAME_COL, center, CLOCK_RADIUS, width=FRAME_WIDTH)

    # Draw hour ticks
    for i in range(1, 13):
        pos_tick_end = (center[0] + M * math.cos(i * math.pi / 6), center[1] - M * math.sin(i * math.pi / 6))
        pos_tick_start = (center[0] + (M - 20) * math.cos(i * math.pi / 6),
                          center[1] - (M - 20) * math.sin(i * math.pi / 6))
        pygame.draw.line(screen, CLOCK_FRAME_COL, pos_tick_start, pos_tick_end)

    # Draw seconds ticks
    for i in range(1, 61):
        pos_tick_end = (center[0] + M * math.cos(i * math.radians(6)), center[1] - M * math.sin(i * math.radians(6)))
        pos_tick_start = (center[0] + (M - 8) * math.cos(i * math.radians(6)),
                          center[1] - (M - 8) * math.sin(i * math.radians(6)))
        pygame.draw.line(screen, CLOCK_FRAME_COL, pos_tick_start, pos_tick_end)


while not terminate:

    screen.fill(BACKGROUND)

    draw_clock_base()

    cur_time = datetime.datetime.now()
    hour = cur_time.hour
    minutes = cur_time.minute
    seconds = cur_time.second

    """
    0:00 => Hand is @ 90° position
    1:00 => Hand is @ 90°-30° position
    2:00 => Hand is @ 90°-60° position
    So for any hour H => Hand is @ 90°-H°30°
    
    H should be H%12 to account for 24hrs
    
    Same for minutes, but instead of 30° we subtract 6°
    
    For any hand we draw a line from the center to the computed position
    
    """
    # Compensate to make it more similar to analog clocks irl
    hour = hour + minutes / 60 + seconds / 3600
    minutes = minutes + seconds / 60
    
    angle_hour = (hour % 12) * (math.pi / 6)
    angle_minutes = minutes * math.radians(6) 
    angle_seconds = seconds * math.radians(6)

    posH = (center[0] + H * math.sin(angle_hour), center[1] - H * math.cos(angle_hour)) # Trig power!
    posM = (center[0] + M * math.sin(angle_minutes), center[1] - M * math.cos(angle_minutes))
    posS = (center[0] + S * math.sin(angle_seconds), center[1] - S * math.cos(angle_seconds))

    pygame.draw.line(screen, HOUR_HAND_COL, center, posH, 5)
    pygame.draw.line(screen, MINUTE_HAND_COL, center, posM, 3)
    pygame.draw.line(screen, SECOND_HAND_COL, center, posS, 2)

    pygame.draw.circle(screen, HOUR_HAND_COL, center, 13)
    pygame.draw.circle(screen, SECOND_HAND_COL, center, 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            terminate = True

    pygame.display.update()
    clk.tick(60)
