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


    def get_action(self):
        return self.action

    def pressed(self, mousePos):
        if self.pressRect.collidepoint(mousePos):
            return True
        return False
    
    ## TO IMPLEMENT ##
    def buttonPressed(action):
        if action == "none":
            return
        if action == "quit":
            pygame.quit()

    def makeRect(self):
        self.pressRect = pygame.rect.Rect((self.get_location()[0], self.get_location()[1]), (self.get_width(), self.get_height()))
        