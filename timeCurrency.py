from stopwatch import stopwatch
class timeCurrency:

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def add_hours(self,hours=1):
        self.value += hours

    def add_from_timer(self,timer:stopwatch):
        self.value += timer.elapsed_time
        timer.reset()

    def time_spent(self,hours): #helper for buy
        self.value -= hours

    def can_spend(self, hours_required): #helper for buy
        if self.value - hours_required >= 0:
            return True
        else:
            return False   

    def buy(self,hours_price): 
        if self.can_spend(hours_price):
            self.time_spent(hours_price)
        else:
            print("Not enough hours!")

    def set(self, value):
        self.value = value