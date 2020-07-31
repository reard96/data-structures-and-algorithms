# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    # sort segments by largest value
    segments.sort(key = lambda x: x[1])

    # intialize first point
    points = [segments[0][1]]

    for s in segments:
        # ignore points included already
        if not(s[0] <= points[-1] <= s[1]):
            points.append(s[1])

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
