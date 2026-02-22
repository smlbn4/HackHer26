from sprite import sprite

class bug(sprite):
    bug_types = []

    def __init__(self, type:str, probability, description):
        self.found = False
        self.type = type
        self.probability = probability
        self.description = description
        super().__init__(self.get_path())

        bug.bug_types.append(self)

    def is_found(self):
        self.found = True

    def forget(self): #undiscovers bug
        self.found = False
        bug.bug_types.remove(str(self))
        #need to change sprite

    def get_path(self):
        return f"bugs/{self.type}bug.PNG"

    def get_prob(self):
        return self.probability
    
    def __str__(self):
        return self.type
    #def get_sprite(self):
        #return f"{self.spritesfolder}/{self.type}stage{self.stage}.PNG" #needs to be edited

