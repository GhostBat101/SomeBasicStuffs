def oddeven(list: object) -> object:
    even = 0
    odd = 0
    for i in list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


def main():
    # empty list
    lst = []

    # input number of elements
    n = int(input("Enter number of elements : "))
    print("Write the elements: ")
    # iterating till the range
    for i in range(0, n):
        ele = int(input())

        lst.append(ele)  # adding the element
    x = oddeven(lst)
    print("The created list is: "+str(lst))
    print("The number of even and odds are- "+str(x))

main()
