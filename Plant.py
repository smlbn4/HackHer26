class plant:
    def __init__(self, type, img_folder, bugs, price):
        self.stage = 1
        self.type = type
        self.img_folder = img_folder
        self.bugs = bugs
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


    
