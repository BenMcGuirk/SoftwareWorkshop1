"""
First, make all the attributes non-public.
Then, define getters and setters for the three attributes.
Make sure that price is > 0 
Make sure that size should be related to one of the following values (small, medium and large)
Make sure that brand is a string
"""

class BouncyBall:

    def __init__(self, price, size, brand):
        self._price = price 
        self._size = size 
        self._brand = brand

    def get_price(self):
        return self._price
    
    def set_price(self, price):
        if price < 0:
            print('Invalid price')
        self._price = price
    
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if size != 'small' and size != 'medium' and size != 'large':
            print('Invalid size')
        self._size = size
    
    def get_brand(self):
        return self._brand
    
    def set_brand(self, brand):
        if type(brand) is str:
            self._brand = brand
        print('Invalid brand')