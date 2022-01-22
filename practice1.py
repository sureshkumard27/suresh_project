class Computer:
    type="Laptop"
    def config(self):
        print("i5", "16GB", "1TB")
com1=Computer()
com2=Computer()
Computer.config(com1)
com1.config()
com2.config()
print(com1.type)
print(com2.type)