# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    cnt = {}
    segments = 0

    list_points = [(x, 'l') for x in starts]
    list_points += [(x, 'p') for x in points]
    list_points += [(x, 'r') for x in ends]

    list_points.sort()

    for p in list_points:
        if p[1] == 'l':
            segments += 1
        elif p[1] == 'r':
            segments -= 1
        else:
            cnt[p[0]] = segments

    return [cnt[x] for x in points]


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
