## IMPORTS ##
import pygame
from keyboardControls import keyboardControls
from sprite import sprite
from button import button
from plant import plant
from bug import bug
from plot import plot
from plotMenu import plotMenu
from stopwatch import stopwatch
from timeCurrency import timeCurrency
from currency import currency
#############


def main():
    canvas      = pygame.display.set_mode((640, 640))
    keepRunning = True
    kbReader    = keyboardControls("ESCAPE")
    sw          = stopwatch()
    timeBalance = timeCurrency(0)
    coinBalance = currency(10)

    plots       = [None, None, None, None, None]
    for e in plots:
        e = plot()

    i = 0
    plotRects   = [None, None, None, None, None]
    for e in plotRects:
        e = pygame.rect.Rect((plant.PLOT_X_LOCS[i], plant.PLANT_Y), (plant.PLANT_DIMS))
        i += 1

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

    # Plot menu
    pMenu = plotMenu()
    buttons.extend([pMenu.plotBuy, pMenu.plotWater, pMenu.plotWatch, pMenu.plotSell])
    allSprites.extend([pMenu, pMenu.plotB

    # Bugs
    bumblebee = bug("bumblebee", 0.2, "The bumblebee is a bug.", "beebalm")
    grasshopper = bug("grasshopper", 0.5, "The grasshopper is a bug.", "lettuce")
    ladybug = bug("ladybug", 0.1, "The ladybug is a bug.", "geranium")
    monarch = bug("monarch", 0.3, "The monarch is a bug.", "milkweed")
    mantis = bug("mantis", 0.4, "The mantis is a bug.", "tomato")

    # Plant
    beebalm = plant("beebalm", bumblebee, 8, 16)
    geranium = plant("geranium", ladybug, 10, 18)
    milkweed = plant("milkweed", monarch, 6, 14)
    lettuce = plant("lettuce", grasshopper, 2, 10)
    tomato = plant("tomato", mantis, 4, 12)

    # Focus screen
    focusScreen = sprite("./sprites/focusbg.PNG")
    focusScreen.visible = False
    unfocusButton = button("./sprites/unfocusbutton.PNG", (0, 0), "unfocus")
    unfocusButton.pressRect = pygame.rect.Rect((129, 316), (383, 173))
    unfocusButton.visible = False
    buttons.insert(0, unfocusButton)
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
        result = kbReader.processOneEvent(mousePos, buttons, pMenu, focusScreen, unfocusButton, plots, coinBalance, plotRects)

        if result == False:
            keepRunning = False
        if result == "focusstart":
            sw.start()
        elif result == "focusstop":
            sw.stop()

            # Take away the focus UI
            focusScreen.visible = False
            unfocusButton.visible = False

            # Add spent time to piggy bank
            timeBalance.add_hours(sw.elapsedTime())

            sw.reset()




if __name__ == "__main__":
    main()
