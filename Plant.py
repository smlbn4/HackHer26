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
        return self.img_folder + "/stage" + self.stage + ".png"

    def can_sell_plant(self):
        if self.stage == 5:
            return True
        else:
            return False
        
    def get_price(self):
        return self.price



