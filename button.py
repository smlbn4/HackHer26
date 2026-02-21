###
import pygame
from sprite import sprite
###

class button(sprite):
    
    ## CONSTRUCTOR ##
    def __init__(self, imagefname:str, loc:tuple[int, int]=(0,0), action:str = "none"):
        super().__init__(imagefname, loc)

    def pressed(self, mousePos):
        if self.get_rect().collidepoint(mousePos):
            return True
        return False