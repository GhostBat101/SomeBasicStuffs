def sort(nums):
    for i in range(len(nums) - 1):
        minpos = i
        k = len(nums)
        for j in range(i, k):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp


def input_data():
    i = input("\nEnter the numbers : ").strip().split()
    return i

# Basic way of getting input from the user
# n = int(input("Enter number of elements : "))
# iterating till the range
# for i in range(0, n):
#    ele = int(input())
#    lst.append(ele)  # adding the element
# print(lst)

# using map and exception handling
try:
    print("Please use a [space] between each input.")
    lst = list(map(int, input_data()))
    print("Unsorted list: ", lst)
    sort(lst)
    print("Sorted list: ", lst)
except:
    print("Wrong inputs. Only use Int values")
