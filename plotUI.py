import pygame

class plotUI():
    @staticmethod
    def selectPlot(plotRects):
        while True:
            mousePos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        i = 0
                        for p in plotRects:
                            if p.colliderect(mousePos):
                                return i
                            else:
                                i += 1
