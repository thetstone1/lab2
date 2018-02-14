import pygame
class Target:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.rect = pygame.Rect((self.x,self.y,40,10))
  def hit(self,rock,surf):
    return self.rect.colliderect(rock.getrect())
  def moveTo(self,x,y):
    self.x = x
    self.y = y
    self.rect = pygame.Rect((self.x,self.y,40,10))
  def draw(self, surf):
    pygame.draw.rect(surf,(0,0,0),self.rect)


