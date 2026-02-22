import plant
import currency

class plot:
    def __init__(self, plot_plant=None):
        self.plot_plant = plot_plant
        if self.plot_plant != None:
            self.is_empty = False
        else:
            self.is_empty = True

    def sell_plant(self, balance:currency): 
        if not self.is_empty:
            if self.plot_plant.can_sell_plant():
                plant.plant.plant_types.remove(str(self.plot_plant))
                self.plot_plant.reset_stage()

                revenue = self.plot_plant.get_sale_price()
                balance.increase_value(revenue)
                self.is_empty = True
            else:
                print("Error: Plant is not mature, cannot be sold.")
        else:
            print("Error: Plot is empty, no plant to be sold.")

    def buy_plant(self, balance:currency, seed:plant): 
        if not self.is_empty:
            print("Error: Plot is not empty, cannot buy seeds.")
        else:
            seed_price = seed.get_purchase_price()
            if not balance.can_spend(seed_price):
                print("Error: Insufficient funds.")
            else:
                balance.decrease_value(seed_price)
                self.plot_plant = seed
                plant.plant.plant_types.append(str(self.plot_plant))
                self.is_empty = False

    def watch_plant(self):
        if not self.is_empty:
            if self.plot_plant.can_spawn_bugs:
                pass
            else:
                print("Error: Plant cannot spawn bugs, nothing to watch.")
        else:
            print("Error: Plot is empty, no plant to watch.")

    def water(self):
        if not self.is_empty:
            self.plot_plant.water_plant()
        else:
            print("Error: Plot is empty, no plant to water.")

if __name__ == "__main__":
    milkweed = plant.plant("milkweed", sale_price=3.0, purchase_price=1.5)
    geranium = plant.plant("geranium", sale_price=4.0, purchase_price=2.0)

    balance = currency.currency(0)
    print(balance)

    plot1 = plot(milkweed)
    plot1.water()
    plot1.water()
    plot1.water()
    plot1.water()

    plot1.sell_plant(balance)
    print(balance)

    plot1.buy_plant(balance, milkweed)
    print(balance)

    plot1.water()
    plot1.water()
    plot1.water()
    plot1.water()
    
    plot1.sell_plant(balance)
    print(balance)
