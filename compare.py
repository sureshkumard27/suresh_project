class Person:
    def __init__(self):
        self.name="Naveen"
        self.age=28

    def compare(self,other):
        if self.age==other.age:
            return true
        else:
            return false

p1=Person()
p1.age=30
p2=Person()
p1.compare(p2)
'''if(p1.compare(p2)):
    print("They are same")
else:
    print("They are different")'''



