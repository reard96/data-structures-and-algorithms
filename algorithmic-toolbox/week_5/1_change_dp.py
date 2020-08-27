# Uses python3
import sys
import math

def get_change(m):
    coins = [1, 3, 4]
    min_coins = [0] + [math.inf] * m

    if m == 0:
        return 0

    for i in range(1, m+1):
        for coin in coins:
            if i >= coin:
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1

    return min_coins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
