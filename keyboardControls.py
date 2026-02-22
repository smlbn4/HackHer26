
## IMPORTS ##
import pygame
from stopwatch import stopwatch
#############

class keyboardControls():
    

    ## CONSTRUCTOR ##
    def __init__(self, quitKey):
        self.quitKey = pygame.key.key_code(quitKey)
        

    def processOneEvent(self, mousePos = None, buttons = None, pMenu = None, focusScreen = None, unfocusButton = None, plots = None, coinBalance = None, plotRects = None):
        pressedKeys =  pygame.key.get_pressed()
        if pressedKeys[self.quitKey]:
            return False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for b in buttons:
                        if pygame.Rect(b.getRect()).collidepoint(mousePos) and b.visible:
                            return b.buttonPressed(b.getAction(), focusScreen, unfocusButton, plots, plotRects)
                elif event.button == 3:
                    if pMenu.visible:
                        pMenu.hide()
                    else:
                        pMenu.show(mousePos)
        return True