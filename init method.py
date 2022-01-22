class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("config detials of computer is",self.cpu,self.ram)

com1=Computer("i5","16gb")
com2=Computer("rhyzen 3", "32gb")
com1.cpu="i3"


com1.config()
com2.config()