def square_digits(num):
    new = []
    for i in str(num):
        new.append(str(int(i) ** 2))
    return int("".join(new))


def iterate(num):
    data = str(num)
    new = map(int, data)
    for c in new:
        print(c * c, end="")




inti = 1203
print("Using list: ",square_digits(inti))
print("Using map: ", end="")
iterate(inti)
