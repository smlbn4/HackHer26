from sprite import sprite
class plant(sprite):
    numPlants = 0

    ## CONSTRUCTOR ##
    def __init__(self, type:str, img_folder:str, bugs = [], price:float = 0.0):
        self.stage = 1
        self.type = type
        self.img_folder = img_folder
        super().__init__(self.get_path())

        self.bugs = bugs
        self.price = price

    def water_plant(self):
        if self.stage < 5:
            self.stage += 1

        super().__init__(self.get_path())

    def get_path(self):
        return f"{self.img_folder}/{self.type}stage{self.stage}.PNG"

    def can_sell_plant(self):
        if self.stage == 5:
            return True
        else:
            return False
        
    def get_price(self):
        return self.price
    
if __name__ == "__main__":
    daisy = plant("PLC", "./Placeholder Sprites/testPlant")
    daisy.water_plant()
    print(daisy.get_img())