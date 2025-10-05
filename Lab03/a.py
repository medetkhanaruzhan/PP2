class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")
        
student1 = Student("Dias",20)
student1.introduce()