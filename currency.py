class currency:
    def __init__(self, value:float = 0):
        self.value = value

    def increase_value(self, amt):
        self.value += amt

    def decrease_value(self, amt):
        self.value -= amt

    def get_value(self):
        return self.value
    
    def can_spend(self, amt):
        if self.value - amt >= 0:
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.value}"
        
        