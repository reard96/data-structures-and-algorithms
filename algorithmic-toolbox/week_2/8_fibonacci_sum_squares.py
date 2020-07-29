# Uses python3
from sys import stdin

# Helper function
def fibonacci_last_digit(n):
    if n <= 1:
        return n

    cache = [0, 1]

    for i in range(2, n+1):
        cache.append((cache[i-1] + cache[i-2]) % 10)

    return cache[n]

def fibonacci_sum_squares(n):
    return (fibonacci_last_digit(n % 60) * fibonacci_last_digit((n+1) % 60) % 10)

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
