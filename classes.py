class student:
    marks=98
    def __init__(self,name,age):
        self.name=name
        self.age=age
s=student("ram",24)
print("student name is",s.name)
print("student age is",s.age)
print("student marks is",s.marks)
