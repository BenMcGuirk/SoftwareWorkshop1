"""
Refactor code so that there is less repeated code (create superclass called lecturer)

class ComputerLecturer(object):
    salary = 100000
    monthly_bonus = 500
    def __init__(self, name, age, address, phone,
programming_modules):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.programming_modules = programming_modules
class LinguisticsLecturer(object):
    salary = 100000
    monthly_bonus = 500
    def __init__(self, name, age, address, phone, bilingual):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.bilingual = bilingual
"""

#Refactored code:

class lecturer(object): 
    salary = 100000
    monthly_bonus = 500
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

class ComputerLecturer(lecturer):
    def __init__(self, name, age, address, phone, programming_modules):
        lecturer.__init__(self, name, age, address, phone)
        self.programming_modules = programming_modules

class LinguisticsLecturer(lecturer):
    def __init__(self, name, age, address, phone, bilingual):
        lecturer.__init__(self, name, age, address, phone)
        self.bilingual = bilingual