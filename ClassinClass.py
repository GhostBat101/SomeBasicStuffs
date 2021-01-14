class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def showinfo(self):
        print(self.name, self.roll)

    class Laptop:
        def __init__(self):
            self.brand = 'hp'
            self.ram = 16
            self.cpu = 'ryzen 9'


s1 = Student('Jack', 20)
s2 = Student('Rohan', 10)

print(s1.showinfo())
