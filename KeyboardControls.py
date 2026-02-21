## IMPORTS ##
import pygame
import pickle
import button
#############

class keyboardControls():
    
    def __init__(self, quitKey):
        self.quitKey = pygame.key.key_code(quitKey)
        

    def processOneEvent(self, mousePos, buttons):
        pressedKeys =  pygame.key.get_pressed()
        if pressedKeys[self.quitKey]:
            return False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("click")
                    for b in buttons:
                        if b.getRect().collidepoint(mousePos):
                            b.buttonPressed(b.getAction())
        return True