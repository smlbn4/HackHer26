from sprite import sprite
from timeCurrency import timeCurrency

class plant(sprite):
    ## All plants should be 127 x 197 px ##
        
    # Possible x locations
    PLOT_X_LOCS = [58, 154, 260, 366, 472, 578]

    PLANT_DIMS = (127, 197)

    PLANT_Y = 350   # Y for all plants
    plant_types = []

    plantCount = -1

    ## CONSTRUCTOR ##
    def __init__(self, type:str, bug, purchase_price:float = 0.0, sale_price:float = 0.0):

        plant.plantCount += 1                   # Increases plant count

        self.stage = 1                          # Initial stage
        self.type = type   
        self.bug = bug                     # Type (string)
        super().__init__(self.get_path())       # Sprite superclass

        self.can_spawn_bugs = False             # Can't spawn bugs until stage 5
        self.bug = bug                       # Bugs to spawn
        self.purchase_price = purchase_price    # Purchase price from buy tab
        self.sale_price = sale_price            # Sell price at stage 5
        plant.plant_types.append(str(self))     # Add plant to list of all plants

        # Location based on past planted 
        self.loc = (plant.PLOT_X_LOCS[plant.plantCount], plant.PLANT_Y)

    def water_plant(self, hours:timeCurrency):
        if hours.can_spend(1):
            if self.stage < 5:
                self.stage += 1
            else:
                return

            if self.stage == 5:
                self.can_spawn_bugs = True

            super().__init__(self.get_path())
        else:
            return

    def get_path(self):
        return f"{self.type}/{self.type}stage{self.stage}.PNG"

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

if __name__ == "__main__":
    flower1 = plant("beebalm")
    flower2 = plant("geranium")


