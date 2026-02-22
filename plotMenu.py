import pygame
from sprite import sprite
from button import button

class plotMenu(sprite):


    def __init__(self):
        super().__init__("./Plot Menu Sprites/plotmenubase.PNG")

        self.plotBuy = None
        self.plotWater = None
        self.plotWatch = None
        self.plotSell = None

        self.enable("buy")
        self.disable("water")
        self.disable("watch")
        self.disable("sell")


    def enable(self, buttonType:str):
        if buttonType == "buy":
            self.plotBuy = button("./Plot Menu Sprites/plotmenubuyenabled.PNG")
            self.plotBuy.pressRect = (self.get_location()[0] + 56, self.get_location()[1] + 46, 80, 28)

        if buttonType == "water":
            self.plotWater = button("./Plot Menu Sprites/plotmenuwaterenabled.PNG")
            self.plotWater.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 83, 75, 30)

        if buttonType == "watch":
            self.plotWatch = button("./Plot Menu Sprites/plotmenuwatchenabled.PNG")
            self.plotWatch.pressRect = (self.get_location()[0] + 58, self.get_location()[1] + 153, 75, 27)

        if buttonType == "sell":
            self.plotSell = button("./Plot Menu Sprites/plotmenusellenabled.PNG")
            self.plotSell.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 83, 75, 30)


    def disable(self, buttonType:str):
        if buttonType == "buy":
            self.plotBuy = button("./Plot Menu Sprites/plotmenubuydisabled.PNG")
            self.plotBuy.pressRect = (self.get_location()[0] + 56, self.get_location()[1] + 46, 80, 28)

        if buttonType == "water":
            self.plotWater = button("./Plot Menu Sprites/plotmenuwaterdisabled.PNG")
            self.plotWater.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 83, 75, 30)

        if buttonType == "watch":
            self.plotWatch = button("./Plot Menu Sprites/plotmenuwatchdisabled.PNG")
            self.plotWatch.pressRect = (self.get_location()[0] + 58, self.get_location()[1] + 153, 75, 27)

        if buttonType == "sell":
            self.plotSell = button("./Plot Menu Sprites/plotmenuselldisabled.PNG")
            self.plotSell.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 83, 75, 30)