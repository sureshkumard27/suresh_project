class Student:
    college = "KL University"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return(self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls):
        return cls.college

s1=Student(86,97,59)
s2=Student(98,67,85)
print(s1.avg(), s2.avg())
print(Student.info())

