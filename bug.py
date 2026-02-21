from sprite import sprite

class bug(sprite):

    def __init__(self,probability,spritesfolder):
        self.found = False
        self.probability = probability
        self.spritesfolder = spritesfolder
    def get_prob(self):
        return self.probability
    def get_img(self):
        return 