import time


def row_sum_odd_numbers(n):
    return n * n * n


def main():
    n = int(input("Enter the height of your tree: "))
    print(row_sum_odd_numbers(n))


def exception_handling():
    try:
        main()
    except:
        print("Please put an Integer number. Try it again")
        time.sleep(2)
        exception_handling()


exception_handling()
