## IMPORTS ##
import pygame
import pickle
import keyboardControls
import sprite
import button
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

    # Plant
    
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
