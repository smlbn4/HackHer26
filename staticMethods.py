## IMPORTS ##
import pygame
import sys
import os
from quitGame import quitGame
#############


@staticmethod
def selectPlot(plotRects, buttons):

    while True:
        mousePos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for b in buttons:
                        if pygame.Rect(b.getRect()).collidepoint(mousePos) and b.visible and b.getAction() == "quit":
                            raise quitGame
                        
                    i = 0
                    for p in plotRects:
                        p = pygame.Rect(p)
                        if p.collidepoint(mousePos):
                            return i

                        else:
                            i += 1

## ADDED FOR PYINSTALLER
@staticmethod
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    # acquired from https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)