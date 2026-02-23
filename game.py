## IMPORTS ##
import pygame
from keyboardControls import keyboardControls
from sprite import sprite
from button import button
from plant import plant
from plot import plot
from plotMenu import plotMenu
from stopwatch import stopwatch
from timeCurrency import timeCurrency
from currency import currency
from staticMethods import resource_path
from quitGame import quitGame
import sys
#############


def main():
    pygame.init()

    canvas      = pygame.display.set_mode((640, 640))
    keepRunning = True
    kbReader    = keyboardControls("ESCAPE")
    sw          = stopwatch()
    timeBalance = timeCurrency(500)
    coinBalance = currency(500)

    plots       = []
    for i in range(5):
        newPlot = plot()
        plots.append(newPlot)


    plotRects   = []
    for i in range(5):
        e = pygame.rect.Rect(plant.PLOT_X_LOCS[i], plant.PLANT_Y, plant.PLANT_DIMS[0], plant.PLANT_DIMS[1])
        plotRects.append(e)

    BGCOLOR = (155, 172, 140)


    ## SPRITES ##
    allSprites  = []

    buttons = []

    # Mist
    mist = sprite(resource_path("./sprites/mist.PNG"))
    allSprites.append(mist)
    
    # Hours label
    hoursSprite = sprite(resource_path("./sprites/hourslabel.PNG"))
    hoursSprite.loc = ((canvas.get_width() / 2) - (hoursSprite.get_width() / 2) + 40, 10)
    allSprites.append(hoursSprite)

    hoursLabel = pygame.font.SysFont("Textile", 40)
    hoursLabelSurface = hoursLabel.render(str(timeBalance.get_value()), True, (0, 0, 0))
    hoursLabelRect = hoursLabelSurface.get_rect()
    hoursLabelRect.center = (hoursSprite.loc[0] + 200, 135)

    # Start button
    focusButton = button(resource_path("./sprites/focusbutton.PNG"), action = "focus")
    focusButton.loc = ((canvas.get_width() / 2) - (focusButton.get_width() / 2) + 40, 10)
    focusButton.makeRect()
    allSprites.append(focusButton)
    buttons.append(focusButton)

    # Quit button
    quitButton = button(resource_path("./sprites/quitbutton.PNG"), action = "quit")
    quitButton.loc = (canvas.get_width() - quitButton.get_width(), 15)
    quitButton.makeRect()
    allSprites.append(quitButton)
    buttons.append(quitButton)

    # Piggybank
    piggyBank = sprite(resource_path("./sprites/piggybank.PNG"))
    piggyBank.loc = (5, 5)
    allSprites.append(piggyBank)

    piggyLabel = pygame.font.SysFont("Textile", 52)
    piggyLabelSurface = piggyLabel.render(str(coinBalance), True, (0, 0, 0))
    piggyLabelRect = piggyLabelSurface.get_rect()
    piggyLabelRect.center = (125, 75)

    # Dirt
    dirt = sprite(resource_path("./sprites/dirt.PNG"))
    dirt.loc = (0, canvas.get_height() - dirt.get_height() - 20)
    allSprites.append(dirt)

    # Plants
    for e in plots:
        if e.plot_plant != None:
            allSprites.append(e.plot_plant)

    # Grass
    grass = sprite(resource_path("./sprites/grass.PNG"))
    grass.loc = (0, -10)
    allSprites.append(grass)

    # Purchase menu
    shop = sprite(resource_path("./sprites/shop.PNG"))
    shop.loc = (0, canvas.get_height() - shop.height)
    shop.visible = False
    allSprites.append(shop)

    # Plot menu
    pMenu = plotMenu()
    buttons.extend([pMenu.plotBuy, pMenu.plotWater, pMenu.plotWatch, pMenu.plotSell])
    allSprites.extend([pMenu, pMenu.plotBuy, pMenu.plotWater, pMenu.plotWatch, pMenu.plotSell])

    # Focus screen
    focusScreen = sprite(resource_path("./sprites/focusbg.PNG"))
    focusScreen.visible = False
    unfocusButton = button(resource_path("./sprites/unfocusbutton.PNG"), (0, 0), "unfocus")
    unfocusButton.pressRect = pygame.rect.Rect((129, 316), (383, 173))
    unfocusButton.visible = False
    buttons.insert(0, unfocusButton)
    allSprites.extend([focusScreen, unfocusButton])
    
    #############

    
    try:
        while keepRunning:
            canvas.fill(BGCOLOR)

            for e in plots:
                if e.plot_plant != None and not sw.running:
                    allSprites.append(e.plot_plant)

            # Draw all sprites
            for s in allSprites:
                if s.visible:
                    canvas.blit(s.get_image(), s.get_location())

            if not sw.running:
                piggySurface = piggyLabel.render(str(coinBalance), True, (0, 0, 0))
                canvas.blit(piggySurface, piggyLabelRect)

                hoursSurface = hoursLabel.render(str(timeBalance.get_value()), True, (0, 0, 0))
                canvas.blit(hoursSurface, hoursLabelRect)
            else:
                canvas.blit(focusScreen.get_image(), focusScreen.get_location())
                canvas.blit(unfocusButton.get_image(), unfocusButton.get_location())
            
            # Draw final product
            pygame.display.flip()

            mousePos = pygame.mouse.get_pos()

            # Process input
            result = kbReader.processOneEvent(canvas, mousePos, buttons, pMenu, focusScreen, unfocusButton, plots=plots, coinBalance = coinBalance, plotRects=plotRects, timeBalance = timeBalance, shop = shop, allSprites = allSprites)

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

                timeBalance.set(round(timeBalance.get_value(), 1))

                sw.reset()

    except quitGame:
        pass


    pygame.quit()
    sys.exit()




if __name__ == "__main__":
    main()
