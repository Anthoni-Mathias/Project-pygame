import pygame
from pygame.locals import *
from sys import exit

pygame.init()

"""
Screen size for the game
"""
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('title')

"""
Loop efect and odjects
"""
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
  pygame.draw.rect(screen, (255,0,0), (200,300,40,50))
  pygame.display.update()