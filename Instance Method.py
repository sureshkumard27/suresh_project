class Student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    #setter method(mutator)

    def set(self):
        m1=85
    #getter method(accessor)
    def avg(self):
        return(self.m1+self.m2+self.m3)/3

s1 = Student(84,97,99)
s2 = Student(96,85,82)

s1.set()

print(s1.avg())
print(s2.avg())