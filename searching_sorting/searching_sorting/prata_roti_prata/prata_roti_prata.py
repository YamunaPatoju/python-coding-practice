t = int(input())

for _ in range(t):
    p = int(input())

    data = list(map(int, input().split()))
    l = data[0]
    ranks = data[1:]

    def canCook(time):
        total = 0

        for r in ranks:
            curr = 0
            cnt = 1

            while curr + cnt * r <= time:
                curr += cnt * r
                total += 1
                cnt += 1

                if total >= p:
                    return True

        return False

    low = 0
    high = max(ranks) * p * (p + 1) // 2

    while low < high:
        mid = (low + high) // 2

        if canCook(mid):
            high = mid
        else:
            low = mid + 1

    print(low)
