from sprite import sprite

class bug(sprite):

    buglist = []

    def __init__(self,probability,spritesfolder):
        self.found = False
        self.probability = probability
        self.spritesfolder = spritesfolder

        bug.buglist.append(self)

    def is_found(self):
        self.found = True

    def forget(self): #undiscovers bug
        self.found = False
        #need to change sprite

    def get_prob(self):
        return self.probability
    
    def __str__(self):
        return self.type
    #def get_sprite(self):
        #return f"{self.spritesfolder}/{self.type}stage{self.stage}.PNG" #needs to be edited