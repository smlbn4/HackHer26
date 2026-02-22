###
import pygame
from sprite import sprite
from keyboardControls import keyboardControls
from plot import plot
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
    def buttonPressed(self, action = "none", canvas = None, focusScreen = None, unfocusButton = None, plots = None, coinBalance = None, plotRects = None, timeBalance = None, shop = None):
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
            chosenIndex = plotUI.selectPlot(plotRects)
            
            seed = None

            shop.visible = True
            canvas.blit(shop.get_image(), shop.get_location())
            pygame.display.flip()

            while seed == None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_l:
                            seed = plant("lettuce", 2, 5, chosenIndex)
                            continue
                        elif event.key == pygame.K_t:
                            seed = plant("tomato", 4, 10, chosenIndex)
                            continue
                        elif event.key == pygame.K_m:
                            seed = plant("milkweed", 6, 15, chosenIndex)
                            continue
                        elif event.key == pygame.K_b:
                            seed = plant("beebalm", 8, 20, chosenIndex)
                            continue
                        elif event.key == pygame.K_g:
                            seed = plant("geranium", 10, 25, chosenIndex)
                            continue

            print("made it past loop")
        
            shop.visible = False
            canvas.blit(shop.get_image(), shop.get_location())
            pygame.display.flip()
            
            plots[chosenIndex].buy_plant(coinBalance, seed)

        if action == "water":
            chosenIndex = plotUI.selectPlot(plotRects)

            plots[chosenIndex].water(timeBalance)


        if action == "watch":
            chosenIndex = plotUI.selectPlot(plotRects)


        if action == "sell":
            chosenIndex = plotUI.selectPlot(plotRects)

            plots[chosenIndex].sell_plant(coinBalance)
            plots[chosenIndex] = plot()

            pygame.display.flip()



    def makeRect(self):
        self.pressRect = pygame.rect.Rect(int(self.get_location()[0]), int(self.get_location()[1]), int(self.get_width()), int(self.get_height()))

    def getRect(self):
        return self.pressRect