"""
Update the code below so the welcome_students method in the superclass can be executed 
when you run the code of my_science_teacher.welcome_students()
"""
class Teacher:
    def __init__(self, full_name, teacher_id):
        self.full_name = full_name
        self.teacher_id = teacher_id
    def welcome_students(self):
        print(f"Welcome to class!, I'm your teacher1. My name is {self.full_name}.") # This line is not working
class ScienceTeacher(Teacher):
    def __init__(self, full_name, teacher_id):
        Teacher.__init__(self, full_name, teacher_id)
my_science_teacher = ScienceTeacher("Emily Smith", "S355A213")
my_science_teacher.welcome_students()