from sprite import sprite
class plant(sprite):
    plant_types = []

    ## CONSTRUCTOR ##
    def __init__(self, type:str, bugs = [], purchase_price:float = 0.0, sale_price:float = 0.0):
        self.stage = 1
        self.type = type
        super().__init__(self.get_path())

        self.can_spawn_bugs = False
        self.bugs = bugs
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        plant.plant_types.append(str(self))

    def water_plant(self):
        if self.stage < 5:
            self.stage += 1
        else:
            return

        if self.stage == 5:
            self.can_spawn_bugs = True

        super().__init__(self.get_path())

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
        self.stage = 0
   
    def __str__(self):
        return self.type

if __name__ == "__main__":
    flower1 = plant("beebalm")
    flower2 = plant("geranium")


