
class Computer:
    def __init__(self, cpu, ram, ssd):
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd

    def specs(self):
        print("config is: ", self.cpu, self.ram, self.ssd)


conf1 = Computer ('i7', '16GB', '1TB')
conf2 = Computer('Ryzen 7', '16GB', '1TB')


Computer.specs(conf1)
Computer.specs(conf2)
conf2.specs()