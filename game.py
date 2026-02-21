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
    kbReader    = keyboardControls.keyboardControls("escape")

    BGCOLOR = (255, 247, 224)


    ## SPRITES ##
    allSprites  = []

    # BUTTONS #
    buttons = []

    # Start button
    startButton = button.button("./Placeholder Sprites/PLCstartbutton.PNG")
    startButton.loc = ((canvas.get_width() / 2) - (startButton.get_width() / 2), 10)
    allSprites.append(startButton)
    buttons.append(startButton)

    # Quit button
    quitButton = button.button("./Placeholder Sprites/PLCquitbutton.PNG")
    quitButton.loc = ((canvas.get_width() - quitButton.get_width() - 10, 10))
    allSprites.append(quitButton)
    buttons.append(quitButton)

    # Dirt
    dirt = sprite.sprite("./Placeholder Sprites/PLCplots.PNG")
    dirt.loc = (0, canvas.get_height() - dirt.get_height() - 30)
    allSprites.append(dirt)

    # Plant
    plants = []         # To hold present plants

    testPlant1 = plant.plant("PLC", "./Placeholder Sprites/testPlant")
    testPlant2 = plant.plant("PLC", "./Placeholder Sprites/testPlant")
    testPlant3 = plant.plant("PLC", "./Placeholder Sprites/testPlant")
    testPlant4 = plant.plant("PLC", "./Placeholder Sprites/testPlant")
    testPlant5 = plant.plant("PLC", "./Placeholder Sprites/testPlant")

    plants.extend([testPlant1, testPlant2, testPlant3, testPlant4, testPlant5])
    allSprites.extend([testPlant1, testPlant2, testPlant3, testPlant4, testPlant5])


    
    
    #############

    while keepRunning:

        # Background color
        canvas.fill(BGCOLOR)

        # Draw all sprites
        for s in allSprites:

            print(s)
            canvas.blit(s.get_image(), s.get_location())
        
        # Draw final product
        pygame.display.flip()

        mousePos = pygame.mouse.get_pos()
        for b in buttons:
            b.pressed(mousePos)

        keepRunning = kbReader.processOneEvent()

if __name__ == "__main__":
    main()
