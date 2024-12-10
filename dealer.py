class Dealer:
    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory
    

class Inventory(Dealer):
    def __init__(self, make, model, trim, year, odometer, colour, transmission, price):
        self.make = make
        self.model = model
        self.trim = trim
        self.year = year
        self.odometer = odometer
        self.colour = colour
        self.transmission = transmission
        self.price = price
        
