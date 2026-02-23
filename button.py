## IMPORTS ##
import pygame
import random
from sprite import sprite
from plot import plot
from staticMethods import selectPlot, resource_path
from plant import plant
from bug import bug
from quitGame import quitGame
#############

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
    
    def buttonPressed(self, action = "none", canvas = None, mousePos = None, focusScreen = None, unfocusButton = None, plots = None, coinBalance = None, plotRects = None, timeBalance = None, shop = None, allSprites = None, buttons = None):
        if action == "none":
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
            select = sprite(resource_path("./sprites/plotselecticon.PNG"))
            canvas.blit(select.get_image(), select.get_location())
            pygame.display.flip()

            chosenIndex = selectPlot(plotRects, buttons)

            select.visible = False

            seed = None

            if plots[chosenIndex].is_empty:
                shop.visible = True
                canvas.blit(shop.get_image(), shop.get_location())
                pygame.display.flip()

                while seed == None:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            raise quitGame
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                for b in buttons:
                                    if pygame.Rect(b.getRect()).collidepoint(mousePos) and b.visible and b.getAction() == "quit":
                                        raise quitGame
                                    
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
            else:
                pass
        
            shop.visible = False
            
            plots[chosenIndex].buy_plant(coinBalance, seed)

            del select.surface
            del select

        if action == "water":
            select = sprite(resource_path("./sprites/plotselecticon.PNG"))
            canvas.blit(select.get_image(), select.get_location())
            pygame.display.flip()

            chosenIndex = selectPlot(plotRects, buttons)

            plots[chosenIndex].water(timeBalance)

            select.visible = False
            del select.surface
            del select


        if action == "watch":
            select = sprite(resource_path("./sprites/plotselecticon.PNG"))
            canvas.blit(select.get_image(), select.get_location())
            pygame.display.flip()

            chosenIndex = selectPlot(plotRects, buttons)
            
            bug_found = plots[chosenIndex].watch_plant(timeBalance)
            if isinstance(bug_found, bug):
                bug_found.loc = (random.randint(20, 620), random.randint(200, 500))
                allSprites.append(bug_found)
                pygame.display.flip()

            select.visible = False
            del select.surface
            del select


        if action == "sell":
            select = sprite(resource_path("./sprites/plotselecticon.PNG"))
            canvas.blit(select.get_image(), select.get_location())
            pygame.display.flip()
        
            chosenIndex = selectPlot(plotRects, buttons)

            plots[chosenIndex].sell_plant(coinBalance)
            plots[chosenIndex] = plot()

            select.visible = False
            del select.surface
            del select



    def makeRect(self):
        self.pressRect = pygame.rect.Rect(int(self.get_location()[0]), int(self.get_location()[1]), int(self.get_width()), int(self.get_height()))

    def getRect(self):
        return self.pressRect