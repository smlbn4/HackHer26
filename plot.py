import random
from plant import plant
from currency import currency
from timeCurrency import timeCurrency
from bug import bug

class plot:
    
    ## CONSTRUCTOR ##
    def __init__(self, plot_plant=None):        # Initialized empty
        self.plot_plant = plot_plant
        
        if self.plot_plant == None:
            self.is_empty = True
        else:
            self.is_empty = False

    ## METHODS ##
    def sell_plant(self, balance:currency):
        # If there is a plant in slot
        if not self.is_empty:
            # Is mature?
            if self.plot_plant.can_sell_plant():
                plant.plant_types.remove(str(self.plot_plant))      # Remove plant from lost
                self.plot_plant.reset_stage()                       # Return to stage 1 for next use

                revenue = self.plot_plant.get_sale_price()          # Funds based on sell price
                balance.increase_value(revenue)                     # Add funds to balance
                self.is_empty = True                                # Set plot to empty

            # Plant is not stage 5 - cannot sell
            else:
                print("Error: Plant is not mature, cannot be sold.")

        # Plot has no plant
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
                plant.plant_types.append(str(self.plot_plant))
                self.is_empty = False

    def watch_plant(self, clock:timeCurrency):
            if not self.is_empty:
                if self.plot_plant.can_spawn_bugs:
                    if not clock.can_spend(1):
                        print("Not enough hours!")
                    else:
                        clock.time_spent(1)
                        unfound_bugs = []

                        for dude in self.plot_plant.bugs:
                            if not dude.found:
                                unfound_bugs.append(dude)

                        if len(unfound_bugs) == 0:
                            print("All bugs discovered!!!!")
                        else:
                            for dude in unfound_bugs:
                                if random.random() < dude.probability:
                                    print(f"New Discovery!!! \n{dude.type}")
                                else:
                                    print("no little dudes found :(")

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
    bumblebee = bug("bumblebee", 0.4, "milkweed")

    milkweed = plant("milkweed", bugs=[bumblebee], sale_price=3.0, purchase_price=1.5)
    geranium = plant("geranium", sale_price=4.0, purchase_price=2.0)

    balance = currency(20)
    print(balance)

    plot1 = plot(milkweed)
    plot1.water()
    plot1.water()
    plot1.water()
    plot1.water()

    timer = timeCurrency(10)
    plot1.watch_plant(timer)

    plot1.buy_plant(balance, milkweed)
    print(balance)

    plot1.water()
    plot1.water()
    plot1.water()
    plot1.water()
    
    plot1.sell_plant(balance)
    print(balance)
