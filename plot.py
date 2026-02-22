import plant
import currency

class plot:
    def __init__(self, plot_plant=None):
        self.isEmpty = True
        self.plot_plant = plot_plant

    def sell_plant(self, balance:currency):
        if self.plot_plant.can_sell_plant():
            plant.plant.plant_types.remove(str(self.plot_plant))

            revenue = self.plot_plant.get_sale_price()
            balance.increase_value(revenue)
        else:
            print("Error: Plant is not mature, cannot be sold.")


if __name__ == "__main__":
    flower1 = plant.plant("PLC", "./Placeholder Sprites/testPlant", sale_price=3.0)
    flower1.water_plant()
    flower1.water_plant()
    flower1.water_plant()
    flower1.water_plant()

    balance = currency.currency(0)
    print(balance, 2)

    plot1 = plot(flower1)

    plot1.sell_plant(balance)
    print(balance)

