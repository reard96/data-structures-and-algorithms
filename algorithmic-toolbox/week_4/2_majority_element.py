# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    first_maj_elem = get_majority_element(a, left, (left + right - 1) // 2 + 1)
    second_maj_elem = get_majority_element(a, (left + right - 1) // 2 + 1, right)

    first_counter = 0
    for i in range(left, right):
        if a[i] == first_maj_elem:
            first_counter += 1
    if first_counter > (right - left) // 2:
        return first_maj_elem

    second_counter = 0
    for i in range(left, right):
        if a[i] == second_maj_elem:
            second_counter += 1
    if second_counter > (right - left) // 2:
        return second_maj_elem

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
