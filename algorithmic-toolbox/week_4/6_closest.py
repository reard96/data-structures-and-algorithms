#Uses python3
import sys
import math

# utility function for distance between 2 points
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def min_distance_sorted(x, y):
    coordinates = list(zip(x, y))
    coordinates = sorted(coordinates, key=lambda x: x[0])
    return smallest_distance(coordinates)

def smallest_distance(coordinates):
    N = len(coordinates)

    # brute force base case
    if N <= 3:
        x, y = [list(point) for point in zip(*coordinates)]
        return brute_force(x, y)

    mid = N // 2

    d1 = smallest_distance(coordinates[:mid])
    d2 = smallest_distance(coordinates[mid:])
    d3 = min(d1, d2)

    mid_coordinates = [c for c in coordinates if abs(coordinates[mid][0] - c[0]) < d3]

    return check_middle(mid_coordinates, d3)

def check_middle(coordinates, d):
    min_dist = d
    N = len(coordinates)
    coordinates = sorted(coordinates, key=lambda x: x[1])

    for i in range(N-1):
        p1 = coordinates[i]
        for j in range(i+1, min(i+7, N)):
            p2 = coordinates[j]
            distance = dist(p1, p2)

            if distance < min_dist:
                min_dist = distance
    return min_dist

def brute_force(x, y):
    coordinates = list(zip(x, y))

    min_dist = 10**18

    for i in range(len(coordinates)-1):
        p1 = coordinates[i]
        for j in range(i+1, len(coordinates)):
            p2 = coordinates[j]
            distance = dist(p1, p2)

            if distance < min_dist:
                min_dist = distance
    return min_dist

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(min_distance_sorted(x, y)))
