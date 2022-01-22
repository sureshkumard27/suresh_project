class car:
    def __init__(self):
        self.mileage=10
        self.company="BMW"
c1=car()
c2=car()
c1.mileage=8
print(c1.mileage, c1.company)
print(c2.mileage, c2.company)