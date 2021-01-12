import re

print("#Notice: this will only work with if the alphabets are encrypted. And Not the Signs like +/- signs")
raw = input("File loaction: ")
data = open(raw).read()

print("".join(re.findall("[A-Za-z]", data)))
print(re.findall("[A-Za-z]", data))