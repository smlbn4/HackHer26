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

        self.visible = False



    def enable(self, buttonType:str):
        if buttonType == "buy":
            self.plotBuy = button("./Plot Menu Sprites/plotmenubuyenabled.PNG", self.get_location(), "buy")
            self.plotBuy.pressRect = (self.get_location()[0] + 56, self.get_location()[1] + 46, 80, 28)

        if buttonType == "water":
            self.plotWater = button("./Plot Menu Sprites/plotmenuwaterenabled.PNG", self.get_location(), "water")
            self.plotWater.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 83, 75, 30)

        if buttonType == "watch":
            self.plotWatch = button("./Plot Menu Sprites/plotmenuwatchenabled.PNG", self.get_location(), "watch")
            self.plotWatch.pressRect = (self.get_location()[0] + 58, self.get_location()[1] + 153, 75, 27)

        if buttonType == "sell":
            self.plotSell = button("./Plot Menu Sprites/plotmenusellenabled.PNG", self.get_location(), "sell")
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

    def set_position(self, loc:tuple):
        self.loc = loc

        self.plotBuy.pressRect = (self.get_location()[0] + 56, self.get_location()[1] + 46, 80, 28)
        self.plotWater.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 83, 75, 30)
        self.plotWatch.pressRect = (self.get_location()[0] + 58, self.get_location()[1] + 153, 75, 27)
        self.plotSell.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 83, 75, 30)

    def show(self, mousePos:tuple):
        self.set_position(mousePos)

