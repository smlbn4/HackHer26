## IMPORTS ##
from sprite import sprite
from bug import bug
from staticMethods import resource_path
#############


class plant(sprite):
    ## All plants should be 127 x 197 px ##
        
    # Possible x locations
    PLOT_X_LOCS = [58, 154, 260, 366, 472, 578]

    PLANT_DIMS = (127, 197)

    PLANT_Y = 350   # Y for all plants
    plant_types = []


    ## CONSTRUCTOR ##
    def __init__(self, type:str, purchase_price:float = 0.0, sale_price:float = 0.0, index = len(plant_types) - 1):

        self.stage = 1                          # Initial stage
        self.type = type   
        super().__init__(self.get_path())       # Sprite superclass

        self.can_spawn_bugs = False             # Can't spawn bugs until stage 5
        
        self.thisBug = None

        if type == "lettuce":
            self.thisBug = bug("grasshopper", resource_path("./bugs/grasshopperbug.PNG"), 0.5, "Did you know grasshoppers breathe through their abdomen?", self.type)
        elif type == "tomato":
            self.thisBug = bug("mantis", resource_path("./bugs/mantisbug.PNG"), 0.4, "Did you know mantises have 5 eyes?", self.type)
        elif type == "milkweed":
            self.thisBug = bug("monarch", resource_path("./bugs/monarchbug.PNG"), 0.3, "Did you know monarchs are poisonous?", self.type)
        elif type == "beebalm":
            self.thisBug = bug("bumblebee", resource_path("./bugs/bumblebeebug.PNG"), 0.2, "Did you know bumblebees dance to tell directions?", self.type)
        else:
            self.thisBug = bug("ladybug", resource_path("./bugs/ladybugbug.PNG"), 0.1, "Did you know ladybugs can eat up to 5000 and in their life?", self.type)

        self.purchase_price = purchase_price    # Purchase price from buy tab
        self.sale_price = sale_price            # Sell price at stage 5
        plant.plant_types.append(str(self))     # Add plant to list of all plants

        # Location based on past planted 
        self.loc = (plant.PLOT_X_LOCS[index], plant.PLANT_Y)

    def water_plant(self):
        if self.stage < 5:
            self.stage += 1
        else:
            return

        if self.stage == 5:
            self.can_spawn_bugs = True

        super().__init__(self.get_path(), self.loc)

    def get_path(self):
        return resource_path(f"{self.type}/{self.type}stage{self.stage}.PNG")

    def can_sell_plant(self):
        if self.stage == 5:
            return True
        else:
            return False

    def get_purchase_price(self):
        return self.purchase_price

    def get_sale_price(self):
        return self.sale_price
    
    def reset_stage(self):
        self.stage = 1
   
    def __str__(self):
        return self.type



