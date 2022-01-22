class person:
    def __init__(self):
        self.name="Naveen"
        self.age=28

    def update(self):
        self.age=30

    c1=person()
    c2=person()
    c1.name="rashi"
    c1.age=12
    c1.update()
    print(c1.name)
    print(c1.age)
    print(c2.name)
    print(c2.age)