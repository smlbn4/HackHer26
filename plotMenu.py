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

        self.hide()


    def enable(self, buttonType:str):
        if buttonType == "buy":
            self.plotBuy = button("./Plot Menu Sprites/plotmenubuyenabled.PNG", self.get_location(), "buy")
            self.plotBuy.pressRect = (self.get_location()[0] + 56, self.get_location()[1] + 46, 80, 28)

        if buttonType == "water":
            self.plotWater = button("./Plot Menu Sprites/plotmenuwaterenabled.PNG", self.get_location(), "water")
            self.plotWater.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 83, 75, 30)

        if buttonType == "watch":
            self.plotWatch = button("./Plot Menu Sprites/plotmenuwatchenabled.PNG", self.get_location(), "watch")
            self.plotWatch.pressRect = (self.get_location()[0] + 58, self.get_location()[1] + 120, 75, 27)

        if buttonType == "sell":
            self.plotSell = button("./Plot Menu Sprites/plotmenusellenabled.PNG", self.get_location(), "sell")
            self.plotSell.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 153, 75, 30)


    def disable(self, buttonType:str):
        if buttonType == "buy":
            self.plotBuy = button("./Plot Menu Sprites/plotmenubuydisabled.PNG")
            self.plotBuy.pressRect = (self.get_location()[0] + 56, self.get_location()[1] + 46, 80, 28)

        if buttonType == "water":
            self.plotWater = button("./Plot Menu Sprites/plotmenuwaterdisabled.PNG")
            self.plotWater.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 83, 75, 30)

        if buttonType == "watch":
            self.plotWatch = button("./Plot Menu Sprites/plotmenuwatchdisabled.PNG")
            self.plotWatch.pressRect = (self.get_location()[0] + 58, self.get_location()[1] + 120, 75, 27)

        if buttonType == "sell":
            self.plotSell = button("./Plot Menu Sprites/plotmenuselldisabled.PNG")
            self.plotSell.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 153, 75, 30)


    def show(self, mousePos:tuple):
        self.set_position(mousePos)

        self.visible = True
        
        self.plotBuy.visible = True
        self.plotWater.visible = True
        self.plotWatch.visible = True
        self.plotSell.visible = True


    def hide(self):
        self.visible = False
        
        self.plotBuy.visible = False
        self.plotWater.visible = False
        self.plotWatch.visible = False
        self.plotSell.visible = False


    def set_position(self, newLoc:tuple):
        self.loc = newLoc

        self.plotBuy.move((self.get_location()[0], self.get_location()[1]))
        self.plotWater.move((self.get_location()[0], self.get_location()[1]))
        self.plotWatch.move((self.get_location()[0], self.get_location()[1]))
        self.plotSell.move((self.get_location()[0], self.get_location()[1]))


    def hide(self):
        if self.visible == False:
            return
        else:
            self.visible = False
            self.plotBuy.visible = False
            self.plotWater.visible = False
            self.plotWatch.visible = False
            self.plotSell.visible = False

