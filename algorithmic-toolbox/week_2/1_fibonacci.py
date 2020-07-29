# Uses python3
def fibonacci(n):
    if n <= 1:
        return n

    cache = [0, 1]

    for i in range(2, n+1):
        cache.append(cache[i-1] + cache[i-2])

    return cache[n]

n = int(input())
print(fibonacci(n))
