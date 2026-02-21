## IMPORTS ##
import pygame
import pickle
import keyboardControls
import sprite
import button
import plant
#############

def main():
    canvas      = pygame.display.set_mode((640, 640))
    keepRunning = True
    kbReader    = keyboardControls.keyboardControls("ESCAPE")

    BGCOLOR = (255, 247, 224)


    ## SPRITES ##
    allSprites  = []

    # Start button
    startButton = button.button("./Placeholder Sprites/PLCstartbutton.PNG")
    startButton.loc = ((canvas.get_width() / 2) - (startButton.get_width() / 2), 10)
    allSprites.append(startButton)

    # Quit button
    quitButton = button.button("./Placeholder Sprites/PLCquitbutton.PNG")
    quitButton.loc = ((canvas.get_width() - quitButton.get_width() - 10, 10))
    allSprites.append(quitButton)

    # Dirt
    dirt = sprite.sprite("./Placeholder Sprites/PLCplots.PNG")
    dirt.loc = (0, canvas.get_height() - dirt.get_height() - 30)
    allSprites.append(dirt)

    # Plant
    testPlant = plant.plant("PLC", "./Placeholder Sprites/testPlant")
    testPlant.water_plant()
    testPlant.loc = (100, 100)
    allSprites.append(testPlant)

    plantYLoc =  canvas.get_height() - (dirt.get_height() / 2) - 30 + testPlant.get_height()
    plotXLocs = [106, 212, 318, 424, 530, 636]
    currPlantNum = 0


    
    
    #############

    while keepRunning:
        canvas.fill(BGCOLOR)
        keepRunning = kbReader.processOneEvent()

        # Draw all sprites
        for s in allSprites:
            canvas.blit(s.get_image(), s.get_location())
        
        # Draw final product
        pygame.display.flip()

if __name__ == "__main__":
    main()
