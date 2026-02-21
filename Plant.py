class Plant:
    def __init__(self, type, img_folder, bug_dict, price):
        self.stage = 1
        self.type = type
        self.img_folder = img_folder
        self.bug_dict = bug_dict
        self.price = price

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

if __name__ == "__main__":
    flower1 = Plant("Daisy", "demo_img_folder", {"Common": 0.33, "Rare": 0.1}, 3.50)
    
    flower1.water_plant()
    
