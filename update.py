class Person:
    def __init__(self):
        self.name="Naveen"
        self.age=28
    def update(self):
        self.age=30
p1=Person()
p2=Person()

p1.name="rashi"
p1.age=12
p1.update()

print(p1.name, p1.age)
print(p2.name, p2.age)