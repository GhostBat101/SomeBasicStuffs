def sort(nums):
    for i in range(len(nums)-1):
        minpos = i
        k = len(nums)
        for j in range(i, k):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp


lst = []

# number of elemetns as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    lst.append(ele)  # adding the element
sort(lst)
print(lst)