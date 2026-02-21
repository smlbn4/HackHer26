## IMPORTS ##
import pygame
import pickle
import KeyboardControls
#############

def main():
    canvas      = pygame.display.set_mode((640, 640))
    keepRunning = True
    kbReader    = KeyboardControls.KeyboardControls("ESCAPE")

    BGCOLOR = (255, 247, 224)

    while keepRunning:
        canvas.fill(BGCOLOR)
        pygame.display.flip()
        keepRunning = kbReader.processOneEvent()

if __name__ == "__main__":
    main()
