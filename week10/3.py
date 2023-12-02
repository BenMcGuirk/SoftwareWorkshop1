"""
Convert the diagram hierarchy into python code.
Please include attributes and methods.
Create some instances of the classes.
Make sure general attributes are in the superclass.
Include unique attributes to subclasses.

1 Electronic device(voltage, weight, height, color)
2 Computer(memory, hard_drive) .. TV(resolution, has_sky)
3 Desktop() .. Laptop(C)
"""

class ElectronicDevice:
    def __init__(self, voltage, weight, height, color):
        self.voltage = voltage
        self.weight = weight
        self.height = height
        self.color = color

class Computer(ElectronicDevice):
    def __init__(self, voltage, weight, height, color, memory, hard_drive):
        super().__init__(voltage, weight, height, color)
        self.memory = memory
        self.hard_drive = hard_drive

class Desktop(Computer):
    def __init__(self, voltage, weight, height, color, memory, hard_drive):
        super().__init__(voltage, weight, height, color, memory, hard_drive)

class Laptop(Computer):
    def __init__(self, voltage, weight, height, color, memory, hard_drive):
        super().__init__(voltage, weight, height, color, memory, hard_drive)

class TV(ElectronicDevice):
    def __init__(self, voltage, weight, height, color, resolution, has_sky):
        super().__init__(voltage, weight, height, color)
        self.resolution = resolution
        self.has_sky = has_sky