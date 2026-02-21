###
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
###

class sprite():  

    ## CONSTRUCTOR ##
    def __init__ (self, imagefname:str, loc:tuple[int, int]=(0,0)):

        # Setting up the image
        self.imageFileName =    imagefname
        self.image =            pygame.image.load(imagefname)
        self.surface =          pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        self.surface.blit(self.image, (0, 0))

        self.loc =         loc
        self.width =       pygame.Surface.get_width(self.surface)
        self.height =      pygame.Surface.get_height(self.surface)


    ## GETTERS ##
    # Surface object
    def get_image(self):

        return self.surface

    # Width
    def get_width(self):

        return self.width

    # Height
    def get_height(self):

        return self.height
    
    # Location
    def get_location(self):

        return self.loc
    