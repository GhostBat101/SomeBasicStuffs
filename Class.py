
class Computer:
    def specs(self):
        print("Ryzen 9 5900X 16GB RAM 1TB SSD")


conf1 = Computer

Computer.specs(conf1)
conf1.specs(self=conf1)