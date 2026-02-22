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

    buttons = []

    # Start button
    startButton = button.button("./Placeholder Sprites/PLCstartbutton.PNG")
    startButton.loc = ((canvas.get_width() / 2) - (startButton.get_width() / 2), 15)
    startButton.makeRect()
    allSprites.append(startButton)
    buttons.append(startButton)

    # Quit button
    quitButton = button.button("./Placeholder Sprites/PLCquitbutton.PNG", action = "quit")
    quitButton.loc = (canvas.get_width() - quitButton.get_width() - 15, 15)
    quitButton.makeRect()
    allSprites.append(quitButton)
    buttons.append(quitButton)

    # Dirt
    dirt = sprite.sprite("./Placeholder Sprites/PLCplots.PNG")
    dirt.loc = (0, canvas.get_height() - dirt.get_height() - 30)
    allSprites.append(dirt)

    # Plant
    testPlant = plant.plant("milkweed")
    allSprites.append(testPlant)
    
    
    #############

    while keepRunning:
        canvas.fill(BGCOLOR)

        # Draw all sprites
        for s in allSprites:
            canvas.blit(s.get_image(), s.get_location())
        
        # Draw final product
        pygame.display.flip()

        mousePos = pygame.mouse.get_pos()

        # Process input
        keepRunning = kbReader.processOneEvent(mousePos, buttons)



if __name__ == "__main__":
    main()
