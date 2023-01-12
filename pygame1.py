import pygame
pygame.init()

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Dark Souls')

game_status = True

while game_status:
    events = pygame.event.get()
    pygame.display.update()
    pass
pygame.quit()
quit()