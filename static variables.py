class car:
    wheels=4
    def __init__(self):
        self.mileage=10
        self.company="BMW"
c1=car()
c2=car()
c1.mileage=8
car.wheels=5
print(c1.mileage, c1.company, c1.wheels)
print(c2.mileage, c2.company, c2.wheels)
