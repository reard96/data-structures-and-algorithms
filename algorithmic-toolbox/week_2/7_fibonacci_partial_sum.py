# Uses python3
import sys

# helper function
def fibonacci_sum_last_digit(n):
    if n < 2:
        return n

    sumArray = [1, 1]

    # Pisano period of 60
    n = n % 60
    for _ in range(n):
        sumArray.append((sumArray[-1] + sumArray[-2]) % 10)

    return (sumArray[-1] - 1) % 10

def fibonacci_partial_sum(from_, to):
    return ((fibonacci_sum_last_digit(to) + 10) - fibonacci_sum_last_digit(from_ - 1)) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
