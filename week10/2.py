"""
Create a Panda class that inherits from the Mammal class (see below).
• Make Panda inherit all the attributes defined in Mammal
• Add a class attribute to Panda: is_endangered = True
• Add an instance attribute: code
• Create an instance of Panda and store it in the variable my_panda. You can choose
any values as the arguments used to create the instance.
"""

class Mamal:
    def __init__(self, name, age, health, num_offspring, years_in_captivity):
        self.name = name
        self.age = age
        self.health = health
        self.num_offspring = num_offspring
        self.years_in_captivity = years_in_captivity

class panda(Mamal):
    def __init__(self, name, age, health, num_offspring, years_in_captivity, is_endangered = True):
        Mamal.__init__(self, name, age, health, num_offspring, years_in_captivity)
        self.is_endangered = is_endangered
    
my_panda = panda('Steve', 22, 'Good', 4, 10)