###
import pygame
from sprite import sprite
###

class button(sprite):
    
    ## CONSTRUCTOR ##
    def __init__(self, imagefname:str, loc:tuple[int, int]=(0,0), action:str = "none"):
        super().__init__(imagefname, loc)
        self.action = action
        self.pressRect = pygame.rect.Rect(0, 0, 0, 0)


    def getAction(self):
        return self.action

    def pressed(self, mousePos):
        if self.pressRect.collidepoint(mousePos):
            return True
        return False
    
    ## TO IMPLEMENT ##
    def buttonPressed(self, action):
        if action == "none":
            return True
        if action == "quit":
            return False
        if action == "focus":
            return # STOPWATCH IMPLEMENTATION

    def makeRect(self):
        self.pressRect = pygame.rect.Rect((self.get_location()[0], self.get_location()[1]), (self.get_width(), self.get_height()))

    def getRect(self):
        return self.pressRect
