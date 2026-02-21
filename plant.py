from sprite import sprite
class plant(sprite):
    numPlants = 0

    ## CONSTRUCTOR ##
    def __init__(self, type:str, img_folder:str, bugs = [], price:float = 0.0):
        super().__init__(f"{img_folder}/{type}stage1.PNG")
        self.stage = 1
        self.type = type

        self.img_folder = img_folder
        numPlants += 1 # type: ignore

        # Individual stage images
        self.stage1image = f"{img_folder}/{type}stage1.PNG"
        self.stage2image = f"{img_folder}/{type}stage2.PNG"
        self.stage3image = f"{img_folder}/{type}stage3.PNG"
        self.stage4image = f"{img_folder}/{type}stage4.PNG"
        self.stage5image = f"{img_folder}/{type}stage5.PNG"

        self.bugs = bugs
        self.price = price

    def water_plant(self):
        if self.stage < 5:
            self.stage += 1
        
    def get_img(self):
        if self.stage == 1:
            return self.stage1image
        elif self.stage == 2:
            return self.stage2image
        elif self.stage == 3:
            return self.stage3image
        elif self.stage == 4:
            return self.stage4image
        else:
            return self.stage5image

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