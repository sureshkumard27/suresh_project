class first:
    def first(self):
        print("first")


class second(first):
    def second(self):
        print("second")


class final(second):
    def final(self):
        print("final")


a = final()
a.first()
a.second()
a.final()
