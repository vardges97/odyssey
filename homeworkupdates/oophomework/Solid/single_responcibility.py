class coffeemaker:
    def __init__(self,coffee,milk,water_amount,cocoa):
        self.coffee = coffee
        self.milk = milk
        self.water_amount = water_amount
        self.cocoa = cocoa

    def espresso(self,coffee,water_amount):
        ...
    def latte(self,coffee,water_amount,milk):
        ...
    def cappuchino(self,coffee,water_amount,milk):
        ...
    """and so on this violates the single responsibility principle because the class has multiple functions that s
    hould be separated"""

class espressomaker:
    def __init__(self,coffee):
        self.coffee = coffee

    def makeespresso(self,coffee):
        ...

class lattemaker:
    def __init__(self,coffee,milk,water_amount):
        self.coffee = coffee
        self.milk = milk
        self.water_amount = water_amount

    def make_latte(self,coffee,milk,water_amount,milk_amount):
        ...
