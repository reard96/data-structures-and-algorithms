# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    units = []
    for i in range(len(weights)):
        units.append(values[i] / weights[i])

    current_weight = 0
    trigger = True

    while(trigger):
        # get highest unit
        max_unit = units.index(max(units))

        # full item taken in
        if (weights[max_unit] <= capacity):
            current_weight += weights[max_unit]
            capacity -= weights[max_unit]
            value += values[max_unit]

        else:
            current_weight += capacity
            value += units[max_unit]*capacity
            capacity = 0

        weights.pop(max_unit)
        values.pop(max_unit)
        units.pop(max_unit)

        if (capacity == 0 or len(units) == 0):
            trigger = False

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
