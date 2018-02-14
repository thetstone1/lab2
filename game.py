#!/usr/bin/python
 
import launcher
import serial
import rock
import target
import random
import time
import pygame, sys
from pygame.locals import *

FPS = 30

def main():
  pygame.init()
  fpsClock = pygame.time.Clock()
  my_serial = serial.Serial("/dev/ttyACM0")
  my_launcher = launcher.Launcher(0,400)
  my_rock = rock.Rock(0,400)
  my_target = target.Target(random.random()*280+100,390)
  window = pygame.display.set_mode((500,400))
  pygame.display.set_caption('Lab 2 Stone')
  while(True):
    draw_world(window)
    mag_alt = read_arduino(my_serial)
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
        elif event.key == pygame.K_SPACE and not my_rock.isMoving() and not my_target.hit(my_rock,window):
          my_launcher.fire(my_rock)
        elif event.key == pygame.K_r:
          my_serial.write('r')
        elif event.key == pygame.K_g:
          my_serial.write('g')
      if event.type == QUIT:
        pygame.quit()
        sys.exit()

    my_rock.move(1.0/FPS)
    my_launcher.Alt_Mag(mag_alt)
    if(my_rock.y > 400):
      my_rock.moveto(0,400,window)
      displaytxt("You Missed!!",window)
    if my_target.hit == True:
      my_rock.moveto(0,400,window)
      displaytxt("Good Hit!!",window)
      my_target.moveTo(random.random()*280+100,390)

    my_launcher.draw(window)
    my_rock.draw(window)
    my_target.draw(window)
    pygame.display.update()
    fpsClock.tick(FPS)

def draw_world(surf):
  surf.fill((0,128,128))
  font = pygame.font.Font(None, 60)
  pygame.draw.rect(surf,(0,128,0),(0,370,500,30))
  txt = """Launcher"""
  txtimg = font.render(txt,True,(255,255,255))
  surf.blit(txtimg,(150,50),None,0) 
def displaytxt(str,surf):
  font = pygame.font.Font(None, 60)
  txtimg = font.render(str,True,(255,255,255))
  surf.blit(txtimg,(150,150),None,0)
  pygame.display.update()
  time.sleep(3) 

def read_arduino(myserial):
  myserial.write('p')
  vals = myserial.readline()
  mag_alt = [int(x) for x in vals.split(',')]
  return mag_alt
main()
    
