import serial
import math
import pygame, sys
from pygame.locals import *

MAX_MAG = 100
MIN_MAG = 10
MAX_ANGLE = 90
MIN_ANGLE = 0
class Launcher:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.mag = 50
    self.ang = .78539
  def Alt_Mag(self, mag_alt):
    self.mag = mag_alt[0]-155
    self.alt = mag_alt[1]-160
    if self.mag < 0:
      self.mag = 10
    if self.alt < 0:
      self.alt = 5 

  def Alt(self, alt):
    self.alt = alt

  def changeMagnitude(self,delta):
    if self.mag < 100 and self.mag > 10:
      self.mag = self.mag + delta
    elif self.mag > 100:
      self.mag = self.mag - 6
    elif self.mag < 10:
      self.mag = self.mag + 6
  def changeAngle(self,delta):
    if self.ang < 1.57 and self.ang > 0:
      self.ang = self.ang + delta
    elif self.ang > 1.57:
      self.ang = self.ang -.13962 
    elif self.ang < 0:
      self.ang = self.ang + .13962
  def fire(self, rock):
    rock.v_x = abs(self.mag*math.cos(self.ang))
    rock.v_y = -1*abs(self.mag*math.sin(self.ang))
  def draw(self,surf):
    self.s_point = (self.x,self.y)
    e_x = abs(self.mag*math.cos(self.ang))
    e_y = 400-abs(self.mag*math.sin(self.ang))
    self.e_point = (e_x,e_y)
    pygame.draw.line(surf,(0,0,0),self.s_point,self.e_point, 2) 
    
