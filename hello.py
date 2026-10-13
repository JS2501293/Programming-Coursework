class Student:
    def __init__(self, name, student_id, grade):
        self.name = name 
        self.student_id = student_id
        self.grade = grade

    def get_name(self):
        return self.name

    def get_id(self):
        return self.student_id

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def display_info(self):
        print(f"NAME: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Grade: {self.grade}")
        
        
