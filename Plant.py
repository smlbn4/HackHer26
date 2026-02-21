##
from sprite import sprite
from bug import bug
##

class plant(sprite):

    ## All plants should be 127 x 197 px ##

    # How many plants are present (static)
    numPlants = -1      # (Starts at -1 so positions work correctly)
        
    # Possible x locations
    plotXLocs = [58, 154, 260, 366, 472, 578]

    PLANT_Y = 350   # Y for all plants

    ## CONSTRUCTOR ##
    def __init__(self, type:str, img_folder:str, bugs:list[bug] = [], price:float = 0.0):

        plant.numPlants += 1

        # Individual stage images
        self.stage1image = f"{img_folder}/{type}stage1.PNG"
        self.stage2image = f"{img_folder}/{type}stage2.PNG"
        self.stage3image = f"{img_folder}/{type}stage3.PNG"
        self.stage4image = f"{img_folder}/{type}stage4.PNG"
        self.stage5image = f"{img_folder}/{type}stage5.PNG"

        super().__init__(self.stage1image)

        self.loc = (plant.plotXLocs[plant.numPlants], plant.PLANT_Y)

        self.stage = 1                          # Current stage
        self.type = type                        # String defining plant type

        self.img_folder = img_folder            # Folder name contianing stage images

        self.bugs = bugs                        # Possible bugs attracted
        self.price = price                      # Sell cost




    def water_plant(self):
        if self.stage < 5:
            self.stage += 1
        
    def get_img(self):
        return self.img_folder + "/stage" + str(self.stage) + ".png"

    def can_sell_plant(self):
        if self.stage == 5:
            return True
        else:
            return False
        
    def get_price(self):
        return self.price
    
    def sell_plant(self):
        plant.numPlants -= 1
        return self.price


    
