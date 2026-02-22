###
import pygame
from sprite import sprite
from keyboardControls import keyboardControls
from plotUI import plotUI
from plant import plant
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
    def buttonPressed(self, action = "none", focusScreen = None, unfocusButton = None, plots = None, coinBalance = None, plotRects = None):
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
        
        # Buy in target plot
        if action == "buy":
            "activated click yay"
            chosenIndex = plotUI.selectPlot(plotRects)
            
            seed = None

            event = pygame.event.wait()

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    seed = plant("lettuce", 2, 5)
                elif event.key == pygame.K_t:
                    seed = plant("tomato", 4, 10)
                elif event.key == pygame.K_m:
                    seed = plant("milkweed", 6, 15)
                elif event.key == pygame.K_b:
                    seed = plant("beebalm", 8, 20)
                elif event.key == pygame.K_g:
                    seed = plant("geranium", 10, 25)
            
            plots[chosenIndex].buy_plant(coinBalance, seed)

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
