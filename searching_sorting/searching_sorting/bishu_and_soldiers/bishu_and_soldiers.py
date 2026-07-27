from bisect import bisect_right

n = int(raw_input())
arr = list(map(int, raw_input().split()))

arr.sort()

prefix = [0] * n
prefix[0] = arr[0]

for i in range(1, n):
    prefix[i] = prefix[i - 1] + arr[i]

q = int(raw_input())

for _ in range(q):
    power = int(raw_input())

    idx = bisect_right(arr, power)

    if idx == 0:
        print 0, 0
    else:
        print idx, prefix[idx - 1]
