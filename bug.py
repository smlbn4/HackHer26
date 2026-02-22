from sprite import sprite

class bug(sprite):
    bug_types = []

    def __init__(self, type:str, probability,spritesfolder):
        self.found = False
        self.type = type
        self.probability = probability
        self.spritesfolder = spritesfolder

        bug.buglist.append(str(self))

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