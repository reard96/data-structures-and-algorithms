# Uses python3
def edit_distance(s, t):
    n = len(s)
    m = len(t)

    # array of distances
    distances = [[0] * (m+1) for i in range(n+1)]

    # initialize zero row and column
    for i in range(n+1):
        distances[i][0] = i
    for j in range(m+1):
        distances[0][j] = j

    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion = distances[i][j-1] + 1
            deletion = distances[i-1][j] + 1
            match = distances[i-1][j-1]
            mismatch = distances[i-1][j-1] + 1

            # check whether there is a match
            if s[i-1] == t[j-1]:
                distances[i][j] = min(insertion, deletion, match)
            else:
                distances[i][j] = min(insertion, deletion, mismatch)

    return distances[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
