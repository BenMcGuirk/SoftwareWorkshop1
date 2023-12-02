"""
You just signed up for a video game development competition and your team decided to 
use inheritance to represent the characters. Some team members have made mistakes 
in the code and the inheritance is not working correctly. The due date to submit the 
game is tomorrow and you are the only one who can save your team from being 
disqualified.

Your task is to:
Fix the errors in the code developed by your team. Implement the correct hierarchy.
 Requirements:
Enemy must be a subclass of Character.
Player must be a subclass of Character.
Enemy must be a superclass of DifficultEnemy and EasyEnemy.

This is the code that your team wrote. It throws many errors and the inheritance is 
not defined correctly.
"""

class Character:
    def __init__(self, x, y, img_file, speed, life_counter):
        self.x = x
        self.y = y
        self.img_file = img_file
        self.speed = speed
        self.life_counter = life_counter

class Enemy(Character):
    def __init__(self, x, y, img_file, speed, life_counter, message):
        Character.__init__(self, x, y, img_file, speed, life_counter)
        self.message = "I'm here to protect my master"

class Player(Character):
    def __init__(self, x, y, img_file, speed, life_counter):
        Character.__init__(self, y, img_file, speed, life_counter)
        self.speed = 56

class DifficultEnemy(Enemy):
      def __init__(self, x, y, img_file):
          Enemy.__init__(self, img_file, 80)

class EasyEnemy(Enemy):
    def __init__(self, x, y, img_file, 40):
        Enemy.__init__(self, x, y, img_file)
        self.life_counter = 1