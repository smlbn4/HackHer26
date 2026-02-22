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

import pygame_widgets
from pygame_widgets.textbox import TextBox
#############


def main():
    pygame.init()

    canvas      = pygame.display.set_mode((640, 640))
    keepRunning = True
    kbReader    = keyboardControls("ESCAPE")
    sw          = stopwatch()
    timeBalance = timeCurrency(999)
    coinBalance = currency(10)

    plots       = []
    for i in range(5):
        newPlot = plot()
        plots.append(newPlot)


    plotRects   = []
    for i in range(5):
        e = pygame.rect.Rect(plant.PLOT_X_LOCS[i], plant.PLANT_Y, plant.PLANT_DIMS[0], plant.PLANT_DIMS[1])
        print(plant.PLOT_X_LOCS[i], plant.PLANT_Y, plant.PLANT_DIMS[0], plant.PLANT_DIMS[1])
        plotRects.append(e)

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

    # Piggybank
    piggyBank = sprite("./sprites/piggybank.PNG")
    piggyBank.loc = (5, 5)
    allSprites.append(piggyBank)

    piggyLabel = pygame.font.SysFont("Textile", 52)
    piggyLabelSurface = piggyLabel.render(str(coinBalance), True, (0, 0, 0))
    piggyLabelRect = piggyLabelSurface.get_rect()
    piggyLabelRect.center = (125, 75)

    # Dirt
    dirt = sprite("./Placeholder Sprites/PLCplots.PNG")
    dirt.loc = (0, canvas.get_height() - dirt.get_height() - 20)
    allSprites.append(dirt)

    # Plants
    for e in plots:
        if e.plot_plant != None:
            allSprites.append(e.plot_plant)
            print("added plant")

    # Purchase menu
    shop = sprite("./sprites/shop.PNG")
    shop.loc = (0, canvas.get_height() - shop.height)
    shop.visible = False
    allSprites.append(shop)

    # Plot menu
    pMenu = plotMenu()
    buttons.extend([pMenu.plotBuy, pMenu.plotWater, pMenu.plotWatch, pMenu.plotSell])
    allSprites.extend([pMenu, pMenu.plotBuy, pMenu.plotWater, pMenu.plotWatch, pMenu.plotSell])


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

        for e in plots:
            if e.plot_plant != None and not sw.running:
                allSprites.append(e.plot_plant)

        # Draw all sprites
        for s in allSprites:
            if s.visible:
                canvas.blit(s.get_image(), s.get_location())

        if not sw.running:
            text_surface = font.render(str(coinBalance), True, (0, 0, 0))
            canvas.blit(text_surface, text_rect)
        
        # Draw final product
        pygame.display.flip()

        mousePos = pygame.mouse.get_pos()

        # Process input
        result = kbReader.processOneEvent(canvas, mousePos, buttons, pMenu, focusScreen, unfocusButton, plots=plots, coinBalance = coinBalance, plotRects=plotRects, timeBalance = timeBalance, shop = shop)

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
