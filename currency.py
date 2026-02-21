class currency:
    def __init__(self, value):
        self.value = value

    def increase_value(self, x):
        self.value += x

    def decrease_value(self, x):
        self.value -= x

    def get_value(self):
        return self.value
    
    def can_spend(self, amt):
        if self.value - amt >= 0:
            return True
        else:
            return False
        
        