## IMPORTS ##
from sprite import sprite
from button import button
from staticMethods import resource_path
#############

class plotMenu(sprite):


    def __init__(self):
        super().__init__(resource_path("./Plot Menu Sprites/plotmenubase.PNG"))

        self.plotBuy = None
        self.plotWater = None
        self.plotWatch = None
        self.plotSell = None

        self.enable("buy")
        self.enable("water")
        self.enable("watch")
        self.enable("sell")

        self.hide()


    def enable(self, buttonType:str):
        if buttonType == "buy":
            self.plotBuy = button(resource_path("./Plot Menu Sprites/plotmenubuyenabled.PNG"), self.get_location(), "buy")
            self.plotBuy.pressRect = (self.get_location()[0] + 56, self.get_location()[1] + 46, 80, 28)

        if buttonType == "water":
            self.plotWater = button(resource_path("./Plot Menu Sprites/plotmenuwaterenabled.PNG"), self.get_location(), "water")
            self.plotWater.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 83, 75, 30)

        if buttonType == "watch":
            self.plotWatch = button(resource_path("./Plot Menu Sprites/plotmenuwatchenabled.PNG"), self.get_location(), "watch")
            self.plotWatch.pressRect = (self.get_location()[0] + 58, self.get_location()[1] + 120, 75, 27)

        if buttonType == "sell":
            self.plotSell = button(resource_path("./Plot Menu Sprites/plotmenusellenabled.PNG"), self.get_location(), "sell")
            self.plotSell.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 153, 75, 30)


    def disable(self, buttonType:str):
        if buttonType == "buy":
            self.plotBuy = button(resource_path("./Plot Menu Sprites/plotmenubuydisabled.PNG"))
            self.plotBuy.pressRect = (self.get_location()[0] + 56, self.get_location()[1] + 46, 80, 28)

        if buttonType == "water":
            self.plotWater = button(resource_path("./Plot Menu Sprites/plotmenuwaterdisabled.PNG"))
            self.plotWater.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 83, 75, 30)

        if buttonType == "watch":
            self.plotWatch = button(resource_path("./Plot Menu Sprites/plotmenuwatchdisabled.PNG"))
            self.plotWatch.pressRect = (self.get_location()[0] + 58, self.get_location()[1] + 120, 75, 27)

        if buttonType == "sell":
            self.plotSell = button(resource_path("./Plot Menu Sprites/plotmenuselldisabled.PNG"))
            self.plotSell.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 153, 75, 30)


    def show(self, mousePos:tuple):
        self.move(mousePos)

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


    def move(self, newLoc:tuple):
        self.loc = newLoc

        self.plotBuy.pressRect = (self.get_location()[0] + 56, self.get_location()[1] + 46, 80, 28)
        self.plotBuy.loc = newLoc
        self.plotWater.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 83, 75, 30)
        self.plotWater.loc = newLoc
        self.plotWatch.pressRect = (self.get_location()[0] + 58, self.get_location()[1] + 120, 75, 27)
        self.plotWatch.loc = newLoc
        self.plotSell.pressRect = (self.get_location()[0] + 59, self.get_location()[1] + 153, 75, 30)
        self.plotSell.loc = newLoc


    def hide(self):
        if self.visible == False:
            return
        else:
            self.visible = False
            self.plotBuy.visible = False
            self.plotWater.visible = False
            self.plotWatch.visible = False
            self.plotSell.visible = False

