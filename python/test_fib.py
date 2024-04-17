def fibonacci_check(number):
    # Function that checks if 'number' is one of the first 52 Fibonacci numbers
    # It generates each next number in the Fibonacci sequence untill:
    #   1 - The input number has been found as a Fibonacci number
    #   2 - The maximum iterations are exceeded
    #   3 - The input number is smaller than the next Fibonacci number
    # Adapted from: https://www.geeksforgeeks.org/python-program-to-print-the-fibonacci-sequence/

    if number < 0:
        print("Negative number")
        return False
    if number == 0:
        print("Fibonacci number found, input: 0, count: 0")
        return True

    max_iter = 51
    n1 = 0
    n2 = 1
    next_number = n2
    count = 1

    while count <= max_iter and number >= next_number:
        count += 1
        if number == next_number:
            print("Fibonacci number found, input: {}, count: {}".format(number, count))
            return True

        n1, n2 = n2, next_number
        next_number = n1 + n2

    print("Not a fibonacci number (or larger than the 52nd): input: {}, next Fibonacci: {}, previous Fibonacci: {}".format(number, next_number, n2))

    return False


print(fibonacci_check(-1))
print()
print(fibonacci_check(1))
print()
print(fibonacci_check(5))
print()
print(fibonacci_check(4))
print()
print(fibonacci_check(6767))
print()
print(fibonacci_check(832040))
print()
print(fibonacci_check(32951280099))
print()
print(fibonacci_check(53316291173))
