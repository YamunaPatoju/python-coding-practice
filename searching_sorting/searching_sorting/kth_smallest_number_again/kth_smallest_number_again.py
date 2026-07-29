import bisect

t = int(raw_input())

for _ in xrange(t):
    n, q = map(int, raw_input().split())

    intervals = []
    for _ in xrange(n):
        l, r = map(int, raw_input().split())
        intervals.append((l, r))

    intervals.sort()

    merged = []
    for l, r in intervals:
        if not merged or merged[-1][1] < l - 1:
            merged.append([l, r])
        else:
            merged[-1][1] = max(merged[-1][1], r)

    prefix = []
    total = 0
    for l, r in merged:
        total += (r - l + 1)
        prefix.append(total)

    for _ in xrange(q):
        k = int(raw_input())

        if not prefix or k > prefix[-1]:
            print -1
            continue

        idx = bisect.bisect_left(prefix, k)

        prev = 0 if idx == 0 else prefix[idx - 1]
        l, r = merged[idx]

        print l + (k - prev - 1)
