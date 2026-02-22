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
                plant.plant_types.remove(self.plot_plant)           # Remove plant from lost
                self.plot_plant.reset_stage()                       # Return to stage 1 for next use

                revenue = self.plot_plant.get_sale_price()          # Funds based on sell price
                
                balance.increase_value(revenue)                     # Add funds to balance
                
                self.plot_plant.visible = False           
                del self.plot_plant
                self.is_empty = True                                # Set plot to empty


                

            # Plant is not stage 5 - cannot sell
            else:
                return

        # Plot has no plant
        else:
            return

    def buy_plant(self, balance:currency, seed:plant): 
        if not self.is_empty:
            return
        else:
            seed_price = seed.get_purchase_price()
            if not balance.can_spend(seed_price):
                return
            else:
                balance.decrease_value(seed_price)
                self.plot_plant = seed
                plant.plant_types.append(self.plot_plant)
                self.is_empty = False

    def watch_plant(self, clock:timeCurrency):
            if not self.is_empty:
                if self.plot_plant.can_spawn_bugs:
                    if not clock.can_spend(1):
                        return "Not enough time!"
                    else:
                        clock.time_spent(1)

                        if random.random() < self.plot_plant.thisBug.probability:
                            self.plot_plant.thisBug.is_found()
                            print("New bug discovered!")
                            return self.plot_plant.thisBug
                        else:
                           return "All bugs discovered for this species"
                else:
                    return "Plant is not mature."
            else:
                return "Plot is empty!"

    def water(self, hours:timeCurrency):
        if hours.can_spend(1):
            if not self.is_empty:
                hours.time_spent(1)
                self.plot_plant.water_plant()
            else:
                return

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
