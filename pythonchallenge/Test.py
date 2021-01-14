from numpy import *
from array import *


arr = array('i', [])

n = int(input("Enter the number of elements you want: "))

for i in range(n):
    x = int(input("Enter the Value: "))
    arr.append(x)
k = 0
val = int(input("Enter what value you want to search for: "))
for i in arr:
    if i == val:
        print(k)
        break
    else:
        print("Not in the Array")
        break
    k += 1


