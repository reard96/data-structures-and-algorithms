# Uses python3
import sys

def fibonacci_last_digit(n):
    if n <= 1:
        return n

    cache = [0, 1]

    for i in range(2, n+1):
        cache.append((cache[i-1] + cache[i-2]) % 10)

    return cache[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_last_digit(n))
