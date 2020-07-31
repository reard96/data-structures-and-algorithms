#Uses python3

import sys

# helper function
def is_greater_or_equal(a, b):
    # sort of cheating but will turn them to strings to compare
    return int(str(a) + str(b)) >= int(str(b) + str(a))

def largest_number(a):
    res = ""
    while len(a) > 0:
        max_digit = 0
        for x in a:
            if is_greater_or_equal(int(x), max_digit):
                max_digit = int(x)
        res += str(max_digit)
        a.remove(str(max_digit))
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

