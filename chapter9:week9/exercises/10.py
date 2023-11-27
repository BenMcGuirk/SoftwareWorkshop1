"""
First, make all the attributes non-public. 
Then, define getters and setters for the three attributes. 
Finally, write two versions of the class: one with the property() function and another one with the @property decorator.
"""

class BouncyBall1:

    def __init__(self, price, size, brand): 
        self._price = price
        self._size = size   
        self._brand = brand

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        self._size = size

    def get_brand(self):
        return self._brand
    
    def set_brand(self, brand):
        self._brand = brand

    thePrice = property(get_price, set_price)
    theSize = property(get_size, set_size)
    theBrand = property(get_brand, set_brand)


class BouncyBall2:

    def __init__(self, price, size, brand): 
        self._price = price
        self._size = size   
        self._brand = brand

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @price.deleter
    def price(self):
        del self._price
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size

    @size.deleter
    def size(self):
        del self._size

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @brand.deleter
    def brand(self):
        del self._brand