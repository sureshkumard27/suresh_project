class Student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self):
        self.m1=40

s1=Student(85,97,88)
s2=Student(78,96,99)

s1.get_m1()
s1.set_m1()
print(s1.avg())
print(s2.avg())
print(s1.m1)