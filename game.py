## IMPORTS ##
import pygame
import pickle
import keyboardControls
import sprite
#############

def main():
    canvas      = pygame.display.set_mode((640, 640))
    keepRunning = True
    kbReader    = keyboardControls.KeyboardControls("ESCAPE")

    BGCOLOR = (255, 247, 224)


    ## SPRITES ##
    allSprites  = []

    startButton = sprite.sprite("./Placeholder Sprites/PLCstartbutton.PNG")
    startButton.loc = ((canvas.get_width() / 2) - (startButton.get_width() / 2),10)
    allSprites.append(startButton)
    
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
