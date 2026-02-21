## IMPORTS ##
import pygame
import pickle
#############

class KeyboardControls():
    
    def __init__(self, quitKey):
        self.quitKey = pygame.key.key_code(quitKey)
        

    def processOneEvent(self):
        pressedKeys =  pygame.key.get_pressed()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return False
        return True