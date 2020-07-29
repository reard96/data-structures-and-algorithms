# Uses python3
from sys import stdin

def fibonacci_sum_squares(n):
    if n < 2:
        return n

    sumArray = [1, 1]

    # Pisano period of 60
    n = n % 60
    for _ in range(n):
        sumArray.append((sumArray[-1] ** 2 + sumArray[-2] ** 2) % 10)

    return (sumArray[-1] - 1) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
