# python3
import sys


def compute_min_refills(distance, tank, stops):
    # number of gas stations
    n = len(stops)

    # add start and end points
    stops.insert(0, 0)
    stops.append(distance)

    numRefills = 0
    currentRefill = 0

    while currentRefill <= n:
        lastRefill = currentRefill
        while (currentRefill <= n and stops[currentRefill+1] - stops[lastRefill] <= tank):
            currentRefill += 1
        if currentRefill == lastRefill:
            return -1
        elif currentRefill <= n:
            numRefills += 1

    return numRefills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
