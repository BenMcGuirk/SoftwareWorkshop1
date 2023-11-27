"""
**Building a Movie Class with Unique IDs** <br>

**Objective:** Understand the implementation of class and instance attributes, and how to manage unique identifiers for each 
class instance in Python. <br>

**Task Description:**
> Define a class named **Movie**. <br>
> > Within the class, create a class attribute named **id_counter** initialized to 0. This attribute will track the next 
available ID for new movie instances. <br>
> > Define the **_ _init_ _** method to accept **title** and **rating** as parameters. Additionally, the **_ _init_ _** 
method should automatically set an **id** instance attribute by incrementing **Movie.id_counter** and assign this new value to 
the **id**.

> Ensure that each new **Movie** instance has a unique **id** by incrementing **Movie.id_counter** each time a new instance 
is created.<br>
> Inside the **Movie** class, define a method info that prints out the movie's ID, title, and rating in a readable format.<br>
Test your class:<br>
> > Create an instance of the **Movie** class with the title "Inception" and a rating of 8.8.
> > Create another instance of the **Movie** class with the title "The Matrix" and a rating of 8.7.
> > Call the **info** method on both instances to display their information.

**Expected Output:** When calling the **info** method on your **Movie** instances, the output should display the ID, title, 
and rating of each movie, like so:


ID: 1, Title: Inception, Rating: 8.8ID: 2, Title: The Matrix, Rating: 8.7



**Guidelines:** <br>
> > Remember that the **id_counter** should be incremented only within the _ _init_ _ method.
> > Do not forget to use the **self** keyword when working with instance attributes.
> > Use the **@classmethod** decorator if you decide to create a class method to increment the **id_counter**.
> > Provide comments in your code to explain the purpose of each method and attribute.
"""

class Movie:
    id_counter = 0

    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
        Movie.id_counter += 1
        self.id = Movie.id_counter

    def info(self):
        print(f"ID: {self.id}, Title: {self.title}, Rating: {self.rating}")

movie1 = Movie("Inception", 8.8)
movie2 = Movie("The Matrix", 8.7)

movie1.info()
movie2.info()