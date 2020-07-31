# Uses python3
import sys

def optimal_summands(n):
    summands = []
    candy_required = 1

    while n >= candy_required:
        summands.append(candy_required)
        n -= candy_required
        candy_required += 1

    # last time through add remaining candy for first prize
    summands[-1] = summands[-1] + n

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
