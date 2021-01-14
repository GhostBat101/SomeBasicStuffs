class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def showinfo(self):
        print(self.name, self.roll)
    class Laptop:
        pass

s1 = Student('Jack', 20)
s2 = Student('Rohan', 10)

print(s1.showinfo())