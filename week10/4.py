"""
Create two classes that inherit from the Pizza class (See the code below)
• PizzaMargherita class. Instance attribute: has_extra_cheese
• PizzaMarinara class. Instance attribute: has_extra_basil
• These two classes must inherit all the instance attributes of the Pizza class.
• Create two instances, one of each subclass and assign them to their corresponding
variable
"""

class Pizza:
    def __init__(self, size, toppings, price, rating):
        self.size = size  # "Small", "Medium", or "Large"
        self.toppings = toppings  # A list of toppings
        self.price = price
        self.rating = rating  # Scale from 1 to 5
# Add the subclasses below this line

class PizzaMargherita(Pizza):
    def __init__(self, size, toppings, price, rating, has_extra_cheese):
        Pizza.__init__(self, size, toppings, price, rating)
        self.has_extra_cheese = has_extra_cheese

class PizzaMarinara(Pizza): 
    def __init__(self, size, toppings, price, rating, has_extra_basil):
        Pizza.__init__(self, size, toppings, price, rating)
        self.has_extra_basil = has_extra_basil

pizza_margherita = PizzaMargherita('Small', ['Cheese', 'Tomato'], 10, 4, True)
pizza_marinara = PizzaMarinara('Medium', ['Cheese', 'Tomato'], 12, 3, True)