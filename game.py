#!/usr/bin/python
 
import launcher
import serial
import math
import pygame, sys
from pygame.locals import *

FPS = 30

def main():
  pygame.init()
  fpsClock = pygame.time.Clock()
  my_launcher = launcher.Launcher(0,400)
  window = pygame.display.set_mode((500,400))
  pygame.display.set_caption('Lab 2 Stone')
  while(True):
    draw_world(window)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          my_launcher.changeAngle(.05236)
        elif event.key == pygame.K_DOWN:
          my_launcher.changeAngle(-.05236)
        elif event.key == pygame.K_LEFT:
          my_launcher.changeMagnitude(-3)
        elif event.key == pygame.K_RIGHT:
          my_launcher.changeMagnitude(3)
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    my_launcher.draw(window)
    pygame.display.update()
    fpsClock.tick(FPS)

def draw_world(surf):
  surf.fill((0,128,128))
  font = pygame.font.Font(None, 60)
  pygame.draw.rect(surf,(0,128,0),(0,350,500,50))
  txt = """Launcher"""
  txtimg = font.render(txt,True,(255,255,255))
  surf.blit(txtimg,(150,50),None,0) 

main()
    
