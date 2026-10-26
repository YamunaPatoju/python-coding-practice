t = int(input())
input()

for case in range(t):
    m, n = map(int, input().split())

    x = [int(input()) for _ in range(m - 1)]
    y = [int(input()) for _ in range(n - 1)]

    x.sort(reverse=True)
    y.sort(reverse=True)

    i = 0
    j = 0
    vertical = 1
    horizontal = 1
    cost = 0

    while i < len(x) and j < len(y):
        if x[i] >= y[j]:
            cost += x[i] * horizontal
            vertical += 1
            i += 1
        else:
            cost += y[j] * vertical
            horizontal += 1
            j += 1

    while i < len(x):
        cost += x[i] * horizontal
        i += 1

    while j < len(y):
        cost += y[j] * vertical
        j += 1

    print(cost)

    if case < t - 1:
        input()
