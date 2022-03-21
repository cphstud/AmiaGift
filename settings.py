import pygame
pygame.font.init()
width, height = 600, 800
Window = pygame.display.set_mode((width, height))
delta = width/20
pygame.display.set_caption("Julegavespillet")
WHITE = (255, 255, 255)
main_font = pygame.font.SysFont('arial', 25)
clock = pygame.time.Clock()
#Variabler
FPS = 60
level = 0
points = 0
player_vel = 40
spawn = 10
gift_vel = 3


alien_counter=1
frame_counter=0
frequency=20
score=0