## IMPORTS ##
import pygame
from keyboardControls import keyboardControls
from sprite import sprite
from button import button
from plant import plant
from bug import bug
from plotMenu import plotMenu
from stopwatch import stopwatch
#############


def main():
    canvas      = pygame.display.set_mode((640, 640))
    keepRunning = True
    kbReader    = keyboardControls("ESCAPE")
    sw          = stopwatch()

    BGCOLOR = (255, 247, 224)


    ## SPRITES ##
    allSprites  = []

    buttons = []

    # Start button
    focusButton = button("./Placeholder Sprites/PLCstartbutton.PNG", action = "focus")
    focusButton.loc = ((canvas.get_width() / 2) - (focusButton.get_width() / 2), 15)
    focusButton.makeRect()
    allSprites.append(focusButton)
    buttons.append(focusButton)

    # Quit button
    quitButton = button("./Placeholder Sprites/PLCquitbutton.PNG", action = "quit")
    quitButton.loc = (canvas.get_width() - quitButton.get_width() - 15, 15)
    quitButton.makeRect()
    allSprites.append(quitButton)
    buttons.append(quitButton)

    # Dirt
    dirt = sprite("./Placeholder Sprites/PLCplots.PNG")
    dirt.loc = (0, canvas.get_height() - dirt.get_height() - 30)
    allSprites.append(dirt)

    # Plant
    testPlant = plant("milkweed")
    allSprites.append(testPlant)

    # Plot menu
    pMenu = plotMenu()
    buttons.extend([pMenu.plotBuy, pMenu.plotWater, pMenu.plotWatch, pMenu.plotSell])
    allSprites.extend([pMenu, pMenu.plotBuy, pMenu.plotWater, pMenu.plotWatch, pMenu.plotSell])

    
    # Bugs
    bumblebee = bug("bumblebee", 0.5, "The bumblebee is a bug.", "beebalm")
    grasshopper = bug("grasshopper", 0.2, "The grasshopper is a bug.", "lettuce")
    ladybug = bug("ladybug", 0.4, "The ladybug is a bug.", "geranium")
    monarch = bug("monarch", 0.3, "The monarch is a bug.", "milkweed")
    mantis = bug("mantis", 0.1, "The mantis is a bug.", "tomato")

    # Focus screen
    focusScreen = sprite("./sprites/focusbg.PNG")
    focusScreen.visible = False
    unfocusButton = button("./sprites/unforcusbutton.PNG", (), "unfocus")
    unfocusButton.visible = False
    buttons.append(unfocusButton)
    allSprites.extend([focusScreen, unfocusButton])
    
    #############

    while keepRunning:
        canvas.fill(BGCOLOR)

        # Draw all sprites
        for s in allSprites:
            if s.visible:
                canvas.blit(s.get_image(), s.get_location())
        
        # Draw final product
        pygame.display.flip()

        mousePos = pygame.mouse.get_pos()

        # Process input
        keepRunning = kbReader.processOneEvent(mousePos, buttons, pMenu, focusScreen, unfocusButton)




if __name__ == "__main__":
    main()
