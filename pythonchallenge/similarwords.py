import re
raw = input("File location: ")
data = open(raw).read()

list1 = re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)

print("".join(list1))