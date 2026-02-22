###
import pygame
from sprite import sprite
from keyboardControls import keyboardControls
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
    def buttonPressed(self, action = "none", focusScreen = None, unfocusButton = None):
        if action == "none":
            print("none")
            return True
        if action == "quit":
            return False
        if action == "focus":
            focusScreen.visible = True
            unfocusButton.visible = True
            keyboardControls.waitForUnfocus(focusScreen, unfocusButton)
            
        if action == "unfocus":
            return
        if action == "buy":
            print("buy")
        if action == "water":
            print("water")
        if action == "watch":
            print("watch")
        if action == "sell":
            print("sell")

    def makeRect(self):
        self.pressRect = pygame.rect.Rect(int(self.get_location()[0]), int(self.get_location()[1]), int(self.get_width()), int(self.get_height()))

    def getRect(self):
        return self.pressRect
    
    def move(self, newLoc):
        self.loc = newLoc
        temp = pygame.Rect(self.pressRect)
        self.pressRect = (self.loc[0], self.loc[1], temp.width, temp.height)
