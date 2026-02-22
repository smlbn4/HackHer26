###
import pygame
from sprite import sprite
from keyboardControls import keyboardControls
from plotUI import plotUI
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
    def buttonPressed(self, action = "none", focusScreen = None, unfocusButton = None, plots = None):
        if action == "none":
            print("none")
            return True
        if action == "quit":
            return False
        if action == "focus":
            focusScreen.visible = True
            unfocusButton.visible = True
            return "focusstart"
        if action == "unfocus":
            return "focusstop"
        if action == "buy":
            chosenIndex = plotUI.selectPlot()
            
            seed = None

            event = pygame.event.wait()

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_L:
                    return
            
            plots[chosenIndex].buy_plant

        if action == "water":
            chosenIndex = plotUI.selectPlot()


        if action == "watch":
            chosenIndex = plotUI.selectPlot()


        if action == "sell":
            chosenIndex = plotUI.selectPlot()



    def makeRect(self):
        self.pressRect = pygame.rect.Rect(int(self.get_location()[0]), int(self.get_location()[1]), int(self.get_width()), int(self.get_height()))

    def getRect(self):
        return self.pressRect
    
    def move(self, newLoc):
        self.loc = newLoc
        temp = pygame.Rect(self.pressRect)
        self.pressRect = (self.loc[0], self.loc[1], temp.width, temp.height)
