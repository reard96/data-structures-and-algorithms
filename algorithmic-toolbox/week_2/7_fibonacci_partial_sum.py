# Uses python3
import sys

def fibonacci_partial_sum(from_, to):
    sumArray = [1, 1]

    for _ in range(from_, to):
        sumArray.append((sumArray[-1] + sumArray[-2]) % 10)

    return (sumArray[-1] - 1) % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
