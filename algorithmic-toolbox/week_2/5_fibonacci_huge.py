# Uses python3
import sys

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    cache = [0, 1]
    previousMod = 0
    currentMod = 1

    for i in range(n - 1):
        tempMod = previousMod
        previousMod = currentMod % m
        currentMod = (tempMod + currentMod) % m
        cache.append(currentMod)
        if currentMod == 1 and previousMod == 0:
            index = n % (i + 1)
            return cache[index]

    return currentMod

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
