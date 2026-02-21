from sprite import sprite

class bug(sprite):

    def __init__(self,probability,spritesfolder):
        self.found = False
        self.probability = probability
        self.spritesfolder = spritesfolder
   #def get_probability(self):